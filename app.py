import streamlit as st

st.set_page_config(
    page_title="Beauty Match",
    page_icon="💄",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Playfair+Display:wght@700;800&display=swap');

:root {
    --bg:        #FFF0F5;
    --pink:      #F9D1D9;
    --hot:       #F48ABD;
    --accent:    #FFA8D6;
    --dusty:     #E8C0C5;
    --pistachio: #D4EBC2;
    --mint:      #CFE5B7;
    --green:     #BADF93;
    --matcha:    #838F58;
    --olive:     #758952;
    --text:      #2F2330;
    --muted:     #7B6472;
    --border:    rgba(248,168,214,.42);
}

.stApp {
    background:
        radial-gradient(circle at 92% 6%,  rgba(255,168,214,.46), transparent 23rem),
        radial-gradient(circle at 9%  78%, rgba(212,235,194,.62), transparent 23rem),
        linear-gradient(135deg, #FFF0F5 0%, #FFF8F6 48%, #F4E2E4 100%);
    color: var(--text);
    font-family: Inter, sans-serif;
}

#MainMenu, footer, header { visibility: hidden; }
.block-container { max-width: 1480px; padding: 2.3rem 2rem 4rem; }
h1, h2, h3 { font-family: 'Playfair Display', serif; color: var(--text); }

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
section[data-testid="stSidebar"] > div { padding-top: 1.1rem; }

.sidebar-brand {
    display: flex; align-items: center; gap: .85rem;
    padding: .9rem .65rem 1.15rem;
    border-bottom: 1px solid rgba(232,192,197,.72);
    margin-bottom: 1.2rem;
}
.logo-box {
    width: 42px; height: 42px; border-radius: 15px;
    display: flex; align-items: center; justify-content: center;
    background: linear-gradient(135deg, var(--accent), var(--olive));
    box-shadow: 0 8px 18px rgba(117,137,82,.2);
    color: white; font-size: 1.25rem;
}
.brand-kicker {
    font-size: .72rem; letter-spacing: .08em;
    text-transform: uppercase; color: var(--olive); font-weight: 700;
}
.brand-name { font-size: 1.22rem; color: #34431d; font-weight: 900; line-height: 1; }

div[role="radiogroup"] label {
    padding: .75rem .9rem !important;
    border-radius: 1rem !important;
    margin: .25rem .15rem !important;
    font-weight: 800 !important;
    color: #758952 !important;
}
div[role="radiogroup"] label:has(input:checked) {
    background: linear-gradient(90deg,
        rgba(255,168,214,.82), rgba(249,209,217,.70)) !important;
    color: #2F2330 !important;
    box-shadow: 0 10px 20px rgba(248,138,189,.16);
}
div[role="radiogroup"] label > div:first-child { display: none; }

.sidebar-footer {
    position: fixed; bottom: 2rem; left: 1.65rem; width: 205px;
    text-align: center; padding: 1.1rem .8rem; border-radius: 1.05rem;
    color: var(--olive); background: rgba(212,235,194,.44);
    border: 1px solid rgba(181,196,154,.4); font-size: .78rem;
}

/* ── Hero ── */
.hero { text-align: center; padding: 2.6rem 1rem 1.4rem; }
.pill {
    display: inline-flex; align-items: center; gap: .4rem;
    padding: .45rem 1rem; border-radius: 999px;
    background: rgba(249,209,217,.62); color: #D94E91;
    border: 1px solid rgba(255,168,214,.75);
    font-weight: 900; font-size: .78rem;
    letter-spacing: .06em; text-transform: uppercase;
}
.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(2.7rem, 4.2vw, 5.15rem);
    line-height: 1.03; font-weight: 800;
    letter-spacing: -.03em; margin: 1.25rem 0 .9rem;
}
.hero-title .pink  { color: #EB80B6; }
.hero-title .green { color: var(--matcha); }
.subtitle {
    color: var(--muted); font-size: 1.02rem;
    line-height: 1.8; max-width: 620px; margin: 0 auto;
}

/* ── Buttons ── */
.stButton > button {
    border-radius: .95rem !important;
    font-weight: 900 !important;
    font-family: Inter, sans-serif !important;
    transition: all .2s !important;
}
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #F48ABD, #E7569F) !important;
    color: #fff !important;
    border: none !important;
    box-shadow: 0 12px 24px rgba(231,86,159,.22) !important;
    min-height: 46px !important;
}
.stButton > button[kind="primary"]:hover {
    box-shadow: 0 16px 32px rgba(231,86,159,.32) !important;
    transform: translateY(-1px) !important;
}
.stButton > button[kind="secondary"] {
    background: rgba(255,255,255,.72) !important;
    border: 1.5px solid rgba(117,137,82,.55) !important;
    color: var(--olive) !important;
}
.stButton > button[kind="secondary"]:hover {
    border-color: #F48ABD !important;
    color: #E7569F !important;
}

/* ── Cards ── */
.custom-card, .metric-card, .product-card {
    background: rgba(255,255,255,.78);
    border: 1px solid var(--border);
    border-radius: 1.35rem;
    box-shadow: 0 16px 36px rgba(200,107,133,.09);
    backdrop-filter: blur(16px);
}
.feature-card { padding: 1.8rem; min-height: 175px; }
.feature-icon {
    width: 48px; height: 48px; border-radius: 1rem;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.35rem; margin-bottom: 1rem;
}
.feature-card h3 { font-size: 1.28rem; margin: .4rem 0 .55rem; }
.feature-card p, .small-text { color: var(--muted); font-size: .9rem; line-height: 1.65; }

.pink-tint   { background: rgba(255,240,245,.7)  !important; border-color: rgba(255,168,214,.55) !important; }
.green-tint  { background: rgba(212,235,194,.42) !important; border-color: rgba(186,223,147,.55) !important; }
.purple-tint { background: rgba(244,226,255,.48) !important; border-color: rgba(214,185,242,.45) !important; }

/* ── Stats ── */
.stats-card { margin: 1.5rem auto; padding: 1.1rem 1rem; max-width: 880px; }
.stat-number { color: #F48ABD; font-weight: 900; font-size: 2rem; line-height: 1; }
.stat-label  { color: var(--muted); font-size: .83rem; margin-top: .3rem; }

/* ── Result cards ── */
.result-card {
    background: rgba(255,255,255,.82);
    border: 1px solid rgba(248,168,214,.35);
    border-radius: 1.15rem;
    padding: 1.35rem 1.45rem;
    margin-bottom: 1rem;
    backdrop-filter: blur(12px);
}
.result-card-label {
    font-size: .72rem; font-weight: 900;
    text-transform: uppercase; letter-spacing: .08em;
    color: var(--hot); margin-bottom: .55rem;
}
.result-card-value { font-size: 1.35rem; font-weight: 900; color: var(--text); }
.result-card-sub   { font-size: .78rem; color: var(--muted); margin-top: .3rem; }

.conf-bar-wrap {
    background: rgba(232,192,197,.35);
    border-radius: 999px; height: 8px; overflow: hidden; margin: .6rem 0;
}
.lab-grid {
    display: grid; grid-template-columns: repeat(3,1fr);
    gap: .75rem; margin-top: .5rem;
}
.lab-cell {
    background: rgba(255,240,245,.7);
    border-radius: .85rem; padding: .9rem 1rem;
    border: 1px solid rgba(248,168,214,.3);
}
.lab-cell-label { font-size: .72rem; color: var(--muted); margin-bottom: .3rem; font-weight: 600; }
.lab-cell-val   { font-size: 1.25rem; font-weight: 900; color: var(--text); }

/* ── Upload page ── */
.upload-zone {
    border: 2px dashed rgba(255,168,214,.65);
    border-radius: 1.4rem;
    background: rgba(255,255,255,.72);
    text-align: center; padding: 2.5rem 2rem;
    transition: background .2s;
}
.upload-zone:hover { background: rgba(255,240,245,.9); }
.tip-card {
    padding: 1.6rem;
    background: rgba(255,255,255,.82);
    border: 1px solid rgba(181,196,154,.7);
    border-radius: 1.25rem;
    box-shadow: 0 12px 28px rgba(117,137,82,.08);
    margin-top: 1rem;
}
.tip-item { display: flex; gap: .85rem; margin: .9rem 0; }
.tip-icon {
    width: 32px; height: 32px; border-radius: 50%;
    background: rgba(249,209,217,.5);
    display: flex; align-items: center; justify-content: center;
    font-size: 1rem; flex-shrink: 0; margin-top: 1px;
}
.preview-empty {
    background: rgba(255,255,255,.55); border-radius: 1.25rem;
    border: 1px solid rgba(248,168,214,.3);
    height: 200px; display: flex; flex-direction: column;
    align-items: center; justify-content: center; color: var(--muted);
}

/* ── Product cards ── */
.product-card { padding: 1.35rem 1.45rem; margin-bottom: 1rem; }
.product-brand {
    font-size: .72rem; color: var(--muted);
    letter-spacing: .08em; text-transform: uppercase; font-weight: 900;
}
.product-name  { font-weight: 900; font-size: 1rem; color: var(--text); margin: .1rem 0 .35rem; }
.price         { font-size: 1.05rem; font-weight: 900; color: var(--text); }
.match-badge   {
    display: inline-block; padding: .3rem .65rem; border-radius: 999px;
    background: rgba(212,235,194,.72); color: #3C7D47; font-weight: 900; font-size: .78rem;
}
.reason {
    background: rgba(255,240,245,.75); border-radius: .8rem;
    padding: .55rem .75rem; color: var(--muted); font-size: .82rem; margin: .6rem 0;
}
.chip {
    display: inline-flex; align-items: center;
    padding: .4rem .85rem; border-radius: 999px;
    border: 1px solid rgba(248,168,214,.65);
    color: var(--muted); background: rgba(255,255,255,.62);
    font-weight: 700; font-size: .82rem; cursor: pointer;
}
.chip.active { color: #fff; background: #F48ABD; border-color: #F48ABD; }

/* ── About Method ── */
.step-card {
    background: rgba(255,255,255,.78);
    border: 1px solid rgba(248,168,214,.35);
    border-radius: 1.25rem; padding: 1.35rem 1.45rem;
    margin-bottom: .9rem;
    backdrop-filter: blur(12px);
    display: flex; gap: 1.1rem; align-items: flex-start;
}
.step-icon-wrap {
    width: 46px; height: 46px; border-radius: 1rem;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.3rem; flex-shrink: 0;
}
.step-badge-num {
    width: 26px; height: 26px; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: .78rem; font-weight: 900; color: white; flex-shrink: 0;
}
.tag-pill {
    display: inline-block; padding: .25rem .7rem;
    border-radius: 999px; font-size: .72rem; font-weight: 700;
    margin: 2px; background: rgba(255,240,245,.85);
    color: var(--muted); border: 1px solid rgba(248,168,214,.35);
}
.pipeline-wrap {
    background: linear-gradient(135deg,
        rgba(249,209,217,.55), rgba(212,235,194,.55));
    border-radius: 1.25rem; padding: 1.4rem 1.6rem;
    margin-bottom: 1.5rem;
    border: 1px solid rgba(248,168,214,.25);
}

@media (max-width: 900px) { .sidebar-footer { display: none; } }
</style>
""", unsafe_allow_html=True)

# ── Session state ──────────────────────────────────────────────────────────
for key, default in [
    ("page", "Home"),
    ("analysis_result", None),
    ("input_image", None),
    ("nav_target", None),
]:
    if key not in st.session_state:
        st.session_state[key] = default

# ── Handle nav_target dari pages lain ─────────────────────────────────────
_NAV_MAP = {
    "home":          "Home",
    "skin":          "Skin Analysis",
    "skin_analysis": "Skin Analysis",
    "results":       "Results",
    "foundation":    "Foundation",
    "about":         "About Method",
}
if st.session_state.nav_target:
    target = _NAV_MAP.get(st.session_state.nav_target)
    if target:
        st.session_state.page = target
    st.session_state.nav_target = None
    st.rerun()

# ── Import pages ───────────────────────────────────────────────────────────
from pages_bm.home          import render_home
from pages_bm.skin_analysis import render_skin_analysis
from pages_bm.results       import render_results
from pages_bm.foundation    import render_foundation
from pages_bm.about_method  import render_about_method

# ── Sidebar ────────────────────────────────────────────────────────────────
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
        "Home": "🏠", "Skin Analysis": "📷",
        "Results": "📊", "Foundation": "💄", "About Method": "📖",
    }

    sel = st.radio(
        "nav", pages,
        index=pages.index(st.session_state.page),
        format_func=lambda x: f"{icons[x]}  {x}",
        label_visibility="collapsed",
    )
    if sel != st.session_state.page:
        st.session_state.page = sel
        st.rerun()

    st.markdown("""
    <div class="sidebar-footer">
        <strong>Beauty Match v1.0</strong><br>
        Capstone Project 2026
    </div>
    """, unsafe_allow_html=True)

# ── Router ─────────────────────────────────────────────────────────────────
_page = st.session_state.page
if   _page == "Home":          render_home()
elif _page == "Skin Analysis": render_skin_analysis()
elif _page == "Results":       render_results()
elif _page == "Foundation":    render_foundation()
elif _page == "About Method":  render_about_method()
