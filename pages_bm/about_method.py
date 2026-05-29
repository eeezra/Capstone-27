import streamlit as st

def render_about_method():
    st.markdown("""
    <style>
    .step-card {
        background:white;border-radius:16px;
        padding:22px 20px;margin-bottom:14px;
        border:1px solid #f0e0e8;
        display:flex;gap:16px;align-items:flex-start;
    }
    .step-icon-wrap {
        width:44px;height:44px;border-radius:12px;
        display:flex;align-items:center;justify-content:center;
        font-size:20px;flex-shrink:0;
    }
    .step-badge {
        width:24px;height:24px;border-radius:50%;
        display:flex;align-items:center;justify-content:center;
        font-size:12px;font-weight:700;color:white;
        flex-shrink:0;margin-top:2px;
    }
    .tag-pill {
        display:inline-block;padding:2px 9px;
        border-radius:999px;font-size:11px;font-weight:600;
        margin:2px;background:#f0f0f0;color:#555;
    }
    .pipeline-wrap {
        background:linear-gradient(135deg,#fce8ef,#e8f5e9);
        border-radius:16px;padding:22px 24px;
        margin-bottom:24px;border:1px solid rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("## About the Method")
    st.markdown("<p style='color:#888;margin-top:-8px;'>How Beauty Match analyzes your skin and recommends foundations</p>",
                unsafe_allow_html=True)

    # Processing pipeline visual
    st.markdown("""
    <div class="pipeline-wrap">
        <div style="font-weight:700;font-size:15px;
            color:#1a1a1a;margin-bottom:16px;">Processing Pipeline</div>
        <div style="display:flex;flex-wrap:wrap;
            align-items:center;gap:8px;">
            <div style="background:white;border-radius:8px;
                padding:7px 14px;font-size:13px;font-weight:600;
                border:1px solid rgba(0,0,0,0.08);">
                ⬆️ Upload Image
            </div>
            <span style="color:#aaa;font-size:18px;">→</span>
            <div style="background:white;border-radius:8px;
                padding:7px 14px;font-size:13px;font-weight:600;
                border:1px solid rgba(0,0,0,0.08);">
                🔍 Face Detection
            </div>
            <span style="color:#aaa;font-size:18px;">→</span>
            <div style="background:white;border-radius:8px;
                padding:7px 14px;font-size:13px;font-weight:600;
                border:1px solid rgba(0,0,0,0.08);">
                🎭 Skin Area Extraction
            </div>
            <span style="color:#aaa;font-size:18px;">→</span>
            <div style="background:white;border-radius:8px;
                padding:7px 14px;font-size:13px;font-weight:600;
                border:1px solid rgba(0,0,0,0.08);">
                🎨 RGB to LAB Conversion
            </div>
            <span style="color:#aaa;font-size:18px;">→</span>
            <br style="width:100%;">
            <div style="background:white;border-radius:8px;
                padding:7px 14px;font-size:13px;font-weight:600;
                border:1px solid rgba(0,0,0,0.08);margin-top:8px;">
                📊 K-Means Clustering
            </div>
            <span style="color:#aaa;font-size:18px;">→</span>
            <div style="background:white;border-radius:8px;
                padding:7px 14px;font-size:13px;font-weight:600;
                border:1px solid rgba(0,0,0,0.08);">
                📐 Euclidean Distance Matching
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    steps = [
        {
            "icon": "⬆️",
            "icon_bg": "#fce8ef",
            "badge_bg": "#e91e8c",
            "num": "1",
            "label_bg": "#fce8ef",
            "label_color": "#c0587e",
            "label": "Input Layer",
            "title": "Upload Image",
            "tags": ["Input Validation", "Image Resizing", "EXIF Strip"],
            "desc": (
                "User uploads a facial photo via drag-and-drop or webcam capture. "
                "Supported formats: JPG, PNG, WebP. Image is pre-processed to "
                "normalize resolution and remove EXIF metadata."
            ),
        },
        {
            "icon": "🔍",
            "icon_bg": "#fce8ef",
            "badge_bg": "#e91e8c",
            "num": "2",
            "label_bg": "#fce8ef",
            "label_color": "#c0587e",
            "label": "MediaPipe FaceMesh",
            "title": "Face Detection",
            "tags": ["MediaPipe", "FaceMesh", "468 Landmarks"],
            "desc": (
                "MediaPipe FaceMesh detects 468 3D facial landmarks. "
                "This step identifies the face region and establishes landmark "
                "coordinates used in the next step to isolate skin pixels."
            ),
        },
        {
            "icon": "🎭",
            "icon_bg": "#e8f5e9",
            "badge_bg": "#4caf50",
            "num": "3",
            "label_bg": "#e8f5e9",
            "label_color": "#2e7d32",
            "label": "Polygon Masking",
            "title": "Skin Area Extraction",
            "tags": ["Polygon ROI", "Binary Mask", "OpenCV"],
            "desc": (
                "Cheek, forehead, and chin regions are defined using facial landmark "
                "polygons. A binary mask isolates skin pixels, excluding eyes, lips, "
                "eyebrows, and background to reduce color interference."
            ),
        },
        {
            "icon": "🎨",
            "icon_bg": "#e8f5e9",
            "badge_bg": "#4caf50",
            "num": "4",
            "label_bg": "#e8f5e9",
            "label_color": "#2e7d32",
            "label": "Perceptual Color Space",
            "title": "RGB to LAB Conversion",
            "tags": ["CIE LAB", "sRGB", "Color Transform"],
            "desc": (
                "Extracted skin pixels are converted from sRGB to CIE LAB color space. "
                "LAB is perceptually uniform, meaning numerical distances correspond "
                "more closely to human-perceived color differences."
            ),
        },
        {
            "icon": "📊",
            "icon_bg": "#fce8ef",
            "badge_bg": "#e91e8c",
            "num": "5",
            "label_bg": "#fce8ef",
            "label_color": "#c0587e",
            "label": "Clustering",
            "title": "K-Means Clustering",
            "tags": ["K-Means (k=3)", "Scikit-learn", "Cluster Centroid"],
            "desc": (
                "K-Means clustering (k=3) groups skin pixels into dominant color "
                "clusters. The centroid of the largest cluster represents your "
                "primary skin color for downstream matching."
            ),
        },
        {
            "icon": "📐",
            "icon_bg": "#e8f5e9",
            "badge_bg": "#4caf50",
            "num": "6",
            "label_bg": "#e8f5e9",
            "label_color": "#2e7d32",
            "label": "Matching Engine",
            "title": "Euclidean Distance Matching",
            "tags": ["Delta-E", "Foundation DB", "Ranked Results"],
            "desc": (
                "Your skin LAB values are compared against a curated foundation "
                "database using Euclidean distance in LAB space (ΔE). Foundations "
                "are ranked from closest to furthest color match."
            ),
        },
    ]

    for step in steps:
        tags_html = " ".join(
            f'<span class="tag-pill">{t}</span>'
            for t in step["tags"]
        )
        st.markdown(f"""
        <div class="step-card">
            <div class="step-icon-wrap"
                style="background:{step['icon_bg']};">
                {step['icon']}
            </div>
            <div style="flex:1;">
                <div style="display:flex;justify-content:space-between;
                    align-items:flex-start;flex-wrap:wrap;gap:8px;
                    margin-bottom:6px;">
                    <div>
                        <div style="font-weight:700;font-size:15px;
                            color:#1a1a1a;">{step['title']}</div>
                        <div style="
                            display:inline-block;margin-top:3px;
                            background:{step['label_bg']};
                            color:{step['label_color']};
                            border-radius:999px;padding:2px 10px;
                            font-size:11px;font-weight:700;">
                            {step['label']}
                        </div>
                    </div>
                    <div style="display:flex;gap:4px;flex-wrap:wrap;
                        justify-content:flex-end;">{tags_html}</div>
                </div>
                <div style="display:flex;align-items:flex-start;gap:10px;">
                    <div class="step-badge"
                        style="background:{step['badge_bg']};">
                        {step['num']}
                    </div>
                    <div style="font-size:13px;color:#666;
                        line-height:1.7;">{step['desc']}</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Accuracy note
    st.markdown("""
    <div style="
        background:linear-gradient(135deg,#fce8ef,#fdf6e3);
        border-radius:16px;padding:22px 24px;
        margin-top:8px;border:1px solid rgba(192,88,126,0.15);">
        <div style="font-weight:700;font-size:15px;
            margin-bottom:8px;">📌 Note on Accuracy</div>
        <div style="font-size:13px;color:#666;line-height:1.7;">
            Results are most accurate when the photo is taken in natural light
            without filters or heavy makeup. The model has been validated on a
            diverse dataset covering MST 1–10. Individual results may vary based
            on lighting conditions, camera quality, and photo angle.
        </div>
    </div>
    """, unsafe_allow_html=True)
