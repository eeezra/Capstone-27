import streamlit as st
import math

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
        padding:22px 20px;
        border:1px solid #f0e0e8;
        margin-bottom:16px;
    }
    .result-card-label {
        font-size:11px;font-weight:700;
        text-transform:uppercase;letter-spacing:1px;
        color:#999;margin-bottom:6px;
    }
    .result-card-value {
        font-size:22px;font-weight:800;color:#1a1a1a;
    }
    .result-card-sub {
        font-size:12px;color:#aaa;margin-top:4px;
    }
    .mst-dot {
        width:34px;height:34px;border-radius:50%;
        display:inline-block;margin:0 3px;
        border:2px solid transparent;
        transition:transform 0.15s;
    }
    .mst-dot.active {
        border-color:#c0587e;
        transform:scale(1.25);
    }
    .conf-bar-wrap {
        background:#f0f0f0;border-radius:999px;
        height:8px;overflow:hidden;margin:8px 0;
    }
    .conf-bar-fill {
        height:100%;border-radius:999px;
        background:linear-gradient(90deg,#5cb85c,#4cae4c);
    }
    .lab-grid {
        display:grid;grid-template-columns:repeat(3,1fr);gap:12px;
        margin-top:4px;
    }
    .lab-cell {
        background:#fafafa;border-radius:10px;
        padding:12px 14px;border:1px solid #f0e0e8;
    }
    .lab-cell-label { font-size:11px;color:#aaa;margin-bottom:4px; }
    .lab-cell-val { font-size:20px;font-weight:700;color:#222; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("## Analysis Results")
    st.markdown("<p style='color:#888;margin-top:-8px;'>Here's what we found from your skin tone analysis</p>",
                unsafe_allow_html=True)

    result = st.session_state.get("analysis_result")

    if result is None:
        st.info("No analysis result yet. Please go to **Skin Analysis** and analyze a photo first.")
        if st.button("→ Go to Skin Analysis"):
            st.session_state["nav_target"] = "skin"
            st.rerun()
        return

    mst = result["mst_pred"]
    conf = result["confidence"]
    lab = result["cielab"]
    skin_hex = result.get("skin_hex", _lab_to_hex(lab["L"], lab["a"], lab["b"]))
    undertone = result.get("user_undertone", "Warm")
    skintone = result.get("user_skintone", "Medium")

    # ── Top Metric Cards ─────────────────────────────────
    m1, m2, m3, m4 = st.columns(4, gap="medium")

    card_data = [
        ("#fce8ef", "SKIN TONE", skintone, "Classification"),
        ("#fdf6e3", "UNDERTONE", undertone, "Color Bias"),
        ("#e8f5e9", "MST SCORE", f"{mst} / 10", "Monk Scale"),
        ("#ede8f5", "CONFIDENCE", f"{conf}%", "Accuracy"),
    ]

    for col, (bg, label, value, sub) in zip([m1, m2, m3, m4], card_data):
        with col:
            st.markdown(f"""
            <div style="background:{bg};border-radius:14px;
                padding:20px 16px;border:1px solid rgba(0,0,0,0.05);">
                <div class="result-card-label">{label}</div>
                <div class="result-card-value" style="font-size:18px;">{value}</div>
                <div class="result-card-sub">{sub}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Main Content ──────────────────────────────────────
    left_col, right_col = st.columns([1, 1.3], gap="large")

    with left_col:
        # Detected skin color swatch
        st.markdown(f"""
        <div style="
            background:{skin_hex};border-radius:16px;
            height:140px;display:flex;align-items:center;
            justify-content:center;margin-bottom:16px;
            box-shadow:0 4px 20px rgba(0,0,0,0.12);">
            <span style="
                background:rgba(0,0,0,0.25);color:white;
                padding:6px 14px;border-radius:8px;
                font-size:15px;font-weight:700;letter-spacing:1px;">
                {skin_hex.upper()}
            </span>
        </div>
        """, unsafe_allow_html=True)

        # Color details card
        r_hex = skin_hex.lstrip("#")
        r, g, b = tuple(int(r_hex[i:i+2], 16) for i in (0, 2, 4))

        st.markdown(f"""
        <div class="result-card">
            <div style="font-weight:700;font-size:15px;
                margin-bottom:14px;color:#1a1a1a;">
                Detected Skin Color
            </div>
            <table style="width:100%;border-collapse:collapse;">
                <tr>
                    <td style="color:#aaa;font-size:13px;padding:5px 0;">HEX</td>
                    <td style="font-weight:700;font-size:13px;
                        text-align:right;">{skin_hex.upper()}</td>
                </tr>
                <tr>
                    <td style="color:#aaa;font-size:13px;padding:5px 0;">RGB</td>
                    <td style="font-weight:700;font-size:13px;
                        text-align:right;">{r},  {g},  {b}</td>
                </tr>
                <tr>
                    <td style="color:#aaa;font-size:13px;padding:5px 0;">LAB</td>
                    <td style="font-weight:700;font-size:13px;
                        text-align:right;">
                        {lab['L']},  {lab['a']},  {lab['b']}
                    </td>
                </tr>
            </table>
        </div>
        """, unsafe_allow_html=True)

        # Undertone card
        warm_swatches = ["#c8956c", "#b87d55", "#a06840"]
        cool_swatches = ["#c0a0b0", "#a08898", "#907080"]
        neutral_swatches = ["#c4a882", "#b09070", "#9c7e5e"]
        swatch_map = {"Warm": warm_swatches, "Cool": cool_swatches}
        swatches = swatch_map.get(undertone, neutral_swatches)

        undertone_desc = {
            "Warm": "Warm undertones have golden, peachy, or yellow hues. They suit foundations with yellow or golden bases.",
            "Cool": "Cool undertones have pink, red, or bluish hues. They suit foundations with pink or rosy bases.",
            "Neutral": "Neutral undertones are a mix of warm and cool. Most foundation shades will work well.",
        }.get(undertone, "")

        swatches_html = "".join(
            f'<div style="width:32px;height:32px;border-radius:50%;'
            f'background:{s};display:inline-block;margin-right:6px;'
            f'border:2px solid rgba(0,0,0,0.1);"></div>'
            for s in swatches
        )

        bg_col = {"Warm": "#fdf6e3", "Cool": "#e8eef8", "Neutral": "#f0f4ec"}.get(undertone, "#fafafa")

        st.markdown(f"""
        <div style="background:{bg_col};border-radius:14px;
            padding:18px;border:1px solid rgba(0,0,0,0.05);">
            <div style="font-weight:700;font-size:15px;
                margin-bottom:8px;">Undertone: {undertone}</div>
            <div style="font-size:13px;color:#666;
                margin-bottom:12px;">{undertone_desc}</div>
            {swatches_html}
        </div>
        """, unsafe_allow_html=True)

    with right_col:
        # MST Scale
        mst_colors = {
            1: "#f6ede4", 2: "#f3e7db", 3: "#f7ead0", 4: "#eadaba",
            5: "#d7bd96", 6: "#a07850", 7: "#825c43", 8: "#604134",
            9: "#3a312a", 10: "#292420"
        }

        dots_html = "".join(
            f'<div class="mst-dot{"  active" if i == mst else ""}" '
            f'style="background:{c};'
            f'{"box-shadow:0 0 0 3px #c0587e;" if i == mst else ""}"></div>'
            for i, c in mst_colors.items()
        )

        st.markdown(f"""
        <div class="result-card" style="margin-bottom:16px;">
            <div style="display:flex;justify-content:space-between;
                align-items:flex-start;margin-bottom:10px;">
                <div>
                    <div style="font-weight:700;font-size:15px;">Monk Skin Tone Scale</div>
                    <div style="font-size:12px;color:#aaa;margin-top:3px;">
                        The Monk Skin Tone scale provides a 10-point measure of skin color diversity,
                        from lightest (1) to deepest (10).
                    </div>
                </div>
                <div style="
                    background:#fce8ef;color:#c0587e;
                    border-radius:999px;padding:4px 12px;
                    font-size:12px;font-weight:700;white-space:nowrap;">
                    MST {mst}
                </div>
            </div>
            <div style="display:flex;align-items:center;
                gap:2px;margin:14px 0 6px;">
                {dots_html}
            </div>
            <div style="display:flex;justify-content:space-between;">
                <span style="font-size:11px;color:#aaa;">Lightest</span>
                <span style="font-size:11px;color:#aaa;">Deepest</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Confidence card
        bar_color = (
            "#5cb85c" if conf >= 70
            else "#e07b39" if conf >= 45
            else "#cc2222"
        )
        conf_label = (
            "High confidence — face detection and skin area extraction were successful with minimal noise."
            if conf >= 70
            else "Moderate confidence — results may vary with better lighting."
        )

        st.markdown(f"""
        <div class="result-card" style="margin-bottom:16px;">
            <div style="display:flex;justify-content:space-between;
                align-items:center;margin-bottom:8px;">
                <div style="font-weight:700;font-size:15px;">Detection Confidence</div>
                <div style="font-size:18px;font-weight:800;color:{bar_color};">{conf}%</div>
            </div>
            <div class="conf-bar-wrap">
                <div class="conf-bar-fill"
                    style="width:{conf}%;background:{bar_color};"></div>
            </div>
            <div style="font-size:12px;color:#888;margin-top:6px;">{conf_label}</div>
        </div>
        """, unsafe_allow_html=True)

        # How we analyzed
        st.markdown("""
        <div style="background:#e8f5e9;border-radius:14px;
            padding:18px;border:1px solid #c8e6c9;">
            <div style="font-weight:700;font-size:14px;
                margin-bottom:8px;">ℹ️ How we analyzed this</div>
            <div style="font-size:12px;color:#555;line-height:1.7;">
                Your photo was processed using MediaPipe face detection, skin pixel
                extraction via facial landmarks, and K-Means clustering (k=3) to
                identify the dominant skin color. The result was then converted from
                RGB to CIE LAB color space for perceptual matching.
            </div>
        </div>
        """, unsafe_allow_html=True)

        # LAB values
        st.markdown(f"""
        <div style="margin-top:16px;">
            <div style="font-weight:700;font-size:14px;
                margin-bottom:10px;">CIELAB Values</div>
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

    # ── View Recommendations CTA ──────────────────────────
    _, cta_col, _ = st.columns([1, 2, 1])
    with cta_col:
        if st.button("✨  View Foundation Recommendations  →",
                     use_container_width=True, type="primary",
                     key="go_foundation"):
            st.session_state["nav_target"] = "foundation"
            st.rerun()
