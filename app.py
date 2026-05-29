import streamlit as st

st.set_page_config(
    page_title="Beauty Match",
    page_icon="💄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── Global CSS — menggunakan design system dari style.css ─────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Playfair+Display:wght@700;800&display=swap');

/* ── Design tokens ── */
:root {
    --bg:         #FFF0F5;
    --pink:       #F9D1D9;
    --hot:        #F48ABD;
    --accent:     #FFA8D6;
    --dusty:      #E8C0C5;
    --pistachio:  #D4EBC2;
    --mint:       #CFE5B7;
    --green:      #BADF93;
    --matcha:     #838F58;
    --olive:      #758952;
    --text:       #2F2330;
    --muted:      #7B6472;
    --border:     rgba(248,168,214,.42);
}

/* ── App background — triple radial gradient ── */
.stApp {
    background:
        radial-gradient(circle at 92% 6%,  rgba(255,168,214,.46), transparent 23rem),
        radial-gradient(circle at 9%  78%, rgba(212,235,194,.62), transparent 23rem),
        linear-gradient(135deg, #FFF0F5 0%, #FFF8F6 48%, #F4E2E4 100%);
    color: var(--text);
    font-family: Inter, sans-serif;
}

/* ── Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
.block-container {
    max-width: 1480px;
    padding: 2.3rem 2rem 4rem;
}
h1, h2, h3 {
    font-family: 'Playfair Display', serif;
    color: var(--text);
}

/* ── Sidebar ── */
section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        rgba(255,240,245,.96),
        rgba(255,240,245,.93) 68%,
        rgba(212,235,194,.84)
    ) !important;
    border-right: 1px solid rgba(232,192,197,.7);
    box-shadow: 12px 0 35px rgba(232,192,197,.16);
}
section[data-testid="stSidebar"] > div {
    padding-top: 1.1rem;
}

/* ── Sidebar brand block ── */
.sidebar-brand {
    display: flex;
    align-items: center;
    gap: .85rem;
    padding: .9rem .65rem 1.15rem;
    border-bottom: 1px solid rgba(232,192,197,.72);
    margin-bottom: 1.2rem;
}
.logo-box {
    width: 42px; height: 42px;
    border-radius: 15px;
    display: flex; align-items: center; justify-content: center;
    background: linear-gradient(135deg, var(--accent), var(--olive));
    box-shadow: 0 8px 18px rgba(117,137,82,.2);
    color: white;
    font-size: 1.25rem;
}
.brand-kicker {
    font-size: .72rem;
    letter-spacing: .08em;
    text-transform: uppercase;
    color: var(--olive);
    font-weight: 700;
}
.brand-name {
    font-size: 1.22rem;
    color: #34431d;
    font-weight: 900;
    line-height: 1;
}

/* ── Sidebar nav radio ── */
div[role="radiogroup"] label {
    padding: .75rem .9rem !important;
    border-radius: 1rem !important;
    margin: .25rem .15rem !important;
    font-weight: 800 !important;
    color: #758952 !important;
}
div[role="radiogroup"] label:has(input:checked) {
    background: linear-gradient(90deg,
        rgba(255,168,214,.82),
        rgba(249,209,217,.70)
    ) !important;
    color: #2F2330 !important;
    box-shadow: 0 10px 20px rgba(248,138,189,.16);
}
div[role="radiogroup"] label > div:first-child {
    display: none;
}

/* ── Sidebar footer badge ── */
.sidebar-footer {
    position: fixed;
    bottom: 2rem;
    left: 1.65rem;
    width: 205px;
    text-align: center;
    padding: 1.1rem .8rem;
    border-radius: 1.05rem;
    color: var(--olive);
    background: rgba(212,235,194,.44);
    border: 1px solid rgba(181,196,154,.4);
    font-size: .78rem;
}

