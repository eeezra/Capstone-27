import streamlit as st


def render():

    st.markdown("""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;800&display=swap');

    .hero-wrap{
        text-align:center;
        padding-top:1.4rem;
    }

    .hero-pill{
        display:inline-flex;
        align-items:center;
        gap:.45rem;

        padding:.45rem 1.15rem;

        border-radius:999px;

        background:rgba(249,209,217,.45);

        border:1px solid rgba(255,168,214,.60);

        color:#D94E91;

        font-size:.78rem;
        font-weight:800;

        letter-spacing:.04em;

        margin-bottom:1.6rem;
    }

    .hero-title{
        font-family:'Playfair Display', serif !important;

        font-size:clamp(3rem, 5vw, 5rem);

        font-weight:800;

        line-height:1.03;

        letter-spacing:-.04em;

        color:#2F2330;

        max-width:760px;

        margin:auto auto 1.1rem auto;
    }

    .hero-title .pink{
        color:#D94E91;
    }

    .hero-title .olive{
        color:#838F58;
    }

    .hero-sub{
        max-width:430px;

        margin:auto auto 2rem auto;

        font-size:1rem;

        line-height:1.9;

        color:#7B6472;
    }

    /* FEATURE CARDS */

    .cards-wrap{
        max-width:900px;
        margin:auto;
    }

    .feat-card{
        border-radius:28px;

        padding:1.3rem 1.2rem;

        min-height:190px;

        border:1px solid rgba(248,168,214,.26);

        box-shadow:0 12px 30px rgba(200,107,133,.07);

        backdrop-filter:blur(10px);
    }

    .feat-icon{
        width:42px;
        height:42px;

        border-radius:14px;

        display:flex;
        align-items:center;
        justify-content:center;

        font-size:1rem;

        margin-bottom:1rem;
    }

    .feat-title{
        font-size:1rem;
        font-weight:800;

        color:#2F2330;

        margin-bottom:.5rem;
    }

    .feat-desc{
        font-size:.88rem;

        line-height:1.8;

        color:#7B6472;
    }

    /* STATS BAR */

    .stats-bar{
        display:grid;

        grid-template-columns:repeat(4,1fr);

        max-width:760px;

        margin:2rem auto 0 auto;

        border-radius:20px;

        overflow:hidden;

        background:linear-gradient(
            90deg,
            rgba(255,240,245,.92),
            rgba(212,235,194,.72)
        );

        border:1px solid rgba(248,168,214,.18);

        box-shadow:0 10px 24px rgba(200,107,133,.06);
    }

    .stat-cell{
        padding:1.3rem .7rem;

        text-align:center;

        border-right:1px solid rgba(248,168,214,.15);
    }

    .stat-cell:last-child{
        border-right:none;
    }

    .stat-num{
        font-family:'Playfair Display', serif !important;

        font-size:2rem;

        font-weight:800;

        line-height:1;

        color:#2F2330;
    }

    .stat-lbl{
        margin-top:.35rem;

        font-size:.78rem;

        color:#7B6472;

        font-weight:500;
    }

    </style>
    """, unsafe_allow_html=True)

    # ======================================================
    # HERO
    # ======================================================

    st.markdown("""
    <div class="hero-wrap">

        <div class="hero-pill">
            ✦ AI-Powered Foundation Matching ✦
        </div>

        <div class="hero-title">
            Find Your Perfect
            <span class="pink">Foundation</span><br>
            <span class="olive">Match</span>
        </div>

        <div class="hero-sub">
            Analyze your skin tone and undertone to discover
            foundation shades that suit you — powered by
            computer vision and color science.
        </div>

    </div>
    """, unsafe_allow_html=True)

    # ======================================================
    # BUTTONS
    # ======================================================

    _, col1, col2, _ = st.columns([2.2, .95, .95, 2.2])

    with col1:
        if st.button(
            "▶ Start Analysis",
            type="primary",
            use_container_width=True,
            key="hero_start"
        ):
            st.session_state.page = "skin"
            st.rerun()

    with col2:
        if st.button(
            "How It Works",
            use_container_width=True,
            key="hero_about"
        ):
            st.session_state.page = "about"
            st.rerun()

    st.markdown(
        "<div style='height:1.8rem'></div>",
        unsafe_allow_html=True
    )

    # ======================================================
    # FEATURE CARDS
    # ======================================================

    c1, c2, c3 = st.columns(3, gap="medium")

    cards = [

        (
            "#FFF2F7",
            "rgba(255,168,214,.28)",
            "📷",
            "Upload Photo",
            "Use your own photo or capture one live with your webcam. We analyze your skin directly."
        ),

        (
            "#EEF4E8",
            "rgba(186,223,147,.42)",
            "📊",
            "Skin Tone Analysis",
            "Get your skin tone, undertone classification, and Monk Skin Tone scale score instantly."
        ),

        (
            "#FFF2F7",
            "rgba(255,168,214,.22)",
            "✨",
            "Foundation Recommendation",
            "Matched foundations are ranked by Euclidean color distance for the most accurate shade."
        ),
    ]

    for col, (bg, icon_bg, icon, title, desc) in zip([c1, c2, c3], cards):

        with col:

            st.markdown(f"""
            <div class="feat-card" style="background:{bg};">

                <div class="feat-icon"
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

    # ======================================================
    # STATS
    # ======================================================

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
