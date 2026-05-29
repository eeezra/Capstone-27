import streamlit as st

def render_home():

    st.markdown("""
    <style>

    .hero{
        text-align:center;
        padding-top:1.4rem;
    }

    .hero-badge{
        display:inline-flex;
        align-items:center;
        gap:.4rem;

        padding:.45rem 1rem;

        border-radius:999px;

        background:rgba(249,209,217,.62);

        border:1px solid rgba(255,168,214,.75);

        color:#D94E91;

        font-size:.75rem;
        font-weight:800;
    }

    .hero-title{

        font-family:'Playfair Display',serif;

        font-size:4.7rem;

        font-weight:800;

        line-height:1.03;

        letter-spacing:-.03em;

        margin-top:1.3rem;
        margin-bottom:.8rem;
    }

    .pink{
        color:#EB80B6;
    }

    .green{
        color:#838F58;
    }

    .hero-subtitle{

        max-width:560px;

        margin:auto;

        color:#7B6472;

        font-size:1rem;

        line-height:1.8;
    }

    .feature-card{

        background:rgba(255,255,255,.65);

        border-radius:1.3rem;

        border:1px solid rgba(255,168,214,.35);

        backdrop-filter:blur(14px);

        padding:1.7rem;

        min-height:190px;

        box-shadow:
        0 16px 36px rgba(200,107,133,.09);
    }

    .feature-icon{

        width:48px;
        height:48px;

        border-radius:14px;

        display:flex;
        align-items:center;
        justify-content:center;

        font-size:1.3rem;

        margin-bottom:1rem;
    }

    .feature-title{

        font-size:1.05rem;
        font-weight:800;

        margin-bottom:.5rem;

        color:#2F2330;
    }

    .feature-desc{

        color:#7B6472;

        font-size:.88rem;

        line-height:1.7;
    }

    .stats-card{

        background:
        linear-gradient(
            90deg,
            rgba(249,209,217,.55),
            rgba(212,235,194,.72)
        );

        border-radius:1.25rem;

        padding:1.2rem;

        border:1px solid rgba(255,168,214,.25);

        margin-top:2rem;
    }

    .stat-number{

        font-size:1.9rem;

        font-weight:900;

        color:#2F2330;
    }

    .stat-label{

        font-size:.82rem;

        color:#7B6472;
    }

    </style>
    """, unsafe_allow_html=True)

    # ====================================================
    # HERO
    # =====================================================

    st.markdown(
        """
        <p style="
            text-align:center;
            margin-bottom:10px;
        ">
            <span style="
                background:rgba(249,209,217,.62);
                border:1px solid rgba(255,168,214,.75);
                color:#D94E91;
                padding:8px 16px;
                border-radius:999px;
                font-size:12px;
                font-weight:800;
            ">
                ✦ AI-Powered Foundation Matching ✦
            </span>
        </p>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown(
        """
        <h1 style="
            text-align:center;
            font-family:'Playfair Display',serif;
            font-size:72px;
            line-height:1.05;
            margin-bottom:16px;
            color:#2F2330;
        ">
            Find Your Perfect<br>
            <span style="color:#EB80B6;">Foundation</span><br>
            <span style="color:#838F58;">Match</span>
        </h1>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown(
        """
        <p style="
            text-align:center;
            max-width:600px;
            margin:auto;
            color:#7B6472;
            line-height:1.8;
        ">
            Analyze your skin tone and undertone to discover foundation
            shades that suit you — powered by computer vision and color science.
        </p>
        """,
        unsafe_allow_html=True
    )
    
    st.write("")

    # =====================================================
    # CTA BUTTONS
    # =====================================================

    _, c1, c2, _ = st.columns([2.2,1.1,1.1,2.2])

    with c1:
        if st.button(
            "Start Analysis →",
            type="primary",
            use_container_width=True
        ):
            st.session_state.page = "Skin Analysis"
            st.rerun()

    with c2:
        if st.button(
            "How It Works",
            use_container_width=True
        ):
            st.session_state.page = "About Method"
            st.rerun()

    st.write("")
    st.write("")

    # =====================================================
    # FEATURE CARDS
    # =====================================================

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="feature-card">

            <div class="feature-icon"
                 style="background:#FFF0F5;color:#F48ABD;">
                📷
            </div>

            <div class="feature-title">
                Upload Photo
            </div>

            <div class="feature-desc">
                Use your own photo or capture one live with your webcam.
                We analyze your skin directly.
            </div>

        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="feature-card"
             style="
                background:rgba(212,235,194,.42);
                border-color:rgba(186,223,147,.55);
             ">

            <div class="feature-icon"
                 style="background:#EEF4E8;color:#758952;">
                📊
            </div>

            <div class="feature-title">
                Skin Tone Analysis
            </div>

            <div class="feature-desc">
                Get your skin tone, undertone classification,
                and Monk Skin Tone scale score instantly.
            </div>

        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="feature-card">

            <div class="feature-icon"
                 style="background:#FFF0F5;color:#F48ABD;">
                ✨
            </div>

            <div class="feature-title">
                Foundation Recommendation
            </div>

            <div class="feature-desc">
                Matched foundations are ranked by Euclidean
                color distance for the most accurate shade.
            </div>

        </div>
        """, unsafe_allow_html=True)

    st.write("")

    # =====================================================
    # STATS
    # =====================================================

    st.markdown("""
    <div class="stats-card">

        <div style="
            display:grid;
            grid-template-columns:repeat(4,1fr);
            text-align:center;
        ">

            <div>
                <div class="stat-number">50+</div>
                <div class="stat-label">
                    Foundation Shades
                </div>
            </div>

            <div>
                <div class="stat-number">10</div>
                <div class="stat-label">
                    Brands Covered
                </div>
            </div>

            <div>
                <div class="stat-number">99%</div>
                <div class="stat-label">
                    Detection Accuracy
                </div>
            </div>

            <div>
                <div class="stat-number">&lt; 2s</div>
                <div class="stat-label">
                    Analysis Time
                </div>
            </div>

        </div>

    </div>
    """, unsafe_allow_html=True)
