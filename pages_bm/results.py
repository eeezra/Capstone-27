import streamlit as st

def _lab_to_hex(L, a, b):
    try:
        from skimage.color import lab2rgb
        import numpy as np
        rgb = lab2rgb([[[L, a, b]]])[0][0]
        rgb = (rgb * 255).clip(0, 255).astype(int)
        return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"
    except:
        return "#c8956c"


def render():
    st.markdown("""
    <style>
    .result-card {
        background:white;border-radius:16px;
        padding:22px 20px;border:1px solid #f0d8e4;
        margin-bottom:16px;
    }
    .result-card-label {
        font-size:11px;font-weight:700;
        text-transform:uppercase;letter-spacing:1px;
        color:#bbb;margin-bottom:6px;
    }
    .result-card-value {
        font-size:20px;font-weight:800;color:#1a1a1a;
    }
    .result-card-sub { font-size:12px;color:#bbb;margin-top:4px; }
    .conf-bar-wrap {
        background:#f0ece8;border-radius:999px;
        height:8px;overflow:hidden;margin:8px 0;
    }
    .lab-grid {
        display:grid;grid-template-columns:repeat(3,1fr);
        gap:12px;margin-top:4px;
    }
    .lab-cell {
        background:#fff8fb;border-radius:10px;
        padding:12px 14px;border:1px solid #f0d8e4;
    }
    .lab-cell-label { font-size:11px;color:#bbb;margin-bottom:4px; }
    .lab-cell-val { font-size:20px;font-weight:700;color:#333; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("## Analysis Results")
    st.markdown(
        "<p style='color:#999;margin-top:-8px;'>"
        "Here's what we found from your skin tone analysis</p>",
        unsafe_allow_html=True
    )

    result = st.session_state.get("analysis_result")

    if result is None:
        st.markdown("""
        <div style="background:#fff8fb;border-radius:16px;
            padding:40px;text-align:center;
            border:1px solid #f0d8e4;">
            <div style="font-size:40px;margin-bottom:12px;">📊</div>
            <div style="font-weight:700;font-size:16px;
                color:#333;margin-bottom:8px;">
                No analysis result yet
            </div>
            <div style="font-size:13px;color:#999;">
                Please go to Skin Analysis and analyze a photo first.
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        _, c, _ = st.columns([1, 1, 1])
        with c:
            if st.button("→ Go to Skin Analysis",
                         use_container_width=True, type="primary"):
                st.session_state["nav_target"] = "skin"
                st.rerun()
        return

    mst      = result["mst_pred"]
    conf     = result["confidence"]
    lab      = result["cielab"]
    skin_hex = result.get("skin_hex",
                          _lab_to_hex(lab["L"], lab["a"], lab["b"]))
    undertone = result.get("user_undertone", "Warm")
    skintone  = result.get("user_skintone", "Medium")

    # ── Top Metric Cards ─────────────────────────────────
    m1, m2, m3, m4 = st.columns(4, gap="medium")
    card_data = [
        ("#fff0f5", "#f9d0de", "SKIN TONE",   skintone,      "Classification"),
        ("#fdf6e3", "#f0e0a0", "UNDERTONE",   undertone,     "Color Bias"),
        ("#eef4e8", "#c8ddb0", "MST SCORE",   f"{mst} / 10", "Monk Scale"),
        ("#f0ecf8", "#d8c8f0", "CONFIDENCE",  f"{conf}%",    "Accuracy"),
    ]
    for col, (bg, border, label, value, sub) in zip(
        [m1, m2, m3, m4], card_data
    ):
        with col:
            st.markdown(f"""
            <div style="background:{bg};border-radius:14px;
                padding:20px 16px;
                border:1px solid {border};">
                <div class="result-card-label">{label}</div>
                <div class="result-card-value"
                    style="font-size:17px;">{value}</div>
                <div class="result-card-sub">{sub}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    left_col, right_col = st.columns([1, 1.3], gap="large")

    with left_col:
        # Skin color swatch
        st.markdown(f"""
        <div style="
            background:{skin_hex};border-radius:16px;
            height:140px;display:flex;align-items:center;
            justify-content:center;margin-bottom:16px;
            box-shadow:0 4px 20px rgba(0,0,0,0.12);">
            <span style="
                background:rgba(0,0,0,0.22);color:white;
                padding:6px 14px;border-radius:8px;
                font-size:14px;font-weight:700;
                letter-spacing:1px;">
                {skin_hex.upper()}
            </span>
        </div>
        """, unsafe_allow_html=True)

        # Color details
        r_hex    = skin_hex.lstrip("#")
        r, g, b_ = tuple(int(r_hex[i:i+2], 16) for i in (0, 2, 4))
        st.markdown(f"""
        <div class="result-card">
            <div style="font-weight:700;font-size:15px;
                margin-bottom:14px;color:#1a1a1a;">
                Detected Skin Color
            </div>
            <table style="width:100%;border-collapse:collapse;">
                <tr>
                    <td style="color:#bbb;font-size:13px;
                        padding:6px 0;">HEX</td>
                    <td style="font-weight:700;font-size:13px;
                        text-align:right;color:#333;">
                        {skin_hex.upper()}
                    </td>
                </tr>
                <tr>
                    <td style="color:#bbb;font-size:13px;
                        padding:6px 0;">RGB</td>
                    <td style="font-weight:700;font-size:13px;
                        text-align:right;color:#333;">
                        {r},  {g},  {b_}
                    </td>
                </tr>
                <tr>
                    <td style="color:#bbb;font-size:13px;
                        padding:6px 0;">LAB</td>
                    <td style="font-weight:700;font-size:13px;
                        text-align:right;color:#333;">
                        {lab['L']},  {lab['a']},  {lab['b']}
                    </td>
                </tr>
            </table>
        </div>
        """, unsafe_allow_html=True)

        # Undertone card
        ut_cfg = {
            "Warm":    ("#fdf6e3", "#f0e0a0", "#8a6020",
                        ["#c8956c", "#b87d55", "#a06840"],
                        "Warm undertones have golden, peachy, or yellow hues. "
                        "They suit foundations with yellow or golden bases."),
            "Cool":    ("#eef0f8", "#c8d0f0", "#3050a0",
                        ["#c0a0b8", "#a08898", "#907080"],
                        "Cool undertones have pink, red, or bluish hues. "
                        "They suit foundations with pink or rosy bases."),
            "Neutral": ("#eef4e8", "#c8ddb0", "#4a7040",
                        ["#c4a882", "#b09070", "#9c7e5e"],
                        "Neutral undertones are a mix of warm and cool. "
                        "Most foundation shades will work well."),
        }
        bg_ut, border_ut, text_ut, swatches, desc_ut = ut_cfg.get(
            undertone, ut_cfg["Neutral"]
        )
        sw_html = "".join(
            f'<div style="width:30px;height:30px;border-radius:50%;'
            f'background:{s};display:inline-block;margin-right:6px;'
            f'border:2px solid rgba(0,0,0,0.08);"></div>'
            for s in swatches
        )
        st.markdown(f"""
        <div style="background:{bg_ut};border-radius:14px;
            padding:18px;border:1px solid {border_ut};">
            <div style="font-weight:700;font-size:15px;
                color:{text_ut};margin-bottom:8px;">
                Undertone: {undertone}
            </div>
            <div style="font-size:13px;color:#666;
                margin-bottom:12px;line-height:1.7;">
                {desc_ut}
            </div>
            {sw_html}
        </div>
        """, unsafe_allow_html=True)

    with right_col:
        # MST Scale
        mst_colors = {
            1: "#f6ede4", 2: "#f3e7db", 3: "#f7ead0",
            4: "#eadaba", 5: "#d7bd96", 6: "#a07850",
            7: "#825c43", 8: "#604134", 9: "#3a312a", 10: "#292420"
        }
        dots_html = "".join(
            f'<div style="width:32px;height:32px;border-radius:50%;'
            f'background:{c};display:inline-block;margin:0 3px;'
            f'{"box-shadow:0 0 0 3px #c0587e;transform:scale(1.25);" if i == mst else ""}'
            f'border:2px solid rgba(0,0,0,0.08);"></div>'
            for i, c in mst_colors.items()
        )
        st.markdown(f"""
        <div class="result-card">
            <div style="display:flex;justify-content:space-between;
                align-items:flex-start;margin-bottom:12px;">
                <div>
                    <div style="font-weight:700;font-size:15px;
                        color:#1a1a1a;">Monk Skin Tone Scale</div>
                    <div style="font-size:12px;color:#bbb;margin-top:4px;">
                        10-point scale from lightest (1) to deepest (10)
                    </div>
                </div>
                <div style="background:#fff0f5;color:#c0587e;
                    border-radius:999px;padding:4px 12px;
                    font-size:12px;font-weight:700;
                    white-space:nowrap;border:1px solid #f9d0de;">
                    MST {mst}
                </div>
            </div>
            <div style="display:flex;flex-wrap:wrap;
                align-items:center;gap:2px;margin:12px 0 6px;">
                {dots_html}
            </div>
            <div style="display:flex;justify-content:space-between;">
                <span style="font-size:11px;color:#bbb;">Lightest</span>
                <span style="font-size:11px;color:#bbb;">Deepest</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Confidence card
        bar_color = (
            "#6aab5a" if conf >= 70
            else "#e0a030" if conf >= 45
            else "#cc4444"
        )
        conf_label = (
            "High confidence — face detection and skin extraction were successful."
            if conf >= 70 else
            "Moderate confidence — try better lighting for improved accuracy."
        )
        st.markdown(f"""
        <div class="result-card">
            <div style="display:flex;justify-content:space-between;
                align-items:center;margin-bottom:8px;">
                <div style="font-weight:700;font-size:15px;
                    color:#1a1a1a;">Detection Confidence</div>
                <div style="font-size:18px;font-weight:800;
                    color:{bar_color};">{conf}%</div>
            </div>
            <div class="conf-bar-wrap">
                <div style="height:100%;border-radius:999px;
                    width:{conf}%;background:{bar_color};"></div>
            </div>
            <div style="font-size:12px;color:#999;
                margin-top:6px;">{conf_label}</div>
        </div>
        """, unsafe_allow_html=True)

        # How we analyzed
        st.markdown("""
        <div style="background:#eef4e8;border-radius:14px;
            padding:18px;border:1px solid #c8ddb0;
            margin-bottom:16px;">
            <div style="font-weight:700;font-size:14px;
                color:#4a7040;margin-bottom:8px;">
                ℹ️ How we analyzed this
            </div>
            <div style="font-size:12px;color:#555;line-height:1.7;">
                Your photo was processed using MediaPipe face detection,
                skin pixel extraction via facial landmarks, and K-Means
                clustering (k=3) to identify the dominant skin color.
                The result was then converted from RGB to CIE LAB color
                space for perceptual matching.
            </div>
        </div>
        """, unsafe_allow_html=True)

        # LAB values
        st.markdown(f"""
        <div>
            <div style="font-weight:700;font-size:14px;
                color:#1a1a1a;margin-bottom:10px;">CIELAB Values</div>
            <div class="lab-grid">
                <div class="lab-cell">
                    <div class="lab-cell-label">L* (Lightness)</div>
                    <div class="lab-cell-val">{lab['L']}</div>
                </div>
                <div class="lab-cell">
                    <div class="lab-cell-label">a* (Red-Green)</div>
                    <div class="lab-cell-val">{lab['a']}</div>
                </div>
                <div class="lab-cell">
                    <div class="lab-cell-label">b* (Yellow-Blue)</div>
                    <div class="lab-cell-val">{lab['b']}</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    _, cta_col, _ = st.columns([1, 2, 1])
    with cta_col:
        if st.button("✨  View Foundation Recommendations  →",
                     use_container_width=True, type="primary",
                     key="go_foundation"):
            st.session_state["nav_target"] = "foundation"
            st.rerun()