/* ── Hero section ── */
.hero {
    text-align: center;
    padding: 2.6rem 1rem 1.4rem;
}
.pill {
    display: inline-flex;
    align-items: center;
    gap: .4rem;
    padding: .45rem 1rem;
    border-radius: 999px;
    background: rgba(249,209,217,.62);
    color: #D94E91;
    border: 1px solid rgba(255,168,214,.75);
    font-weight: 900;
    font-size: .78rem;
    letter-spacing: .06em;
    text-transform: uppercase;
}
.pill.green {
    background: rgba(212,235,194,.7);
    color: var(--olive);
    border-color: rgba(181,196,154,.55);
}
.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(2.7rem, 4.2vw, 5.15rem);
    line-height: 1.03;
    font-weight: 800;
    letter-spacing: -.03em;
    margin: 1.25rem 0 .9rem;
}
.hero-title .pink  { color: #EB80B6; }
.hero-title .green { color: var(--matcha); }
.subtitle {
    color: var(--muted);
    font-size: 1.02rem;
    line-height: 1.8;
    max-width: 620px;
    margin: 0 auto;
}
.cta-row {
    display: flex;
    justify-content: center;
    gap: 1rem;
    margin-top: 1.6rem;
}
.btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: .6rem;
    border-radius: .95rem;
    font-weight: 900;
    padding: .95rem 1.75rem;
    min-height: 46px;
    border: 1px solid transparent;
    font-family: Inter, sans-serif;
    cursor: pointer;
    text-decoration: none;
}
.btn-primary {
    background: linear-gradient(135deg, #F48ABD, #E7569F);
    color: #fff;
    box-shadow: 0 14px 26px rgba(231,86,159,.22);
}
.btn-outline {
    background: rgba(255,255,255,.62);
    border-color: rgba(117,137,82,.62);
    color: var(--olive);
}

/* ── Cards (shared) ── */
.custom-card, .metric-card, .product-card {
    background: rgba(255,255,255,.78);
    border: 1px solid var(--border);
    border-radius: 1.35rem;
    box-shadow: 0 16px 36px rgba(200,107,133,.09);
    backdrop-filter: blur(16px);
}
.feature-card {
    padding: 1.8rem;
    min-height: 175px;
}
.feature-icon, .method-icon {
    width: 48px; height: 48px;
    border-radius: 1rem;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.35rem;
    margin-bottom: 1rem;
}
.feature-card h3 {
    font-size: 1.28rem;
    margin: .4rem 0 .55rem;
}
.feature-card p, .small-text {
    color: var(--muted);
    font-size: .9rem;
    line-height: 1.65;
}
.pink-tint {
    background: rgba(255,240,245,.7) !important;
    border-color: rgba(255,168,214,.55) !important;
}
.green-tint {
    background: rgba(212,235,194,.42) !important;
    border-color: rgba(186,223,147,.55) !important;
}
.purple-tint {
    background: rgba(244,226,255,.48) !important;
    border-color: rgba(214,185,242,.45) !important;
}

/* ── Stats card ── */
.stats-card {
    margin: 1.5rem auto;
    padding: 1.1rem 1rem;
    max-width: 880px;
}
.stat-number {
    color: #F48ABD;
    font-weight: 900;
    font-size: 2rem;
    line-height: 1;
}
.stat-label {
    color: var(--muted);
    font-size: .83rem;
    margin-top: .3rem;
}

/* ── Step nodes ── */
.step-node {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: .35rem;
}
.step-badge {
    background: linear-gradient(135deg, #F48ABD, #FFA8D6);
    color: white;
    border-radius: 999px;
    font-weight: 900;
    padding: .34rem .55rem;
    font-size: .76rem;
}
.step-icon {
    width: 52px; height: 52px;
    border-radius: 999px;
    display: flex; align-items: center; justify-content: center;
    background: var(--pink);
    color: #E7569F;
    font-size: 1.25rem;
    box-shadow: 0 12px 20px rgba(248,138,189,.2);
}
.step-title { font-weight: 900; margin-top: .25rem; }
.page-title {
    font-size: clamp(2.2rem, 3vw, 3.4rem);
    margin: .4rem 0 .35rem;
}

/* ── Upload page ── */
.upload-box {
    height: 410px;
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    border: 2px dashed rgba(255,168,214,.65);
    border-radius: 1.4rem;
    background: rgba(255,255,255,.72);
    text-align: center;
    padding: 2rem;
}
.upload-symbol {
    width: 84px; height: 84px;
    border-radius: 1.55rem;
    display: flex; align-items: center; justify-content: center;
    background: var(--pink);
    color: #F48ABD;
    font-size: 2.4rem;
    margin-bottom: 1.4rem;
}
.tip-card {
    padding: 1.8rem;
    background: rgba(255,255,255,.82);
    border: 1px solid rgba(181,196,154,.7);
    border-radius: 1.35rem;
    box-shadow: 0 16px 32px rgba(117,137,82,.1);
}
.tip-item {
    display: flex;
    gap: .85rem;
    margin: 1.05rem 0;
}
.tip-item strong { display: block; margin-bottom: .18rem; }
.tip-emoji { font-size: 1.2rem; width: 1.7rem; }
.notice {
    background: rgba(255,240,245,.85);
    border: 1px solid rgba(255,168,214,.5);
    color: #B9507D;
    border-radius: 1.15rem;
    padding: 1.2rem;
    line-height: 1.55;
    margin-top: 1rem;
}
.stButton > button[kind="primary"] {
    width: 100%;
    min-height: 54px;
    border-radius: 1rem;
    border: 0;
    font-weight: 900;
    background: linear-gradient(135deg, #F48ABD, #E7569F);
    color: #fff;
    box-shadow: 0 12px 24px rgba(231,86,159,.2);
}

/* ── Results / metric cards ── */
.metric-card {
    padding: 1.45rem 1.55rem;
    min-height: 126px;
}
.metric-label {
    color: #D94E91;
    font-weight: 900;
    letter-spacing: .08em;
    font-size: .78rem;
    text-transform: uppercase;
    margin-bottom: .65rem;
}
.metric-value {
    font-size: 1.45rem;
    font-weight: 900;
    color: var(--text);
}
.swatch {
    border-radius: .75rem;
    box-shadow: inset 0 0 0 1px rgba(255,255,255,.35), 0 10px 24px rgba(0,0,0,.09);
}
.mst-strip {
    display: grid;
    grid-template-columns: repeat(10, 1fr);
    gap: .65rem;
    align-items: end;
}
.mst-item { text-align: center; position: relative; }
.mst-color {
    height: 36px;
    border-radius: .5rem;
    border: 2px solid transparent;
}
.mst-item.match .mst-color {
    height: 46px;
    border: 4px solid #F48ABD;
    box-shadow: 0 0 0 6px rgba(255,168,214,.25), 0 10px 25px rgba(244,138,189,.28);
}
.match-label {
    position: absolute;
    top: -42px; left: 50%;
    transform: translateX(-50%);
    background: #F48ABD;
    color: white;
    border-radius: .65rem;
    padding: .45rem .8rem;
    font-size: .78rem;
    font-weight: 900;
    white-space: nowrap;
}
.progress-track {
    height: 10px; width: 100%;
    background: rgba(232,192,197,.45);
    border-radius: 999px;
    overflow: hidden;
}
.progress-fill {
    height: 100%;
    background: linear-gradient(90deg, var(--green), var(--olive));
    border-radius: 999px;
}
.progress-fill.pink {
    background: linear-gradient(90deg, #F48ABD, #E7569F);
}

/* ── Foundation product cards ── */
.product-card {
    padding: 1rem 1.1rem;
    min-height: 218px;
}
.product-brand {
    font-size: .78rem;
    color: var(--muted);
    letter-spacing: .08em;
    text-transform: uppercase;
    font-weight: 900;
}
.product-name {
    font-weight: 900;
    font-size: 1rem;
    color: var(--text);
    margin: .1rem 0 .35rem;
}
.price {
    font-size: 1.05rem;
    font-weight: 900;
    color: var(--text);
}
.match-badge {
    display: inline-block;
    padding: .35rem .65rem;
    border-radius: 999px;
    background: rgba(212,235,194,.72);
    color: #3C7D47;
    font-weight: 900;
    font-size: .78rem;
}
.reason {
    background: rgba(255,240,245,.75);
    border-radius: .8rem;
    padding: .55rem .75rem;
    color: var(--muted);
    font-size: .82rem;
    margin: .65rem 0;
}
.chip {
    display: inline-flex;
    align-items: center;
    padding: .45rem .9rem;
    border-radius: 999px;
    border: 1px solid rgba(248,168,214,.65);
    color: var(--muted);
    background: rgba(255,255,255,.62);
    font-weight: 700;
    font-size: .82rem;
}
.chip.active {
    color: #fff;
    background: #F48ABD;
    border-color: #F48ABD;
}

/* ── About Method ── */
.method-timeline {
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    gap: .85rem;
    text-align: center;
}
.pipeline-card { padding: 1.5rem; }
.method-card { padding: 1.35rem; min-height: 235px; }
.code-note {
    border-radius: .85rem;
    padding: .8rem .9rem;
    font-size: .78rem;
    margin-top: 1rem;
    font-family: monospace;
    line-height: 1.55;
}
.tech-card {
    display: flex;
    align-items: center;
    gap: .9rem;
    padding: 1rem;
    border-radius: 1rem;
    border: 1px solid rgba(232,192,197,.45);
    background: rgba(255,255,255,.64);
}
.tech-icon {
    width: 44px; height: 44px;
    border-radius: .9rem;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.45rem;
}
.ref-box {
    padding: 1.4rem;
    background: rgba(255,240,245,.72);
    border: 1px solid rgba(255,168,214,.45);
    border-radius: 1.25rem;
}

/* ── Responsive ── */
@media (max-width: 900px) {
    .method-timeline { grid-template-columns: repeat(2,1fr); }
    .sidebar-footer  { display: none; }
}
</style>
""", unsafe_allow_html=True)

# ─── Session State Init ────────────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "Home"
if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = None
if "uploaded_image" not in st.session_state:
    st.session_state.uploaded_image = None

# ─── Import pages ──────────────────────────────────────────────────────────
from pages_ui.home         import render_home
from pages_ui.skin_analysis import render_skin_analysis
from pages_ui.results       import render_results
from pages_ui.foundation    import render_foundation
from pages_ui.about_method  import render_about_method

# ─── Sidebar ──────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="sidebar-brand">
        <div class="logo-box">💄</div>
        <div>
            <div class="brand-name">Beauty Match</div>
            <div class="brand-kicker">Foundation Advisor</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    pages = ["Home", "Skin Analysis", "Results", "Foundation", "About Method"]
    icons = {
        "Home":          "🏠",
        "Skin Analysis": "📷",
        "Results":       "📊",
        "Foundation":    "💄",
        "About Method":  "📖",
    }

    current = st.radio(
        "nav",
        pages,
        index=pages.index(st.session_state.page),
        format_func=lambda x: f"{icons[x]}  {x}",
        label_visibility="collapsed",
    )
    if current != st.session_state.page:
        st.session_state.page = current
        st.rerun()

    st.markdown("""
    <div class="sidebar-footer">
        <strong>Beauty Match v1.0</strong><br>
        Capstone Project 2026
    </div>
    """, unsafe_allow_html=True)

# ─── Router ────────────────────────────────────────────────────────────────
page = st.session_state.page
if   page == "Home":          render_home()
elif page == "Skin Analysis": render_skin_analysis()
elif page == "Results":       render_results()
elif page == "Foundation":    render_foundation()
elif page == "About Method":  render_about_method()
