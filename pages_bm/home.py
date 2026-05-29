# pages_ui/home.py
import streamlit as st

def render_home():

    # ── Hero section ──────────────────────────────────────────────────────────
    st.markdown("""
    <div class="hero">

        <!-- Badge pill -->
        <div>
            <span class="pill">
                <span style="width:7px;height:7px;border-radius:50%;
                             background:#F48ABD;display:inline-block;"></span>
                AI-Powered Foundation Matching
                <span style="width:7px;height:7px;border-radius:50%;
                             background:#F48ABD;display:inline-block;"></span>
            </span>
        </div>

        <!-- Title -->
        <h1 class="hero-title">
            Find Your Perfect <span class="pink">Foundation</span><br>
            <span class="green">Match</span>
        </h1>

        <!-- Subtitle -->
        <p class="subtitle">
            Analyze your skin tone and undertone to discover foundation
            shades that suit you — powered by computer vision and color
            science.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ── CTA buttons — Streamlit native agar bisa routing ─────────────────────
    _, c1, c2, _ = st.columns([1.6, 1.1, 1.0, 1.6])
    with c1:
        if st.button("Start Analysis  →", key="home_start",
                     type="primary", use_container_width=True):
            st.session_state.page = "Skin Analysis"
            st.rerun()
    with c2:
        if st.button("How It Works", key="home_how",
                     use_container_width=True):
            st.session_state.page = "About Method"
            st.rerun()

    st.markdown("<div style='margin-top:2.4rem'></div>", unsafe_allow_html=True)

    # ── Feature cards ─────────────────────────────────────────────────────────
    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:
        st.markdown("""
        <div class="custom-card feature-card pink-tint">
            <div class="feature-icon" style="background:rgba(255,168,214,.28);">📷</div>
            <h3>Upload Photo</h3>
            <p>Use your own photo or capture one live with your webcam.
               We analyze your skin directly.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="custom-card feature-card green-tint"
             style="transform:translateY(-6px);">
            <div class="feature-icon" style="background:rgba(186,223,147,.38);">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none"
                     stroke="#758952" stroke-width="2.2" stroke-linecap="round">
                    <line x1="18" y1="20" x2="18" y2="10"/>
                    <line x1="12" y1="20" x2="12" y2="4"/>
                    <line x1="6"  y1="20" x2="6"  y2="14"/>
                </svg>
            </div>
            <h3>Skin Tone Analysis</h3>
            <p>Get your skin tone, undertone classification, and Monk Skin Tone
               scale score instantly.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="custom-card feature-card purple-tint">
            <div class="feature-icon" style="background:rgba(214,185,242,.35);">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none"
                     stroke="#9c67c0" stroke-width="1.8" stroke-linecap="round"
                     stroke-linejoin="round">
                    <polygon points="12,2 15.09,8.26 22,9.27 17,14.14
                                     18.18,21.02 12,17.77 5.82,21.02
                                     7,14.14 2,9.27 8.91,8.26"/>
                </svg>
            </div>
            <h3>Foundation<br>Recommendation</h3>
            <p>Matched foundations are ranked by Euclidean color distance
               for the most accurate shade.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='margin-top:1.6rem'></div>", unsafe_allow_html=True)

    # ── Stats bar ─────────────────────────────────────────────────────────────
    st.markdown("""
    <div class="custom-card stats-card"
         style="
            background: linear-gradient(135deg,
                rgba(249,209,217,.85) 0%,
                rgba(212,235,194,.75) 100%);
            border-color: rgba(248,168,214,.35);
            padding: 1.8rem 2.4rem;">
        <div style="
            display: grid;
            grid-template-columns: repeat(4,1fr);
            text-align: center;
            gap: 0;">

            <div style="padding:0 1rem;">
                <div class="stat-number">50+</div>
                <div class="stat-label">Foundation Shades</div>
            </div>

            <div style="
                padding:0 1rem;
                border-left:1px solid rgba(255,255,255,.55);">
                <div class="stat-number">10</div>
                <div class="stat-label">Brands Covered</div>
            </div>

            <div style="
                padding:0 1rem;
                border-left:1px solid rgba(255,255,255,.55);">
                <div class="stat-number">99%</div>
                <div class="stat-label">Detection Accuracy</div>
            </div>

            <div style="
                padding:0 1rem;
                border-left:1px solid rgba(255,255,255,.55);">
                <div class="stat-number">&lt; 2s</div>
                <div class="stat-label">Analysis Time</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
