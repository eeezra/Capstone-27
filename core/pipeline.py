import os
import time
import math
import urllib.request

import numpy as np
import cv2
import joblib
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from scipy.signal import wiener
from skimage.color import rgb2lab, lab2rgb
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import streamlit as st
from datetime import datetime

# ─────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────
BASE_DIR       = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR      = os.path.join(BASE_DIR, "models")
FOUNDATION_CSV = os.path.join(BASE_DIR, "foundation_mst_full_most_updated.csv")

FEATURE_COLS = [
    'cheek_L_mean', 'cheek_L_std', 'cheek_a_mean', 'cheek_a_std',
    'cheek_b_mean', 'cheek_b_std', 'cheek_ITA',
    'forehead_L_mean', 'forehead_L_std', 'forehead_a_mean', 'forehead_a_std',
    'forehead_b_mean', 'forehead_b_std', 'forehead_ITA',
    'nose_L_mean', 'nose_L_std', 'nose_a_mean', 'nose_a_std',
    'nose_b_mean', 'nose_b_std', 'nose_ITA',
    'global_L_mean', 'global_L_std', 'global_a_mean', 'global_a_std',
    'global_b_mean', 'global_b_std', 'global_ITA',
]

MP_LANDMARK_MAP = {
    0:  234, 1:  227, 8:  152, 15: 447, 16: 454,
    17: 70,  18: 63,  19: 66,  20: 65,  21: 55,
    22: 285, 23: 295, 24: 282, 25: 283, 26: 296,
    27: 168, 28: 6,   29: 197, 30: 195, 31: 5,
    32: 4,   33: 1,   34: 19,  35: 94,
}

# ─────────────────────────────────────────────
# DOWNLOAD MODEL
# ─────────────────────────────────────────────
def download_face_landmarker():
    model_path = os.path.join(MODEL_DIR, "face_landmarker.task")
    if not os.path.exists(model_path):
        os.makedirs(MODEL_DIR, exist_ok=True)
        url = (
            "https://storage.googleapis.com/mediapipe-models/"
            "face_landmarker/face_landmarker/float16/1/face_landmarker.task"
        )
        urllib.request.urlretrieve(url, model_path)
    return model_path

# ─────────────────────────────────────────────
# LOAD RESOURCES (cached)
# ─────────────────────────────────────────────
@st.cache_resource
def load_resources():
    from mediapipe.tasks import python as mp_tasks
    from mediapipe.tasks.python import vision as mp_vision

    model_path   = download_face_landmarker()
    base_options = mp_tasks.BaseOptions(model_asset_path=model_path)
    options      = mp_vision.FaceLandmarkerOptions(
        base_options=base_options,
        num_faces=1,
        min_face_detection_confidence=0.3,
        min_face_presence_confidence=0.3,
        min_tracking_confidence=0.3,
    )
    face_mesh = mp_vision.FaceLandmarker.create_from_options(options)

    ensemble = joblib.load(os.path.join(MODEL_DIR, "best_model.pkl"))
    scaler   = joblib.load(os.path.join(MODEL_DIR, "scaler.pkl"))

    kmeans_path = next(
        (os.path.join(MODEL_DIR, f) for f in os.listdir(MODEL_DIR)
         if f.startswith("kmeans_k") and f.endswith(".pkl")),
        None
    )
    if kmeans_path is None:
        raise FileNotFoundError("kmeans_k*.pkl tidak ditemukan di MODEL_DIR")
    kmeans = joblib.load(kmeans_path)

    df_found  = pd.read_csv(FOUNDATION_CSV)
    centroids = (
        df_found.groupby("mst_id")[["lab_L", "lab_a", "lab_b"]]
        .median()
        .rename(columns={"lab_L": "L_ref", "lab_a": "a_ref", "lab_b": "b_ref"})
        .reset_index()
    )
    mst_hex_lookup = (
        df_found.drop_duplicates("mst_id")
        .set_index("mst_id")["mst_hex"]
        .to_dict()
    )
    return face_mesh, ensemble, scaler, kmeans, df_found, centroids, mst_hex_lookup

