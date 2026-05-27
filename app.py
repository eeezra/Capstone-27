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

#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }

.main .block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1100px;
}

[data-testid="stSidebar"] {
    background: #fff5f7 !important;
    border-right: 1px solid #f0d6de;
    min-width: 200px !important;
    max-width: 200px !important;
}
[data-testid="stSidebar"] .block-container {
    padding: 1.5rem 1rem;
}

div[data-testid="stSidebar"] .stRadio > div {
    flex-direction: column;
    gap: 4px;
}
div[data-testid="stSidebar"] .stRadio label {
    background: transparent;
    border-radius: 8px;
    padding: 8px 12px;
    cursor: pointer;
    font-size: 14px;
    color: #555;
    transition: all 0.2s;
    display: block;
    width: 100%;
}
div[data-testid="stSidebar"] .stRadio label:hover {
    background: #fde8ef;
    color: #c0587e;
}
div[data-testid="stSidebar"] .stRadio [aria-checked="true"] + div label,
div[data-testid="stSidebar"] .stRadio label[data-selected="true"] {
    background: #f9ccd8;
    color: #b5446e;
    font-weight: 600;
}

.stButton > button {
    border-radius: 999px;
    font-weight: 600;
    transition: all 0.2s;
}
.stButton > button:hover {
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

.bm-card {
    background: white;
    border-radius: 16px;
    padding: 24px;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06);
    border: 1px solid #f0e0e8;
    height: 100%;
}

.bm-pill {
    display: inline-block;
    padding: 3px 10px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 600;
    margin: 2px;
}
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
