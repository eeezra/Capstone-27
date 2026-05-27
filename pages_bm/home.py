import streamlit as st

def render():
    # ── Hero ──────────────────────────────────────────────
    st.markdown("""
    <style>
    .hero-wrap {
        text-align:center;
        padding: 48px 20px 36px;
        position: relative;
    }
    .hero-badge {
        display:inline-flex;align-items:center;gap:6px;
        background:#fde8ef;color:#c0587e;
        border-radius:999px;padding:6px 16px;
        font-size:13px;font-weight:600;
        margin-bottom:20px;
        border:1px solid #f5c2d0;
    }
    .hero-title {
        font-size:clamp(32px,5vw,52px);
        font-weight:800;
        line-height:1.15;
        color:#1a1a1a;
        margin-bottom:16px;
    }
    .hero-title span { color:#c0587e; }
    .hero-sub {
        font-size:16px;color:#666;
        max-width:520px;margin:0 auto 32px;
        line-height:1.7;
    }
    .stat-grid {
        display:grid;
        grid-template-columns:repeat(4,1fr);
        gap:0;
        background:linear-gradient(90deg,#fce8ef,#e8f5e9);
        border-radius:20px;
        overflow:hidden;
        margin-top:40px;
    }
    .stat-cell {
        padding:24px 16px;
        text-align:center;
        border-right:1px solid rgba(255,255,255,0.5);
    }
    .stat-cell:last-child { border-right:none; }
    .stat-val {
        font-size:28px;font-weight:800;color:#2d2d2d;
    }
    .stat-label {
        font-size:12px;color:#888;margin-top:4px;
    }
    </style>

    <div class="hero-wrap">
        <div class="hero-badge">✨ AI-Powered Foundation Matching</div>
        <h1 class="hero-title">
            Find Your Perfect<br>
            <span>Foundation Match</span>
        </h1>
        <p class="hero-sub">
            Analyze your skin tone and undertone to discover foundation
            shades that suit you — powered by computer vision and color science.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ── CTA Buttons ──────────────────────────────────────
    c1, c2, c3 = st.columns([2, 1.2, 1.2, 2], gap="small")[:3]  # type: ignore
    cola, colb, _, colc = st.columns([1.5, 1.2, 0.6, 1.5])
    with colb:
        if st.button("▶  Start Analysis", use_container_width=True,
                     type="primary", key="hero_start"):
            st.session_state["nav_target"] = "skin"
            st.rerun()
    with colc:
        if st.button("How It Works", use_container_width=True,
                     key="hero_how"):
            st.session_state["nav_target"] = "about"
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Feature Cards ────────────────────────────────────
    fc1, fc2, fc3 = st.columns(3, gap="medium")

    cards = [
        ("#fce8ef", "📷", "Upload Photo",
         "Use your own photo or capture one live with your webcam. We analyze your skin directly."),
        ("#e8f5e9", "📊", "Skin Tone Analysis",
         "Get your skin tone, undertone classification, and Monk Skin Tone scale score instantly."),
        ("#fce8ef", "✨", "Foundation Recommendation",
         "Matched foundations are ranked by Euclidean color distance for the most accurate shade."),
    ]

    for col, (bg, icon, title, desc) in zip([fc1, fc2, fc3], cards):
        with col:
            st.markdown(f"""
            <div style="
                background:{bg};border-radius:16px;
                padding:28px 22px;height:100%;
                border:1px solid rgba(0,0,0,0.05);">
                <div style="
                    width:44px;height:44px;border-radius:12px;
                    background:white;display:flex;align-items:center;
                    justify-content:center;font-size:20px;
                    margin-bottom:14px;
                    box-shadow:0 2px 8px rgba(0,0,0,0.08);">
                    {icon}
                </div>
                <div style="font-weight:700;font-size:16px;
                    color:#1a1a1a;margin-bottom:8px;">{title}</div>
                <div style="font-size:13px;color:#666;line-height:1.6;">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    # ── Stats ────────────────────────────────────────────
    st.markdown("""
    <div class="stat-grid">
        <div class="stat-cell">
            <div class="stat-val">50+</div>
            <div class="stat-label">Foundation Shades</div>
        </div>
        <div class="stat-cell">
            <div class="stat-val">10</div>
            <div class="stat-label">Brands Covered</div>
        </div>
        <div class="stat-cell">
            <div class="stat-val">99%</div>
            <div class="stat-label">Detection Accuracy</div>
        </div>
        <div class="stat-cell">
            <div class="stat-val">&lt; 2s</div>
            <div class="stat-label">Analysis Time</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
