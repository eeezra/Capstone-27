import streamlit as st


def render():

    st.markdown("""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Playfair+Display:wght@700;800&display=swap');

    .hero-pill {
        display: inline-flex;
        align-items: center;
        gap: .4rem;
        padding: .45rem 1.1rem;
        border-radius: 999px;
        background: rgba(249,209,217,.55);
        color: #D94E91;
        border: 1px solid rgba(255,168,214,.70);
        font-weight: 800;
        font-size: .80rem;
        letter-spacing: .04em;
        margin-bottom: 1.4rem;
    }

    .hero-title {
        font-family: 'Playfair Display', serif !important;
        font-size: clamp(3rem, 5vw, 4.8rem);
        font-weight: 800;
        line-height: 1.05;
        letter-spacing: -.03em;
        color: #2F2330;
        margin: 0 0 1rem;
        text-align: center;
    }

    .hero-title .pink {
        color: #D94E91;
    }

    .hero-title .olive {
        color: #838F58;
    }

    .hero-sub {
        font-size: 1rem;
        color: #7B6472;
        line-height: 1.8;
        max-width: 500px;
        margin: 0 auto 2rem auto;
        text-align: center;
    }

    .feat-card {
        background: rgba(255,255,255,.75);
        border: 1px solid rgba(248,168,214,.35);
        border-radius: 1.3rem;
        padding: 1.8rem 1.6rem;
        min-height: 230px;
        box-shadow: 0 14px 30px rgba(200,107,133,.08);
        backdrop-filter: blur(12px);
    }

    .feat-icon-wrap {
        width: 48px;
        height: 48px;
        border-radius: 1rem;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.35rem;
        margin-bottom: 1rem;
    }

    .feat-title {
        font-weight: 700;
        font-size: 1rem;
        color: #2F2330;
        margin-bottom: .45rem;
    }

    .feat-desc {
        font-size: .88rem;
        color: #7B6472;
        line-height: 1.68;
    }

    .stats-bar {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        background: linear-gradient(
            90deg,
            rgba(255,240,245,.90),
            rgba(212,235,194,.70)
        );
        border-radius: 1.3rem;
        overflow: hidden;
        margin-top: 2rem;
        border: 1px solid rgba(248,168,214,.28);
        box-shadow: 0 8px 24px rgba(200,107,133,.07);
    }

    .stat-cell {
        padding: 1.5rem 1rem;
        text-align: center;
        border-right: 1px solid rgba(248,168,214,.22);
    }

    .stat-cell:last-child {
        border-right: none;
    }

    .stat-num {
        font-family: 'Playfair Display', serif;
        font-size: 1.9rem;
        font-weight: 800;
        color: #2F2330;
        line-height: 1;
    }

    .stat-lbl {
        font-size: .80rem;
        color: #7B6472;
        margin-top: .35rem;
        font-weight: 500;
    }

    </style>
    """, unsafe_allow_html=True)

    # HERO

    st.markdown("""
    <div style="text-align:center; padding: 2rem 1rem 1.4rem;">

        <div class="hero-pill">
            ✦ AI-Powered Foundation Matching ✦
        </div>

        <h1 class="hero-title">
            Find Your Perfect
            <span class="pink">Foundation</span><br>
            <span class="olive">Match</span>
        </h1>

        <p class="hero-sub">
            Analyze your skin tone and undertone to discover foundation
            shades that suit you — powered by computer vision and color science.
        </p>

    </div>
    """, unsafe_allow_html=True)

    # CTA BUTTONS

    _, col_start, col_how, _ = st.columns([1.8, 1, 1, 1.8])

    with col_start:

        if st.button(
            "▶  Start Analysis",
            type="primary",
            use_container_width=True,
            key="hero_start",
        ):
            st.session_state["nav_target"] = "skin"
            st.rerun()

    with col_how:

        if st.button(
            "How It Works",
            use_container_width=True,
            key="hero_how",
        ):
            st.session_state["nav_target"] = "about"
            st.rerun()

    st.markdown(
        "<div style='height:1.6rem;'></div>",
        unsafe_allow_html=True
    )

    # FEATURE CARDS

    fc1, fc2, fc3 = st.columns(3, gap="medium")

    cards = [
        (
            "#FFF0F5",
            "rgba(255,168,214,.32)",
            "📷",
            "Upload Photo",
            "Use your own photo or capture one live with your webcam. "
            "We analyze your skin directly.",
        ),

        (
            "#EEF4E8",
            "rgba(186,223,147,.42)",
            "📊",
            "Skin Tone Analysis",
            "Get your skin tone, undertone classification, and Monk Skin "
            "Tone scale score instantly.",
        ),

        (
            "#FFF0F5",
            "rgba(255,168,214,.28)",
            "✨",
            "Foundation Recommendation",
            "Matched foundations are ranked by Euclidean color distance "
            "for the most accurate shade.",
        ),
    ]

    for col, (bg, icon_bg, icon, title, desc) in zip(
        [fc1, fc2, fc3],
        cards
    ):

        with col:

            st.markdown(f"""
            <div class="feat-card" style="background:{bg};">

                <div class="feat-icon-wrap"
                     style="background:{icon_bg};">
                    {icon}
                </div>

                <div class="feat-title">
                    {title}
                </div>

                <div class="feat-desc">
                    {desc}
                </div>

            </div>
            """, unsafe_allow_html=True)

    # STATS BAR

    st.markdown("""
    <div class="stats-bar">

        <div class="stat-cell">
            <div class="stat-num">50+</div>
            <div class="stat-lbl">Foundation Shades</div>
        </div>

        <div class="stat-cell">
            <div class="stat-num">10</div>
            <div class="stat-lbl">Brands Covered</div>
        </div>

        <div class="stat-cell">
            <div class="stat-num">99%</div>
            <div class="stat-lbl">Detection Accuracy</div>
        </div>

        <div class="stat-cell">
            <div class="stat-num">&lt; 2s</div>
            <div class="stat-lbl">Analysis Time</div>
        </div>

    </div>
    """, unsafe_allow_html=True)
