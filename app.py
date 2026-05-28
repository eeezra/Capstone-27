import streamlit as st

st.set_page_config(
    page_title="Beauty Match",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Lock sidebar ─────────────────────────────────────────
st.markdown("""
<style>
[data-testid="collapsedControl"] { display: none !important; }
section[data-testid="stSidebar"] {
    transform: none !important;
    width: 200px !important;
    min-width: 200px !important;
    max-width: 200px !important;
}
</style>
""", unsafe_allow_html=True)

# ─── Global CSS ───────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Playfair+Display:wght@700;800&display=swap');

* { font-family: 'Inter', sans-serif !important; }

.stApp {
    background:
        radial-gradient(circle at 88% 8%,  rgba(255,168,214,.38), transparent 22rem),
        radial-gradient(circle at 6%  82%,  rgba(212,235,194,.50), transparent 22rem),
        linear-gradient(135deg, #FFF0F5 0%, #FFF8F6 50%, #F9EEF2 100%) !important;
    color: #2F2330;
}
.main, .main .block-container {
    background: transparent !important;
}
.main .block-container {
    padding-top: 1rem;
    padding-bottom: 2rem;
    max-width: 1200px;
}

#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }

/* ── Sidebar ── */
section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        rgba(255,240,245,.97) 0%,
        rgba(255,240,245,.94) 65%,
        rgba(212,235,194,.85) 100%
    ) !important;
    border-right: 1px solid rgba(232,192,197,.70) !important;
    box-shadow: 12px 0 35px rgba(232,192,197,.16) !important;
}
section[data-testid="stSidebar"] > div:first-child {
    background: transparent !important;
    padding-top: 0 !important;
}
section[data-testid="stSidebar"] .block-container {
    padding: 0.8rem 0.75rem !important;
    background: transparent !important;
}

/* ── Sembunyikan semua elemen Streamlit di dalam sidebar
      kecuali yang kita render sendiri ── */
section[data-testid="stSidebar"] .stButton,
section[data-testid="stSidebar"] .stButton > button,
section[data-testid="stSidebar"] div[data-testid="stVerticalBlock"] > div {
    all: unset !important;
    display: block !important;
}
section[data-testid="stSidebar"] .stButton > button {
    display: none !important;
}

/* ── Nav item HTML custom ── */
.nav-item {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 9px 12px;
    border-radius: 10px;
    font-size: 13.5px;
    font-weight: 600;
    color: #758952;
    cursor: pointer;
    transition: background 0.15s, color 0.15s;
    margin: 2px 0;
    text-decoration: none;
    user-select: none;
}
.nav-item:hover {
    background: rgba(255,168,214,.28);
    color: #D94E91;
}
.nav-item.active {
    background: linear-gradient(90deg, rgba(255,168,214,.85), rgba(249,209,217,.70));
    color: #2F2330;
    font-weight: 700;
}
.nav-item .nav-icon {
    font-size: 14px;
    width: 18px;
    text-align: center;
    flex-shrink: 0;
}

/* ── Global buttons konten utama ── */
.main .stButton > button {
    border-radius: 999px !important;
    font-weight: 700 !important;
    transition: all 0.2s !important;
    min-height: 44px !important;
    display: inline-flex !important;
    align-items: center !important;
}
.main .stButton > button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 18px rgba(192,88,126,.22) !important;
}
.main .stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #F48ABD, #D94E91) !important;
    color: white !important;
    border: none !important;
    box-shadow: 0 8px 20px rgba(217,78,145,.20) !important;
}
.main .stButton > button[kind="secondary"] {
    background: rgba(255,255,255,.80) !important;
    color: #758952 !important;
    border: 1.5px solid rgba(117,137,82,.50) !important;
}

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] {
    background: rgba(255,240,245,.80);
    border-radius: 999px;
    padding: 4px;
    gap: 4px;
    border-bottom: none !important;
}
.stTabs [data-baseweb="tab"] {
    border-radius: 999px !important;
    padding: 6px 18px !important;
    font-weight: 600 !important;
    font-size: 13px !important;
    color: #999 !important;
    background: transparent !important;
    border: none !important;
}
.stTabs [aria-selected="true"] {
    background: white !important;
    color: #D94E91 !important;
    box-shadow: 0 2px 8px rgba(0,0,0,.08) !important;
}
.stTabs [data-baseweb="tab-highlight"],
.stTabs [data-baseweb="tab-border"] { display: none !important; }

