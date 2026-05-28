import streamlit as st

st.set_page_config(
    page_title="ShadeMate",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
/* Paksa sidebar selalu terbuka dan sembunyikan tombol toggle */
[data-testid="collapsedControl"] { display: none !important; }
section[data-testid="stSidebar"] { 
    transform: none !important;
    width: 210px !important;
    min-width: 210px !important;
}
</style>
""", unsafe_allow_html=True)

# ─── Global CSS ───────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Playfair+Display:wght@700;800&display=swap');

* { font-family: 'Inter', sans-serif !important; }

/* ── Background ── */
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
    padding-top: 1.5rem;
    padding-bottom: 3rem;
    max-width: 1200px;
}

/* ── Hide streamlit chrome ── */
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
    min-width: 210px !important;
    max-width: 210px !important;
}
section[data-testid="stSidebar"] > div:first-child {
    background: transparent !important;
    padding-top: 1rem !important;
}
section[data-testid="stSidebar"] .block-container {
    padding: 1.2rem 1rem !important;
    background: transparent !important;
}

/* ── Sidebar radio nav ── */
section[data-testid="stSidebar"] .stRadio > div {
    flex-direction: column;
    gap: 2px;
}
section[data-testid="stSidebar"] .stRadio [role="radiogroup"] {
    gap: 2px;
}
section[data-testid="stSidebar"] .stRadio input[type="radio"] {
    display: none !important;
}
section[data-testid="stSidebar"] .stRadio [data-testid="stMarkdownContainer"] {
    display: none !important;
}
section[data-testid="stSidebar"] .stRadio label {
    background: transparent !important;
    border-radius: 12px !important;
    padding: 10px 14px !important;
    cursor: pointer;
    font-size: 14px;
    font-weight: 700 !important;
    color: #758952 !important;
    transition: all 0.18s;
    display: flex !important;
    align-items: center;
    width: 100%;
    border: none !important;
    margin: 1px 0;
}
section[data-testid="stSidebar"] .stRadio label:hover {
    background: rgba(255,168,214,.25) !important;
    color: #D94E91 !important;
}
section[data-testid="stSidebar"] .stRadio label:has(input:checked) {
    background: linear-gradient(
        90deg,
        rgba(255,168,214,.82),
        rgba(249,209,217,.70)
    ) !important;
    color: #2F2330 !important;
    box-shadow: 0 8px 18px rgba(248,138,189,.16) !important;
}

/* ── Global buttons ── */
.stButton > button {
    border-radius: 999px !important;
    font-weight: 700 !important;
    transition: all 0.2s !important;
    min-height: 46px !important;
}
.stButton > button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 18px rgba(192,88,126,.25) !important;
}
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #F48ABD, #D94E91) !important;
    color: white !important;
    border: none !important;
    box-shadow: 0 10px 22px rgba(217,78,145,.22) !important;
}
.stButton > button[kind="secondary"] {
    background: rgba(255,255,255,.75) !important;
    color: #758952 !important;
    border: 1.5px solid rgba(117,137,82,.55) !important;
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
    padding: 6px 20px !important;
    font-weight: 600 !important;
    font-size: 14px !important;
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

/* ── File uploader ── */
.stFileUploader {
    border-radius: 14px !important;
}

/* ── Dataframe ── */
.stDataFrame {
    border-radius: 12px !important;
    overflow: hidden !important;
}

/* ── Spinner ── */
.stSpinner > div {
    border-top-color: #D94E91 !important;
}

/* ── Expander ── */
.streamlit-expanderHeader {
    background: rgba(255,255,255,.75) !important;
    border-radius: 12px !important;
    border: 1px solid rgba(248,168,214,.40) !important;
    font-weight: 600 !important;
    color: #555 !important;
}

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: #FFF0F5; }
::-webkit-scrollbar-thumb {
    background: #F4A0B8;
    border-radius: 999px;
}
</style>
""", unsafe_allow_html=True)

# ─── Sidebar ──────────────────────────────────────────────
with st.sidebar:
    # Logo + brand
    st.markdown("""
    <div style="
        display:flex;align-items:center;gap:10px;
        padding:.9rem .5rem 1.1rem;
        border-bottom:1px solid rgba(232,192,197,.65);
        margin-bottom:1.2rem;">
        <div style="
            width:42px;height:42px;border-radius:15px;
            background:linear-gradient(135deg,#FFA8D6,#838F58);
            display:flex;align-items:center;justify-content:center;
            font-size:1.2rem;color:white;
            box-shadow:0 8px 18px rgba(117,137,82,.22);">✿</div>
        <div>
            <div style="font-size:.70rem;font-weight:700;
                letter-spacing:.08em;text-transform:uppercase;
                color:#758952;">Capstone 27</div>
            <div style="font-weight:900;font-size:1.1rem;
                color:#2F2330;line-height:1.1;">Beauty Match</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    nav_icons = {
        "⌂  Home": "home",
        "▣  Skin Analysis": "skin",
        "▥  Results": "results",
        "✧  Foundation": "foundation",
        "▤  About Method": "about",
    }

    # Sync navigasi dari tombol — harus SEBELUM st.radio
    if "nav_target" in st.session_state:
        target = st.session_state.pop("nav_target")
        reverse = {v: k for k, v in nav_icons.items()}
        if target in reverse:
            st.session_state["main_nav"] = reverse[target]

    page_selected = st.radio(
        "nav",
        list(nav_icons.keys()),
        label_visibility="collapsed",
        key="main_nav",
    )
    page = nav_icons[page_selected]

    # Footer
    st.markdown("""
    <div style="
        position:fixed;bottom:1.8rem;left:1.4rem;width:178px;
        text-align:center;padding:1rem .8rem;
        border-radius:1rem;
        background:rgba(212,235,194,.42);
        border:1px solid rgba(181,196,154,.40);
        font-size:.76rem;color:#758952;line-height:1.6;">
        Capstone Project 2026<br>
        <span style="color:#B8C4A0;">Beauty Tech Research Lab</span>
    </div>
    """, unsafe_allow_html=True)

# ─── Route Pages ──────────────────────────────────────────
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
