import streamlit as st

# ======================================================
# PAGE CONFIG
# ======================================================

st.set_page_config(
    page_title="Beauty Match",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ======================================================
# SESSION STATE
# ======================================================

if "page" not in st.session_state:
    st.session_state.page = "home"

# ======================================================
# GLOBAL CSS
# ======================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Playfair+Display:wght@700;800&display=swap');

html, body, [class*="css"]{
    font-family:'Inter', sans-serif;
}

/* ======================================================
MAIN BACKGROUND
====================================================== */

.stApp{
    background:
        radial-gradient(circle at 90% 8%, rgba(255,192,220,.22), transparent 18rem),
        radial-gradient(circle at 8% 82%, rgba(212,235,194,.28), transparent 20rem),
        linear-gradient(
            135deg,
            #FFF7FA 0%,
            #FFF9F8 50%,
            #FFF4F7 100%
        );

    overflow-x:hidden;
}

/* ======================================================
STREAMLIT CLEANUP
====================================================== */

#MainMenu,
footer,
header{
    visibility:hidden;
}

[data-testid="collapsedControl"]{
    display:none;
}

/* ======================================================
MAIN CONTAINER
====================================================== */

.main .block-container{
    max-width:1050px;
    padding-top:.7rem;
    padding-bottom:2rem;
}

/* ======================================================
SIDEBAR
====================================================== */

[data-testid="stSidebar"]{
    background:
        linear-gradient(
            180deg,
            rgba(255,240,245,.96) 0%,
            rgba(255,240,245,.93) 60%,
            rgba(219,236,195,.84) 100%
        );

    border-right:1px solid rgba(240,190,210,.55);
}

[data-testid="stSidebar"] .block-container{
    padding-top:1rem;
    padding-left:.8rem;
    padding-right:.8rem;
}

/* ======================================================
SIDEBAR BRAND
====================================================== */

.brand-wrap{
    display:flex;
    align-items:center;
    gap:12px;

    padding-bottom:1rem;
    margin-bottom:1rem;

    border-bottom:1px solid rgba(240,190,210,.4);
}

.brand-icon{
    width:38px;
    height:38px;

    border-radius:12px;

    display:flex;
    align-items:center;
    justify-content:center;

    background:linear-gradient(
        135deg,
        #F7A8CC,
        #95A56A
    );

    color:white;
    font-size:1rem;
    font-weight:700;
}

.brand-small{
    font-size:.58rem;
    font-weight:800;
    letter-spacing:.08em;
    text-transform:uppercase;

    color:#7D8D5D;
}

.brand-big{
    font-size:1rem;
    font-weight:800;

    color:#2F2330;
}

/* ======================================================
SIDEBAR BUTTONS
====================================================== */

[data-testid="stSidebar"] .stButton{
    margin-bottom:.35rem;
}

[data-testid="stSidebar"] .stButton > button{

    width:100%;

    height:42px;

    border:none;

    border-radius:12px;

    background:transparent;

    color:#72844F;

    font-size:.9rem;
    font-weight:600;

    text-align:left;

    justify-content:flex-start;

    transition:all .15s ease;
}

[data-testid="stSidebar"] .stButton > button:hover{

    background:rgba(255,168,214,.18);

    color:#D94E91;
}

/* ======================================================
MAIN BUTTONS
====================================================== */

.main .stButton > button{

    border-radius:999px;

    height:48px;

    font-weight:700;

    font-size:.95rem;

    border:none;
}

.main .stButton > button[kind="primary"]{

    background:linear-gradient(
        135deg,
        #F58BBF,
        #D94E91
    );

    color:white;
}

.main .stButton > button[kind="secondary"]{

    background:white;

    border:1px solid rgba(125,141,93,.35);

    color:#72844F;
}

/* ======================================================
SCROLLBAR
====================================================== */

::-webkit-scrollbar{
    width:6px;
}

::-webkit-scrollbar-thumb{
    background:#F3A6C7;
    border-radius:999px;
}

</style>
""", unsafe_allow_html=True)

# ======================================================
# SIDEBAR
# ======================================================

with st.sidebar:

    st.markdown("""
    <div class="brand-wrap">

        <div class="brand-icon">
            ✿
        </div>

        <div>
            <div class="brand-small">
                CAPSTONE 27
            </div>

            <div class="brand-big">
                Beauty Match
            </div>
        </div>

    </div>
    """, unsafe_allow_html=True)

    navs = [
        ("home", "⌂ Home"),
        ("skin", "◫ Skin Analysis"),
        ("results", "▥ Results"),
        ("foundation", "✧ Foundation"),
        ("about", "☰ About Method"),
    ]

    for page_id, label in navs:

        if st.button(
            label,
            key=f"nav_{page_id}",
            use_container_width=True
        ):
            st.session_state.page = page_id
            st.rerun()

    st.markdown("<div style='height:3rem'></div>", unsafe_allow_html=True)

    st.markdown("""
    <div style="
        background:rgba(212,235,194,.4);
        padding:1rem;
        border-radius:16px;
        font-size:.72rem;
        color:#7D8D5D;
        text-align:center;
        line-height:1.6;
    ">
        Beauty Match v1.0<br>
        <span style="opacity:.7">
            Capstone Project 2026
        </span>
    </div>
    """, unsafe_allow_html=True)

# ======================================================
# ROUTING
# ======================================================

page = st.session_state.page

if page == "home":

    from pages_bm.home import render
    render()

elif page == "skin":

    st.title("Skin Analysis")

elif page == "results":

    st.title("Results")

elif page == "foundation":

    st.title("Foundation")

elif page == "about":

    st.title("About Method")
