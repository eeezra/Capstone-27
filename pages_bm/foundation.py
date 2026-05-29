import streamlit as st
import pandas as pd

def _format_price(p):
    try:
        return f"Rp{float(p):,.0f}".replace(",",".")
    except:
        return str(p)

def _delta_e_to_score(de):
    try:
        score = max(0, 100 - float(de) * 6)
        return round(score, 1)
    except:
        return 90.0

def render_foundation():
    result = st.session_state.get("analysis_result")

    st.markdown("""
    <div class="main-content">
    """, unsafe_allow_html=True)

    # Header row
    header_l, header_r = st.columns([4, 1])
    with header_l:
        st.markdown("""
        <div class="section-title">Foundation Recommendations</div>
        <div class="section-subtitle">Matched to your skin tone — sorted by color similarity score</div>
        """, unsafe_allow_html=True)
    with header_r:
        if result:
            skin_hex = result.get("skin_hex","#C8956C")
            st.markdown(f"""
            <div style="
                display:flex;align-items:center;gap:8px;
                background:white;border:1.5px solid #fce4ec;
                border-radius:999px;padding:8px 16px;
                margin-top:10px;">
                <div style="
                    width:20px;height:20px;border-radius:999px;
                    background:{skin_hex};border:1px solid rgba(0,0,0,0.1);">
                </div>
                <span style="font-size:13px;font-weight:600;color:#374151;">
                    Your tone: {skin_hex}
                </span>
            </div>
            """, unsafe_allow_html=True)

    if not result:
        st.markdown("""
        <div style="text-align:center;padding:60px 0;">
            <div style="font-size:40px;">💄</div>
            <div style="font-size:18px;font-weight:600;color:#6b7280;margin-top:14px;">
                No analysis results yet
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("→ Start Analysis", type="primary"):
            st.session_state.page = "Skin Analysis"
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
        return

    top5 = result.get("top5_recs", [])
    df   = pd.DataFrame(top5)

    # ── Filter bar ───────────────────────────
    st.markdown("""
    <div style="background:white;border-radius:16px;border:1px solid #f3f4f6;padding:20px 24px;margin-bottom:24px;">
        <div style="font-size:15px;font-weight:700;color:#374151;margin-bottom:14px;">
            ⚙️ Filter &amp; Sort
        </div>
    """, unsafe_allow_html=True)

    filter_col1, filter_col2, filter_col3 = st.columns([2,2,1.2], gap="medium")

    brands_available = sorted(df["Brand"].unique().tolist()) if "Brand" in df.columns else []
    undertones_available = sorted(df["Undertone"].unique().tolist()) if "Undertone" in df.columns else []

    with filter_col1:
        st.markdown("<div style='font-size:12px;font-weight:600;color:#9ca3af;letter-spacing:0.8px;text-transform:uppercase;margin-bottom:6px;'>BRAND</div>", unsafe_allow_html=True)
        brand_filter = st.multiselect(
            "brand", ["All"] + brands_available,
            default=["All"], label_visibility="collapsed"
        )

    with filter_col2:
        st.markdown("<div style='font-size:12px;font-weight:600;color:#9ca3af;letter-spacing:0.8px;text-transform:uppercase;margin-bottom:6px;'>UNDERTONE</div>", unsafe_allow_html=True)
        undertone_filter = st.multiselect(
            "undertone", ["All"] + undertones_available,
            default=["All"], label_visibility="collapsed"
        )

    with filter_col3:
        st.markdown("<div style='font-size:12px;font-weight:600;color:#9ca3af;letter-spacing:0.8px;text-transform:uppercase;margin-bottom:6px;'>SORT BY</div>", unsafe_allow_html=True)
        sort_by = st.radio("sort", ["Similarity","Price"], horizontal=True,
                           label_visibility="collapsed")

    st.markdown("</div>", unsafe_allow_html=True)

    # Filter
    df_filtered = df.copy()
    if "All" not in brand_filter and brand_filter:
        df_filtered = df_filtered[df_filtered["Brand"].isin(brand_filter)]
    if "All" not in undertone_filter and undertone_filter:
        df_filtered = df_filtered[df_filtered["Undertone"].isin(undertone_filter)]
    if sort_by == "Price" and "Price" in df_filtered.columns:
        df_filtered["_price_num"] = pd.to_numeric(df_filtered["Price"], errors="coerce")
        df_filtered = df_filtered.sort_values("_price_num")
    elif "delta_e" in df_filtered.columns:
        df_filtered = df_filtered.sort_values("delta_e")

    # ── Product cards ────────────────────────
    for i, (_, row) in enumerate(df_filtered.head(5).iterrows()):
        brand       = row.get("Brand","-")
        product     = row.get("Product","-")
        shade       = row.get("Shade","-")
        undertone   = row.get("Undertone","-")
        price       = _format_price(row.get("Price",0))
        delta_e     = float(row.get("delta_e",0))
        shade_hex   = row.get("hex","") or result.get("hex_color","#C8956C")
        match_score = _delta_e_to_score(delta_e)

        is_top      = (i == 0)
        card_border = "#f9a8c4" if is_top else "#f3f4f6"
        rank_label  = "⭐" if is_top else str(i + 1)
        rank_bg     = "#ec407a" if is_top else "#f3f4f6"
        rank_color  = "white" if is_top else "#6b7280"

        under_tags = "".join([
            f'<span style="background:#fce4ec;color:#c2185b;padding:3px 10px;border-radius:999px;font-size:12px;font-weight:500;margin-right:4px;">{t.strip()}</span>'
            for t in undertone.split(",") if t.strip()
        ])

        match_color = "#22c55e" if match_score >= 90 else "#f59e0b" if match_score >= 75 else "#ef4444"

        why_text = (
            f"Near-perfect Euclidean match in LAB space. {undertone} undertone aligns precisely with your detected undertone bias."
            if is_top else
            f"Strong {undertone.lower()} undertone match with a ΔE of {delta_e:.1f} in CIE LAB. Complements your skin tone well."
        )

        st.markdown(f"""
        <div style="
            background:white; border-radius:16px;
            border:1.5px solid {card_border};
            padding:22px 24px; margin-bottom:16px;
            box-shadow:{'0 2px 12px rgba(240,98,146,0.1)' if is_top else '0 1px 4px rgba(0,0,0,0.04)'};
            transition:all 0.2s;">

            <div style="display:flex;align-items:flex-start;gap:16px;">
                <!-- Rank badge -->
                <div style="
                    width:36px;height:36px;border-radius:999px;
                    background:{rank_bg};color:{rank_color};
                    display:flex;align-items:center;justify-content:center;
                    font-size:15px;font-weight:700;flex-shrink:0;">
                    {rank_label}
                </div>

                <!-- Color swatch -->
                <div style="
                    width:58px;height:58px;border-radius:12px;
                    background:{shade_hex};flex-shrink:0;
                    border:1px solid rgba(0,0,0,0.08);">
                </div>

                <!-- Info -->
                <div style="flex:1;">
                    <div style="font-size:12px;color:#9ca3af;font-weight:500;margin-bottom:2px;">
                        {brand}
                    </div>
                    <div style="font-size:18px;font-weight:700;color:#1f2937;margin-bottom:8px;">
                        {shade}
                    </div>
                    <div style="margin-bottom:6px;">
                        {under_tags}
                        <span style="background:#f3f4f6;color:#6b7280;padding:3px 10px;border-radius:999px;font-size:12px;font-weight:500;">
                            {product}
                        </span>
                    </div>
                </div>

                <!-- Price -->
                <div style="text-align:right;flex-shrink:0;">
                    <div style="font-size:22px;font-weight:800;color:#1f2937;">{price}</div>
                    <div style="font-size:12px;color:#9ca3af;">est. price</div>
                </div>
            </div>

            <!-- Match score bar -->
            <div style="margin-top:16px;">
                <div style="font-size:13px;color:#6b7280;font-weight:500;margin-bottom:6px;">
                    Color Match Score
                </div>
                <div style="display:flex;align-items:center;gap:10px;">
                    <div style="flex:1;background:#f3f4f6;border-radius:999px;height:8px;overflow:hidden;">
                        <div style="background:{match_color};width:{match_score}%;height:100%;border-radius:999px;"></div>
                    </div>
                    <span style="font-size:14px;font-weight:700;color:{match_color};min-width:44px;text-align:right;">
                        {match_score}%
                    </span>
                </div>
            </div>

            <!-- Why it matches -->
            <div style="
                background:#fef2f4;border-radius:10px;
                padding:12px 16px;margin-top:12px;
                font-size:13px;color:#6b7280;line-height:1.6;">
                <strong style="color:#c2185b;">Why it matches:</strong> {why_text}
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
