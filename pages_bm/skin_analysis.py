import streamlit as st
import numpy as np
import cv2

def render_skin_analysis():
    st.markdown("""
    <style>
    .preview-empty{
        min-height:320px;
        border-radius:20px;
        border:1px solid rgba(255,168,214,.25);
        background:rgba(255,255,255,.8);
        display:flex;
        flex-direction:column;
        align-items:center;
        justify-content:center;
        text-align:center;
        color:#7B6472;
    }

    .tip-card{
        background:rgba(255,255,255,.82);
        border-radius:20px;
        padding:22px;
        border:1px solid rgba(255,168,214,.25);
        margin-top:16px;
    }

    .tip-grid{
        display:grid;
        grid-template-columns:1fr 1fr;
        gap:16px;
    }

    .tip-item{
        display:flex;
        gap:10px;
        align-items:flex-start;
    }

    .tip-icon{
        width:34px;
        height:34px;
        border-radius:999px;
        background:#FFF0F5;
        display:flex;
        align-items:center;
        justify-content:center;
        flex-shrink:0;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="page-title">Skin Analysis</div>
    <div class="page-subtitle">
        Upload a clear photo of your face to get started
    </div>
    """, unsafe_allow_html=True)

    mode = st.radio(
        "",
        ["Upload Photo", "Webcam Capture"],
        horizontal=True,
        label_visibility="collapsed"
    )

    left, right = st.columns([1.8, 1], gap="large")

    if mode == "Upload Photo":

        with left:
            uploaded = st.file_uploader(
                "",
                type=["jpg", "jpeg", "png"],
                label_visibility="collapsed",
                key="upload_file"
            )

            st.markdown("""
            <div class="tip-card">
                <div style="font-weight:800;margin-bottom:16px;">
                    Photo Tips for Best Results
                </div>

                <div class="tip-grid">

                    <div class="tip-item">
                        <div class="tip-icon">☀️</div>
                        <div>
                            <b>Natural Lighting</b><br>
                            Use soft daylight or window light.
                        </div>
                    </div>

                    <div class="tip-item">
                        <div class="tip-icon">🚫</div>
                        <div>
                            <b>No Filters</b><br>
                            Upload original photos only.
                        </div>
                    </div>

                    <div class="tip-item">
                        <div class="tip-icon">🙂</div>
                        <div>
                            <b>Face Clearly Visible</b><br>
                            Center your face in the frame.
                        </div>
                    </div>

                    <div class="tip-item">
                        <div class="tip-icon">💄</div>
                        <div>
                            <b>Minimal Makeup</b><br>
                            Gives the most accurate result.
                        </div>
                    </div>

                </div>
            </div>
            """, unsafe_allow_html=True)

        with right:

            if uploaded:
                file_bytes = np.asarray(bytearray(uploaded.read()), dtype=np.uint8)
                img_bgr = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
                img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

                st.session_state["input_image"] = img_rgb

                st.image(img_rgb, use_container_width=True)
            else:
                st.markdown("""
                <div class="preview-empty">
                    <div style="font-size:3rem;">📷</div>
                    <div><b>No photo selected</b></div>
                    <div>Upload a photo to preview it here</div>
                </div>
                """, unsafe_allow_html=True)

            disabled = "input_image" not in st.session_state

            if st.button(
                "Analyze Now →",
                type="primary",
                use_container_width=True,
                disabled=disabled,
                key="analyze_upload"
            ):
                _run_analysis()

    else:

        with left:
            cam_img = st.camera_input(
                "",
                label_visibility="collapsed"
            )

            if cam_img:
                file_bytes = np.asarray(bytearray(cam_img.read()), dtype=np.uint8)
                img_bgr = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
                img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
                img_rgb = cv2.flip(img_rgb, 1)

                st.session_state["input_image"] = img_rgb

        with right:

            if "input_image" in st.session_state:
                st.image(
                    st.session_state["input_image"],
                    use_container_width=True
                )
            else:
                st.markdown("""
                <div class="preview-empty">
                    <div style="font-size:3rem;">📷</div>
                    <div><b>No photo selected</b></div>
                    <div>Capture a photo to preview it here</div>
                </div>
                """, unsafe_allow_html=True)

            disabled = "input_image" not in st.session_state

            if st.button(
                "Analyze Now →",
                type="primary",
                use_container_width=True,
                disabled=disabled,
                key="analyze_cam"
            ):
                _run_analysis()


def _run_analysis():

    if "input_image" not in st.session_state:
        st.warning("Please upload or capture a photo first.")
        return

    try:
        from core.pipeline import (
            load_resources,
            run_pipeline,
            FEATURE_COLS
        )

        with st.spinner("Analyzing your skin tone..."):

            (
                face_mesh,
                ensemble,
                scaler,
                kmeans,
                df_found,
                centroids,
                mst_hex_lookup
            ) = load_resources()

            result, error = run_pipeline(
                st.session_state["input_image"],
                face_mesh,
                ensemble,
                scaler,
                kmeans,
                centroids,
                df_found,
                mst_hex_lookup,
                FEATURE_COLS
            )

        if error:
            st.error(error)
            return

        st.session_state["analysis_result"] = result
        st.session_state.page = "Results"
        st.rerun()

    except Exception as e:
        st.error(f"Analysis failed: {e}")