.stSelectbox > div > div {
    border-radius: 10px !important;
    border-color: rgba(248,168,214,.50) !important;
    background: rgba(255,255,255,.80) !important;
}
.stFileUploader { border-radius: 14px !important; }
.stDataFrame { border-radius: 12px !important; overflow: hidden !important; }
.stSpinner > div { border-top-color: #D94E91 !important; }
.streamlit-expanderHeader {
    background: rgba(255,255,255,.75) !important;
    border-radius: 12px !important;
    border: 1px solid rgba(248,168,214,.40) !important;
    font-weight: 600 !important;
}
::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: #FFF0F5; }
::-webkit-scrollbar-thumb { background: #F4A0B8; border-radius: 999px; }
</style>
""", unsafe_allow_html=True)

# ─── State management ─────────────────────────────────────
if "page" not in st.session_state:
    st.session_state["page"] = "home"
if "nav_target" in st.session_state:
    st.session_state["page"] = st.session_state.pop("nav_target")

current_page = st.session_state["page"]

nav_items = [
    ("home",       "⌂", "Home"),
    ("skin",       "▣", "Skin Analysis"),
    ("results",    "▥", "Results"),
    ("foundation", "✧", "Foundation"),
    ("about",      "▤", "About Method"),
]

# ─── Sidebar ──────────────────────────────────────────────
with st.sidebar:

    # Logo
    st.markdown("""
    <div style="
        display:flex;align-items:center;gap:9px;
        padding:.5rem .2rem .7rem;
        border-bottom:1px solid rgba(232,192,197,.55);
        margin-bottom:.6rem;">
        <div style="
            width:36px;height:36px;border-radius:11px;flex-shrink:0;
            background:linear-gradient(135deg,#FFA8D6,#838F58);
            display:flex;align-items:center;justify-content:center;
            font-size:1rem;color:white;
            box-shadow:0 5px 12px rgba(117,137,82,.20);">✿</div>
        <div>
            <div style="font-size:.62rem;font-weight:700;
                letter-spacing:.08em;text-transform:uppercase;
                color:#758952;line-height:1.3;">Capstone 27</div>
            <div style="font-weight:900;font-size:.9rem;
                color:#2F2330;line-height:1.2;">Beauty Match</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Nav — render semua sebagai HTML murni + st.button tersembunyi
    for page_id, icon, label in nav_items:
        is_active = current_page == page_id
        active_class = "active" if is_active else ""

        # HTML nav item visual
        st.markdown(f"""
        <div class="nav-item {active_class}"
             id="nav-{page_id}"
             onclick="document.getElementById('btn-{page_id}').click()">
            <span class="nav-icon">{icon}</span>
            <span>{label}</span>
        </div>
        """, unsafe_allow_html=True)

        # Button tersembunyi yang trigger Streamlit
        if st.button(label, key=f"btn_{page_id}", label_visibility="collapsed"):
            st.session_state["page"] = page_id
            st.rerun()

    # Sembunyikan semua button bawaan Streamlit di sidebar
    st.markdown("""
    <style>
    section[data-testid="stSidebar"] button {
        position: absolute !important;
        opacity: 0 !important;
        width: 0 !important;
        height: 0 !important;
        pointer-events: none !important;
        overflow: hidden !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # Footer
    st.markdown("""
    <div style="
        position:fixed;bottom:1.4rem;left:.9rem;width:178px;
        text-align:center;padding:.75rem;
        border-radius:.85rem;
        background:rgba(212,235,194,.42);
        border:1px solid rgba(181,196,154,.38);
        font-size:.70rem;color:#758952;line-height:1.65;">
        Beauty Match v1.0<br>
        <span style="color:#B8C4A0;">Capstone Project 2026</span>
    </div>
    """, unsafe_allow_html=True)

# ─── Route Pages ──────────────────────────────────────────
if current_page == "home":
    from pages_bm.home import render
    render()
elif current_page == "skin":
    from pages_bm.skin_analysis import render
    render()
elif current_page == "results":
    from pages_bm.results import render
    render()
elif current_page == "foundation":
    from pages_bm.foundation import render
    render()
elif current_page == "about":
    from pages_bm.about_method import render
    render()