# ─────────────────────────────────────────────
# PREPROCESSING
# ─────────────────────────────────────────────
def preprocess_image(img):
    lab   = cv2.cvtColor(img, cv2.COLOR_RGB2LAB)
    clahe = cv2.createCLAHE(clipLimit=1.0, tileGridSize=(16, 16))
    lab[:, :, 0] = clahe.apply(lab[:, :, 0])
    img_norm = cv2.cvtColor(lab, cv2.COLOR_LAB2RGB)
    img_blur = cv2.GaussianBlur(img_norm, (5, 5), 1.0)
    result   = np.zeros_like(img_blur, dtype=np.float32)
    for c in range(3):
        result[:, :, c] = wiener(img_blur[:, :, c].astype(np.float32), mysize=5)
    return np.clip(result, 0, 255).astype(np.uint8)

# ─────────────────────────────────────────────
# LANDMARK DETECTION
# ─────────────────────────────────────────────
def detect_landmarks(img_rgb, face_mesh):
    import mediapipe as mp_lib
    h, w     = img_rgb.shape[:2]
    mp_image = mp_lib.Image(image_format=mp_lib.ImageFormat.SRGB, data=img_rgb)
    results  = face_mesh.detect(mp_image)
    if not results.face_landmarks:
        return None, None

    mp_lms = results.face_landmarks[0]
    lms    = {
        dlib_idx: (int(mp_lms[mp_idx].x * w), int(mp_lms[mp_idx].y * h))
        for dlib_idx, mp_idx in MP_LANDMARK_MAP.items()
    }
    xs   = [p[0] for p in lms.values()]
    ys   = [p[1] for p in lms.values()]
    bbox = (min(xs), min(ys), max(xs), max(ys))
    return lms, bbox

# ─────────────────────────────────────────────
# MASK HELPERS
# ─────────────────────────────────────────────
def make_cheek_ellipse_mask(img_shape, landmarks):
    h, w   = img_shape[:2]
    mid_y  = (landmarks[27][1] + landmarks[8][1]) // 2
    face_w = landmarks[16][0] - landmarks[0][0]
    ew, eh = int(face_w * 0.18), int(face_w * 0.13)
    mask   = np.zeros((h, w), dtype=np.uint8)
    cv2.ellipse(mask, (landmarks[1][0] + ew,  mid_y), (ew, eh), 0, 0, 360, 1, -1)
    cv2.ellipse(mask, (landmarks[15][0] - ew, mid_y), (ew, eh), 0, 0, 360, 1, -1)
    return mask.astype(bool)

def make_forehead_mask(img_shape, landmarks):
    h, w    = img_shape[:2]
    brow_y  = int(np.mean([landmarks[i][1] for i in range(17, 27)]))
    brow_lx = landmarks[17][0]
    brow_rx = landmarks[26][0]
    face_h  = landmarks[8][1] - landmarks[19][1]
    top_y   = max(0, brow_y - int(face_h * 0.35))
    pts     = np.array([[brow_lx, top_y], [brow_rx, top_y],
                        [brow_rx, brow_y], [brow_lx, brow_y]], dtype=np.int32)
    mask    = np.zeros((h, w), dtype=np.uint8)
    cv2.fillPoly(mask, [pts], 1)
    return mask.astype(bool)

def make_nose_mask(img_shape, landmarks):
    h, w     = img_shape[:2]
    nose_pts = np.array([landmarks[i] for i in range(27, 36)], dtype=np.int32)
    hull     = cv2.convexHull(nose_pts)
    mask     = np.zeros((h, w), dtype=np.uint8)
    cv2.fillPoly(mask, [hull], 1)
    return mask.astype(bool)

def filter_skin_pixels(lab_pixels):
    mask = (
        (lab_pixels[:, 0] >= 25) & (lab_pixels[:, 0] <= 97) &
        (lab_pixels[:, 1] >= 5)  & (lab_pixels[:, 1] <= 30) &
        (lab_pixels[:, 2] >= 5)  & (lab_pixels[:, 2] <= 40)
    )
    return lab_pixels[mask]

