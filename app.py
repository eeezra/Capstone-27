import streamlit as st

st.set_page_config(
    page_title="Beauty Match",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Global CSS ───────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

* { font-family: 'Inter', sans-serif !important; }

/* Force light background everywhere */
.stApp {
    background-color: #fff8fa !important;
}
.main {
    background-color: #fff8fa !important;
}
.main .block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1100px;
    background-color: #fff8fa !important;
}

/* Hide default streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #fff0f5 !important;
    border-right: 1px solid #f9d0de;
    min-width: 210px !important;
    max-width: 210px !important;
}
[data-testid="stSidebar"] > div:first-child {
    background-color: #fff0f5 !important;
}
[data-testid="stSidebar"] .block-container {
    padding: 1.5rem 1rem;
}

/* Hide radio circle indicators */
div[data-testid="stSidebar"] .stRadio > div {
    flex-direction: column;
    gap: 2px;
}
div[data-testid="stSidebar"] .stRadio [role="radiogroup"] {
    gap: 2px;
}
/* Hide the actual radio dot */
div[data-testid="stSidebar"] .stRadio input[type="radio"] {
    display: none !important;
}
div[data-testid="stSidebar"] .stRadio [data-testid="stMarkdownContainer"] {
    display: none !important;
}
/* Style each radio label as nav item */
div[data-testid="stSidebar"] .stRadio label {
    background: transparent;
    border-radius: 8px;
    padding: 9px 14px;
    cursor: pointer;
    font-size: 14px;
    font-weight: 500;
    color: #666;
    transition: all 0.18s;
    display: flex !important;
    align-items: center;
    width: 100%;
    border: none;
    margin: 1px 0;
}
div[data-testid="stSidebar"] .stRadio label:hover {
    background: #fde8ef;
    color: #c0587e;
}
div[data-testid="stSidebar"] .stRadio label[data-baseweb="radio"]:has(input:checked),
div[data-testid="stSidebar"] .stRadio label[aria-checked="true"] {
    background: #fad4e0;
    color: #a8405e;
    font-weight: 700;
}

/* Global buttons */
.stButton > button {
    border-radius: 999px !important;
    font-weight: 600 !important;
    transition: all 0.2s !important;
    border: none !important;
}
.stButton > button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 14px rgba(192,88,126,0.25) !important;
}
/* Primary button */
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #e8607a, #c0587e) !important;
    color: white !important;
}
/* Secondary button */
.stButton > button[kind="secondary"] {
    background: white !important;
    color: #333 !important;
    border: 1.5px solid #e0c0cc !important;
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    background: #fff0f5;
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
    color: #c0587e !important;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08) !important;
}
.stTabs [data-baseweb="tab-highlight"] {
    display: none !important;
}
.stTabs [data-baseweb="tab-border"] {
    display: none !important;
}

/* Selectbox & inputs */
.stSelectbox > div > div {
    border-radius: 10px !important;
    border-color: #f0d0dc !important;
    background: white !important;
}
.stFileUploader {
    border-radius: 14px !important;
}

/* Dataframe */
.stDataFrame {
    border-radius: 12px !important;
    overflow: hidden !important;
}

/* Spinner */
.stSpinner > div {
    border-top-color: #c0587e !important;
}

/* Expander */
.streamlit-expanderHeader {
    background: white !important;
    border-radius: 12px !important;
    border: 1px solid #f0d0dc !important;
    font-weight: 600 !important;
    color: #555 !important;
}

/* Scrollbar */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: #fff0f5; }
::-webkit-scrollbar-thumb { background: #f4a0b8; border-radius: 999px; }
</style>
""", unsafe_allow_html=True)

# ─── Sidebar Nav ──────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="display:flex;align-items:center;gap:10px;margin-bottom:24px;">
        <div style="
            width:36px;height:36px;border-radius:50%;
            background:linear-gradient(135deg,#f4a0b8,#c9a0dc);
            display:flex;align-items:center;justify-content:center;
            font-size:16px;">🎨</div>
        <div>
            <div style="font-weight:700;font-size:15px;color:#2d2d2d;">Beauty Match</div>
            <div style="font-size:11px;color:#999;">Foundation Advisor</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    nav_icons = {
        "🏠  Home": "home",
        "📷  Skin Analysis": "skin",
        "📊  Results": "results",
        "💄  Foundation": "foundation",
        "📖  About Method": "about",
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

    st.markdown("""
    <div style="
        position:fixed;bottom:20px;left:0;width:200px;
        padding:10px 16px;font-size:11px;color:#aaa;">
        Beauty Match v1.0<br>
        <span style="color:#bbb;">Capstone Project 2026</span>
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
