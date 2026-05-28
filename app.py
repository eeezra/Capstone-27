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
    width: 210px !important;
    min-width: 210px !important;
    max-width: 210px !important;
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

/* ── Sidebar background ── */
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
    padding: 0.8rem 0.7rem !important;
    background: transparent !important;
}

/* ── Nav buttons sidebar — compact & flat ── */
section[data-testid="stSidebar"] .stButton {
    margin: 0 !important;
    padding: 0 !important;
}
section[data-testid="stSidebar"] .stButton > button {
    width: 100% !important;
    text-align: left !important;
    justify-content: flex-start !important;
    background: transparent !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 7px 10px !important;
    font-size: 13px !important;
    font-weight: 600 !important;
    color: #758952 !important;
    box-shadow: none !important;
    min-height: unset !important;
    height: 34px !important;
    line-height: 1 !important;
    margin: 0 !important;
    transition: background 0.15s, color 0.15s !important;
    transform: none !important;
    letter-spacing: 0 !important;
}
section[data-testid="stSidebar"] .stButton > button:hover {
    background: rgba(255,168,214,.28) !important;
    color: #D94E91 !important;
    transform: none !important;
    box-shadow: none !important;
}
section[data-testid="stSidebar"] .nav-active .stButton > button {
    background: linear-gradient(
        90deg,
        rgba(255,168,214,.80),
        rgba(249,209,217,.65)
    ) !important;
    color: #2F2330 !important;
    font-weight: 700 !important;
    box-shadow: none !important;
}

/* ── Global buttons (konten utama) ── */
.main .stButton > button {
    border-radius: 999px !important;
    font-weight: 700 !important;
    transition: all 0.2s !important;
    min-height: 44px !important;
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
.stTabs [data-baseweb="tab-border"] {
    display: none !important;
}

/* ── Selectbox ── */
.stSelectbox > div > div {
    border-radius: 10px !important;
    border-color: rgba(248,168,214,.50) !important;
    background: rgba(255,255,255,.80) !important;
}

/* ── Misc ── */
.stFileUploader { border-radius: 14px !important; }
.stDataFrame { border-radius: 12px !important; overflow: hidden !important; }
.stSpinner > div { border-top-color: #D94E91 !important; }
.streamlit-expanderHeader {
    background: rgba(255,255,255,.75) !important;
    border-radius: 12px !important;
    border: 1px solid rgba(248,168,214,.40) !important;
    font-weight: 600 !important;
}

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: #FFF0F5; }
::-webkit-scrollbar-thumb { background: #F4A0B8; border-radius: 999px; }
</style>
""", unsafe_allow_html=True)

# ─── Sidebar ──────────────────────────────────────────────
with st.sidebar:

    st.markdown("""
    <div style="
        display:flex;align-items:center;gap:9px;
        padding:.6rem .3rem .8rem;
        border-bottom:1px solid rgba(232,192,197,.55);
        margin-bottom:.6rem;">
        <div style="
            width:38px;height:38px;border-radius:12px;flex-shrink:0;
            background:linear-gradient(135deg,#FFA8D6,#838F58);
            display:flex;align-items:center;justify-content:center;
            font-size:1.1rem;color:white;
            box-shadow:0 6px 14px rgba(117,137,82,.20);">✿</div>
        <div>
            <div style="font-size:.65rem;font-weight:700;
                letter-spacing:.08em;text-transform:uppercase;
                color:#758952;line-height:1.2;">Capstone 27</div>
            <div style="font-weight:900;font-size:.95rem;
                color:#2F2330;line-height:1.2;">Beauty Match</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    if "page" not in st.session_state:
        st.session_state["page"] = "home"

    if "nav_target" in st.session_state:
        st.session_state["page"] = st.session_state.pop("nav_target")

    nav_items = [
        ("home",       "⌂",  "Home"),
        ("skin",       "▣",  "Skin Analysis"),
        ("results",    "▥",  "Results"),
        ("foundation", "✧",  "Foundation"),
        ("about",      "▤",  "About Method"),
    ]

    for page_id, icon, label in nav_items:
        is_active = st.session_state["page"] == page_id
        if is_active:
            st.markdown('<div class="nav-active">', unsafe_allow_html=True)
        if st.button(
            f"{icon}  {label}",
            key=f"nav_{page_id}",
            use_container_width=True,
        ):
            st.session_state["page"] = page_id
            st.rerun()
        if is_active:
            st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
    <div style="
        position:fixed;bottom:1.5rem;left:1rem;width:178px;
        text-align:center;padding:.8rem;
        border-radius:.9rem;
        background:rgba(212,235,194,.42);
        border:1px solid rgba(181,196,154,.38);
        font-size:.72rem;color:#758952;line-height:1.6;">
        Capstone Project 2026<br>
        <span style="color:#B8C4A0;">Beauty Tech Research Lab</span>
    </div>
    """, unsafe_allow_html=True)

# ─── Route Pages ──────────────────────────────────────────
page = st.session_state.get("page", "home")

if page == "home":
    from pages_bm.home import render
    render()
elif page == "skin":
    from pages_bm.skin_analysis import render
    render()
elif page == "results":
    from pages_bm.results import render
    render()
elif page == "foundation":
    from pages_bm.foundation import render
    render()
elif page == "about":
    from pages_bm.about_method import render
    render()