# ─────────────────────────────────────────────
# FEATURE EXTRACTION
# ─────────────────────────────────────────────
def get_skin_features(img_rgb, lms):
    if img_rgb.ndim == 3 and img_rgb.shape[2] == 4:
        img_rgb = img_rgb[:, :, :3]

    lab        = rgb2lab(img_rgb.astype(np.float64) / 255.0)
    all_pixels = []
    feats      = {}

    zones = {
        'cheek'   : make_cheek_ellipse_mask(img_rgb.shape, lms),
        'forehead': make_forehead_mask(img_rgb.shape, lms),
        'nose'    : make_nose_mask(img_rgb.shape, lms),
    }

    for zone_name, mask in zones.items():
        if mask.sum() < 10:
            for s in ['L_mean','L_std','a_mean','a_std','b_mean','b_std','ITA']:
                feats[f"{zone_name}_{s}"] = 0.0
            continue
        px = filter_skin_pixels(lab[mask])
        if len(px) < 5:
            for s in ['L_mean','L_std','a_mean','a_std','b_mean','b_std','ITA']:
                feats[f"{zone_name}_{s}"] = 0.0
            continue
        all_pixels.append(px)
        for ci, ch in enumerate(['L', 'a', 'b']):
            feats[f'{zone_name}_{ch}_mean'] = float(px[:, ci].mean())
            feats[f'{zone_name}_{ch}_std']  = float(px[:, ci].std())
        feats[f'{zone_name}_ITA'] = math.degrees(
            math.atan2(px[:, 0].mean() - 50, px[:, 2].mean())
        )

    if not all_pixels:
        return None

    combined = np.vstack(all_pixels)
    for ci, ch in enumerate(['L', 'a', 'b']):
        feats[f'global_{ch}_mean'] = float(combined[:, ci].mean())
        feats[f'global_{ch}_std']  = float(combined[:, ci].std())
    feats['global_ITA'] = math.degrees(
        math.atan2(combined[:, 0].mean() - 50, combined[:, 2].mean())
    )
    return feats

# ─────────────────────────────────────────────
# HYBRID PREDICTION
# ─────────────────────────────────────────────
def predict_mst_hybrid(feats, ensemble, scaler, kmeans, centroids, feature_cols,
                        alpha=0.40, temperature=0.6, sigma_eucl=2.0, sigma_ita=4.0):
    x    = np.array([[feats.get(c, 0.0) for c in feature_cols]])
    x_sc = scaler.transform(x)
    dist = kmeans.transform(x_sc)
    x_aug = np.hstack([x_sc, dist])

    model_proba   = ensemble.predict_proba(x_aug)[0]
    model_classes = ensemble.classes_
    log_p         = np.log(model_proba + 1e-10) / temperature
    model_proba   = np.exp(log_p - log_p.max())
    model_proba  /= model_proba.sum()

    L_inp   = feats.get('global_L_mean', 50)
    a_inp   = feats.get('global_a_mean', 8)
    b_inp   = feats.get('global_b_mean', 12)
    ita_inp = math.degrees(math.atan2(L_inp - 50, b_inp))

    mst_keys = centroids['mst_id'].values
    dist_arr = np.sqrt(
        (centroids['L_ref'].values - L_inp)**2 +
        (centroids['a_ref'].values - a_inp)**2 +
        (centroids['b_ref'].values - b_inp)**2
    )
    inv_dist     = np.exp(-dist_arr / sigma_eucl)
    db_proba_lab = inv_dist / inv_dist.sum()

    ita_centroids = np.degrees(np.arctan2(
        centroids['L_ref'].values - 50,
        centroids['b_ref'].values
    ))
    ita_dist     = np.abs(ita_centroids - ita_inp)
    inv_ita      = np.exp(-ita_dist / sigma_ita)
    db_proba_ita = inv_ita / inv_ita.sum()
    db_proba     = 0.60 * db_proba_lab + 0.40 * db_proba_ita

    combined = {}
    for i, mst in enumerate(mst_keys):
        idx     = np.where(model_classes == mst)[0]
        model_p = float(model_proba[idx[0]]) if len(idx) > 0 else 0.0
        combined[mst] = (1 - alpha) * model_p + alpha * float(db_proba[i])

    best_mst = max(combined, key=combined.get)
    total    = sum(combined.values())

    top3_candidates = sorted(combined.items(), key=lambda x: -x[1])
    top3 = [item for item in top3_candidates if abs(item[0] - best_mst) <= 2][:3]
    if len(top3) < 3:
        remaining = [item for item in top3_candidates if item not in top3]
        top3 += sorted(remaining, key=lambda x: abs(x[0] - best_mst))[:3 - len(top3)]

    return (
        int(best_mst),
        round(combined[best_mst] / total * 100, 1),
        [{'mst': int(m), 'conf': round(p / total * 100, 1)} for m, p in top3]
    )

