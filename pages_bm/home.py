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

    .feat-card{
        border-radius:28px;
        padding:1.3rem 1.2rem;
        min-height:190px;
        border:1px solid rgba(248,168,214,.26);
        box-shadow:0 12px 30px rgba(200,107,133,.07);
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

    </style>
    """, unsafe_allow_html=True)

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
            foundation shades that suit you.
        </div>

    </div>

    """, unsafe_allow_html=True)

    _, c1, c2, _ = st.columns([2.2, .95, .95, 2.2])

    with c1:
        st.button(
            "▶ Start Analysis",
            type="primary",
            use_container_width=True
        )

    with c2:
        st.button(
            "How It Works",
            type="secondary",
            use_container_width=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    a, b, c = st.columns(3)

    cards = [
        (
            "#FFF2F7",
            "📷",
            "Upload Photo",
            "Upload your own image or use webcam capture."
        ),
        (
            "#EEF4E8",
            "📊",
            "Skin Tone Analysis",
            "Analyze undertone and Monk Skin Tone scale."
        ),
        (
            "#FFF2F7",
            "✨",
            "Foundation Recommendation",
            "Get accurate shade recommendations instantly."
        )
    ]

    for col, (bg, icon, title, desc) in zip([a,b,c], cards):

        with col:

            st.markdown(f"""

            <div class="feat-card" style="background:{bg};">

                <div style="font-size:1.8rem;margin-bottom:.8rem">
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
