import streamlit as st
import numpy as np
import cv2

def render():
    st.markdown("""
    <style>
    .upload-zone {
        border: 2px dashed #f4a0b8;
        border-radius: 16px;
        padding: 52px 24px;
        text-align: center;
        background: #fff8fb;
        cursor: pointer;
        transition: background 0.2s;
    }
    .upload-zone:hover { background: #fdeef4; }
    .tip-card {
        background: white;
        border-radius: 14px;
        padding: 20px;
        border: 1px solid #f0d8e4;
        margin-top: 16px;
    }
    .tip-item {
        display:flex;align-items:flex-start;
        gap:10px;margin-bottom:14px;
    }
    .tip-icon {
        width:30px;height:30px;border-radius:50%;
        background:#fff0f5;display:flex;
        align-items:center;justify-content:center;
        font-size:13px;flex-shrink:0;margin-top:1px;
    }
    .preview-empty {
        background:#fafafa;border-radius:16px;
        border:1px solid #f0e0e8;
        height:200px;display:flex;
        flex-direction:column;
        align-items:center;justify-content:center;
        color:#ccc;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("## Skin Analysis")
    st.markdown(
        "<p style='color:#999;margin-top:-8px;'>"
        "Upload a clear photo of your face to get started</p>",
        unsafe_allow_html=True
    )

    tab1, tab2 = st.tabs(["📁  Upload Photo", "📷  Webcam Capture"])

    with tab1:
        col_left, col_right = st.columns([1.4, 1], gap="large")

        with col_left:
            uploaded = st.file_uploader(
                "drag_drop",
                type=["jpg", "jpeg", "png"],
                label_visibility="collapsed",
                key="upload_file",
            )
            if uploaded is None:
                st.markdown("""
                <div class="upload-zone">
                    <div style="font-size:36px;margin-bottom:10px;">⬆️</div>
                    <div style="font-weight:600;font-size:15px;color:#666;">
                        Drop your photo here
                    </div>
                    <div style="font-size:13px;color:#bbb;margin-top:4px;">
                        or click to browse — JPG, PNG up to 10MB
                    </div>
                </div>
                """, unsafe_allow_html=True)

            # Tips
            st.markdown("""
            <div class="tip-card">
                <div style="font-weight:700;font-size:14px;
                    color:#444;margin-bottom:14px;">
                    📋 Photo Tips for Best Results
                </div>
                <div class="tip-item">
                    <div class="tip-icon">☀️</div>
                    <div>
                        <div style="font-weight:600;font-size:13px;
                            color:#333;">Natural Lighting</div>
                        <div style="font-size:12px;color:#999;">
                            Face a window or use soft daylight — avoid harsh flash
                        </div>
                    </div>
                </div>
                <div class="tip-item">
                    <div class="tip-icon">🙂</div>
                    <div>
                        <div style="font-weight:600;font-size:13px;
                            color:#333;">Face Clearly Visible</div>
                        <div style="font-size:12px;color:#999;">
                            Make sure your entire face is centered and unobstructed
                        </div>
                    </div>
                </div>
                <div class="tip-item">
                    <div class="tip-icon">🚫</div>
                    <div>
                        <div style="font-weight:600;font-size:13px;
                            color:#333;">No Filters</div>
                        <div style="font-size:12px;color:#999;">
                            Upload the original photo without any beauty filter applied
                        </div>
                    </div>
                </div>
                <div class="tip-item" style="margin-bottom:0;">
                    <div class="tip-icon">💋</div>
                    <div>
                        <div style="font-weight:600;font-size:13px;
                            color:#333;">Minimal Makeup</div>
                        <div style="font-size:12px;color:#999;">
                            Bare skin or light coverage for most accurate results
                        </div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        with col_right:
            preview_placeholder = st.empty()

            if uploaded:
                file_bytes = np.asarray(bytearray(uploaded.read()), dtype=np.uint8)
                img_bgr    = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
                img_rgb    = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
                st.session_state["input_image"] = img_rgb
                preview_placeholder.image(
                    img_rgb, use_container_width=True, caption="Preview"
                )
            else:
                preview_placeholder.markdown("""
                <div class="preview-empty">
                    <div style="font-size:32px;">📷</div>
                    <div style="font-size:13px;margin-top:8px;">No photo selected</div>
                    <div style="font-size:12px;">Upload or capture a photo to preview it here</div>
                </div>
                """, unsafe_allow_html=True)

            analyze_disabled = "input_image" not in st.session_state

            if st.button(
                "Analyze Now  →",
                use_container_width=True,
                type="primary",
                disabled=analyze_disabled,
                key="analyze_btn_upload",
            ):
                _run_analysis()

            if analyze_disabled:
                st.markdown(
                    "<p style='text-align:center;font-size:12px;"
                    "color:#bbb;margin-top:4px;'>"
                    "Upload a photo first to enable analysis</p>",
                    unsafe_allow_html=True
                )

            st.markdown(
                "<div style='text-align:center;margin-top:6px;'>"
                "<a href='#' style='color:#c0587e;font-size:13px;'>"
                "Use demo image</a></div>",
                unsafe_allow_html=True
            )

    with tab2:
        col_cam_l, col_cam_r = st.columns([1.4, 1], gap="large")
        with col_cam_l:
            cam_img = st.camera_input(
                "Take a photo", label_visibility="collapsed"
            )
            if cam_img:
                file_bytes = np.asarray(bytearray(cam_img.read()), dtype=np.uint8)
                img_bgr    = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
                img_rgb    = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
                img_rgb    = cv2.flip(img_rgb, 1)
                st.session_state["input_image"] = img_rgb

        with col_cam_r:
            if "input_image" in st.session_state and cam_img:
                st.image(
                    st.session_state["input_image"],
                    use_container_width=True,
                    caption="Preview"
                )
            if st.button(
                "Analyze Now  →",
                use_container_width=True,
                type="primary",
                disabled="input_image" not in st.session_state,
                key="analyze_btn_cam",
            ):
                _run_analysis()


def _run_analysis():
    if "input_image" not in st.session_state:
        st.warning("Please upload or capture a photo first.")
        return
    try:
        from core.pipeline import load_resources, run_pipeline, FEATURE_COLS
        with st.spinner("Analyzing your skin tone…"):
            (face_mesh, ensemble, scaler,
             kmeans, df_found, centroids, mst_hex_lookup) = load_resources()
            result, error = run_pipeline(
                st.session_state["input_image"],
                face_mesh, ensemble, scaler,
                kmeans, centroids, df_found,
                mst_hex_lookup, FEATURE_COLS
            )
        if error:
            st.error(error)
        else:
            st.session_state["analysis_result"] = result
            st.session_state["nav_target"] = "results"
            st.rerun()
    except Exception as e:
        st.error(f"Analysis failed: {e}")