# ─────────────────────────────────────────────
# RECOMMENDATION
# ─────────────────────────────────────────────
def recommend_foundation(mst_pred, L, a, b, df_found, top_n=5):
    df = df_found.copy()
    df['delta_e'] = np.sqrt(
        (df['lab_L'] - L)**2 +
        (df['lab_a'] - a)**2 +
        (df['lab_b'] - b)**2
    )
    mst_range   = [mst_pred - 1, mst_pred, mst_pred + 1]
    df_primary  = df[df['mst_id'].isin(mst_range)].sort_values('delta_e')
    df_fallback = df[~df['mst_id'].isin(mst_range)].sort_values('delta_e')
    return pd.concat([df_primary, df_fallback]).head(top_n).reset_index(drop=True)

# ─────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────
def cielab_to_hex(L, a, b):
    rgb  = lab2rgb([[[L, a, b]]])[0][0]
    rgb  = np.clip(rgb, 0, 1)
    r, g, b_ = int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255)
    return f"#{r:02x}{g:02x}{b_:02x}"

def format_rupiah(value):
    try:
        return f"Rp{float(value):,.0f}".replace(",", ".")
    except:
        return str(value)

def estimate_user_undertone(a, b):
    if b >= 14:   return "Warm"
    elif b <= 10: return "Cool"
    else:         return "Neutral"

def estimate_user_skintone(mst):
    if mst <= 3:  return "Light/Fair"
    elif mst <= 6: return "Medium"
    else:         return "Deep"

# ─────────────────────────────────────────────
# MAIN PIPELINE
# ─────────────────────────────────────────────
def run_pipeline(img_rgb, face_mesh, ensemble, scaler,
                 kmeans, centroids, df_found, mst_hex_lookup, feature_cols):
    t0 = time.time()

    if img_rgb.ndim == 3 and img_rgb.shape[2] == 4:
        img_rgb = img_rgb[:, :, :3]

    h, w = img_rgb.shape[:2]
    if max(h, w) > 512:
        scale   = 512 / max(h, w)
        img_rgb = cv2.resize(img_rgb, (int(w * scale), int(h * scale)))

    lms, bbox = detect_landmarks(img_rgb, face_mesh)
    if lms is None:
        img_pre   = preprocess_image(img_rgb)
        lms, bbox = detect_landmarks(img_pre, face_mesh)
    else:
        img_pre = preprocess_image(img_rgb)

    if lms is None:
        return None, "❌ Wajah tidak terdeteksi. Pastikan pencahayaan cukup dan wajah menghadap kamera."

    feats = get_skin_features(img_pre, lms)
    if feats is None:
        return None, "❌ Ekstraksi fitur gagal. Wajah terlalu kecil atau terhalang."

    mst, conf, top3 = predict_mst_hybrid(
        feats, ensemble, scaler, kmeans, centroids, feature_cols
    )

    top3_hex = [
        {"mst": t["mst"], "conf": t["conf"],
         "hex": mst_hex_lookup.get(t["mst"], "#888888")}
        for t in top3
    ]

    recs    = recommend_foundation(
        mst, feats["global_L_mean"], feats["global_a_mean"],
        feats["global_b_mean"], df_found, top_n=5
    )
    top_rec = recs.iloc[0]
    latency = round((time.time() - t0) * 1000, 1)

    vis = img_rgb.copy()
    if bbox:
        x1, y1, x2, y2 = bbox
        cv2.rectangle(vis, (x1, y1), (x2, y2), (0, 200, 100), 2)
    for (px, py) in lms.values():
        cv2.circle(vis, (int(px), int(py)), 1, (255, 100, 0), -1)

    skin_hex = cielab_to_hex(
        feats["global_L_mean"],
        feats["global_a_mean"],
        feats["global_b_mean"],
    )

    return {
        "mst_pred"      : mst,
        "confidence"    : conf,
        "top3"          : top3_hex,
        "shade_name"    : top_rec["Shade"],
        "brand"         : top_rec["Brand"],
        "product"       : top_rec["Product"],
        "hex_color"     : cielab_to_hex(top_rec["lab_L"], top_rec["lab_a"], top_rec["lab_b"]),
        "skin_hex"      : skin_hex,
        "user_undertone": estimate_user_undertone(feats["global_a_mean"], feats["global_b_mean"]),
        "user_skintone" : estimate_user_skintone(mst),
        "undertone"     : top_rec["Undertone"],
        "price"         : format_rupiah(top_rec["Price"]),
        "top5_recs"     : recs.to_dict(orient="records"),
        "cielab"        : {
            "L": round(feats["global_L_mean"], 2),
            "a": round(feats["global_a_mean"], 2),
            "b": round(feats["global_b_mean"], 2),
        },
        "latency_ms"    : latency,
        "vis_frame"     : vis,
    }, None
