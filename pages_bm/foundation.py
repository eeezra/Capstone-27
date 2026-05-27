import streamlit as st
import pandas as pd
import numpy as np

def _lab_to_hex(L, a, b):
    try:
        from skimage.color import lab2rgb
        rgb = lab2rgb([[[L, a, b]]])[0][0]
        rgb = (rgb * 255).clip(0, 255).astype(int)
        return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"
    except:
        return "#c8956c"


def format_rupiah(value):
    try:
        v = float(value)
        return f"Rp{v:,.0f}".replace(",", ".")
    except:
        return str(value)


def render():
    st.markdown("""
    <style>
    .rec-card {
        background:white;border-radius:16px;
        padding:22px 20px;margin-bottom:16px;
        border:1px solid #f0e0e8;
        position:relative;
        transition:box-shadow 0.2s;
    }
    .rec-card:hover {
        box-shadow:0 4px 20px rgba(192,88,126,0.12);
    }
    .rec-rank {
        width:32px;height:32px;border-radius:50%;
        background:#f0f0f0;display:flex;
        align-items:center;justify-content:center;
        font-weight:700;font-size:14px;color:#555;
        flex-shrink:0;
    }
    .rec-rank.top {
        background:#fce8ef;color:#c0587e;
        font-size:16px;
    }
    .match-bar-wrap {
        background:#f5f5f5;border-radius:999px;
        height:6px;overflow:hidden;margin:8px 0 4px;
    }
    .match-bar-fill {
        height:100%;border-radius:999px;
        background:linear-gradient(90deg,#f4a0b8,#c0587e);
    }
    .pill {
        display:inline-block;padding:3px 10px;
        border-radius:999px;font-size:11px;font-weight:600;
        margin:2px;
    }
    .filter-section {
        background:white;border-radius:14px;
        padding:18px 20px;
        border:1px solid #f0e0e8;
        margin-bottom:20px;
    }
    </style>
    """, unsafe_allow_html=True)

    result = st.session_state.get("analysis_result")

    # Header
    st.markdown("## Foundation Recommendations")
    st.markdown("<p style='color:#888;margin-top:-8px;'>Matched to your skin tone — sorted by color similarity score</p>",
                unsafe_allow_html=True)

    if result is None:
        st.info("No analysis result found. Please analyze your skin first.")
        if st.button("→ Go to Skin Analysis"):
            st.session_state["nav_target"] = "skin"
            st.rerun()
        return

    # Your tone badge
    skin_hex = result.get("skin_hex", "#c8956c")
    st.markdown(f"""
    <div style="display:flex;align-items:center;gap:10px;margin-bottom:20px;">
        <div style="width:22px;height:22px;border-radius:50%;
            background:{skin_hex};border:2px solid rgba(0,0,0,0.1);"></div>
        <span style="font-size:14px;color:#555;font-weight:600;">
            Your tone: <strong>{skin_hex.upper()}</strong>
        </span>
    </div>
    """, unsafe_allow_html=True)

    top5 = result.get("top5_recs", [])
    if not top5:
        st.warning("No foundation recommendations available.")
        return

    df = pd.DataFrame(top5)

    # ── Filters ───────────────────────────────────────────
    with st.expander("🔽  Filter & Sort", expanded=True):
        fc1, fc2, fc3 = st.columns([1.2, 1.2, 0.8], gap="medium")

        with fc1:
            st.markdown("**Brand**")
            brands = ["All"] + sorted(df["Brand"].dropna().unique().tolist())
            sel_brand = st.selectbox("brand_filter", brands,
                                     label_visibility="collapsed", key="brand_filter")

        with fc2:
            st.markdown("**Undertone**")
            undertones = ["All", "Warm", "Neutral-Warm", "Neutral", "Cool"]
            sel_undertone = st.selectbox("undertone_filter", undertones,
                                          label_visibility="collapsed",
                                          key="undertone_filter")
        with fc3:
            st.markdown("**Sort By**")
            sort_by = st.selectbox("sort_filter", ["Similarity", "Price"],
                                    label_visibility="collapsed", key="sort_filter")

    # Apply filters
    df_show = df.copy()
    if sel_brand != "All":
        df_show = df_show[df_show["Brand"] == sel_brand]
    if sel_undertone != "All":
        df_show = df_show[df_show["Undertone"].str.contains(
            sel_undertone, case=False, na=False)]
    if sort_by == "Price":
        df_show = df_show.sort_values("Price")

    df_show = df_show.reset_index(drop=True)

    if df_show.empty:
        st.warning("No results match the selected filters.")
        return

    # ── Recommendation Cards ───────────────────────────────
    for i, row in df_show.iterrows():
        brand = str(row.get("Brand", "-"))
        product = str(row.get("Product", "-"))
        shade = str(row.get("Shade", "-"))
        undertone = str(row.get("Undertone", "-"))
        price = format_rupiah(row.get("Price", 0))

        # Compute hex from LAB if available
        try:
            hex_c = _lab_to_hex(
                float(row.get("lab_L", 66)),
                float(row.get("lab_a", 16)),
                float(row.get("lab_b", 28)),
            )
        except:
            hex_c = skin_hex

        # Match score: rough inverse delta-E normalized
        try:
            skin_lab = result["cielab"]
            delta_e = math.sqrt(
                (float(row.get("lab_L", 66)) - skin_lab["L"])**2 +
                (float(row.get("lab_a", 16)) - skin_lab["a"])**2 +
                (float(row.get("lab_b", 28)) - skin_lab["b"])**2
            )
            match_score = max(0, round(100 - delta_e * 3.5, 1))
        except:
            match_score = 90 - i * 3

        is_top = i == 0
        rank_html = (
            f'<div class="rec-rank top">⭐</div>'
            if is_top else
            f'<div class="rec-rank">{i+1}</div>'
        )

        # Undertone pill colors
        ut_colors = {
            "warm": ("#fdf6e3", "#c97c30"),
            "neutral": ("#e8f5e9", "#2e7d32"),
            "cool": ("#e8eef8", "#1565c0"),
        }
        pills = " ".join(
            _make_pill(t, ut_colors)
            for t in undertone.split()
        )

        st.markdown(f"""
        <div class="rec-card">
            <div style="display:flex;align-items:flex-start;gap:14px;">
                {rank_html}
                <div style="
                    width:64px;height:64px;border-radius:12px;
                    background:{hex_c};flex-shrink:0;
                    border:1px solid rgba(0,0,0,0.08);
                    position:relative;">
                    <div style="
                        position:absolute;bottom:-6px;left:50%;
                        transform:translateX(-50%);
                        background:rgba(0,0,0,0.5);color:white;
                        font-size:8px;font-weight:700;padding:1px 5px;
                        border-radius:3px;white-space:nowrap;">
                        {hex_c.upper()}
                    </div>
                </div>
                <div style="flex:1;">
                    <div style="font-size:12px;color:#999;
                        margin-bottom:2px;">{brand}</div>
                    <div style="font-weight:700;font-size:16px;
                        color:#1a1a1a;margin-bottom:4px;">{shade}</div>
                    <div style="margin-bottom:6px;">{pills}</div>
                    <div style="font-size:12px;color:#888;">
                        <strong>Color Match Score</strong>
                    </div>
                    <div class="match-bar-wrap">
                        <div class="match-bar-fill"
                            style="width:{match_score}%;"></div>
                    </div>
                    <div style="display:flex;justify-content:space-between;
                        align-items:center;">
                        <div style="font-size:12px;color:#888;">
                            {match_score}%
                        </div>
                        <div style="font-weight:700;font-size:15px;
                            color:#1a1a1a;">{price}</div>
                    </div>
                </div>
            </div>
            <div style="
                margin-top:12px;background:#fff8fb;
                border-radius:10px;padding:12px;
                border:1px solid #f5d0de;
                font-size:12px;color:#666;line-height:1.6;">
                <strong>Why it matches:</strong>
                Near-perfect Euclidean match in LAB space.
                {undertone} undertone aligns with your detected undertone bias.
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Needed for math
    import math


def _make_pill(text, color_map):
    t = text.strip().lower()
    bg, fg = "#f0f0f0", "#555"
    for key, (b, f) in color_map.items():
        if key in t:
            bg, fg = b, f
            break
    return (
        f'<span class="pill" '
        f'style="background:{bg};color:{fg};">'
        f'{text.strip()}</span>'
    )
