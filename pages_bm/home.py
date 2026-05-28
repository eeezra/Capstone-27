import streamlit as st

st.set_page_config(
    page_title="Beauty Match",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =========================================================
# GLOBAL CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Playfair+Display:wght@700;800&display=swap');

*{
    font-family:'Inter',sans-serif !important;
}

html, body, [class*="css"]{
    color:#2F2330;
}

/* =========================================================
MAIN APP
========================================================= */

.stApp{
    background:
        radial-gradient(circle at 90% 8%, rgba(255,192,220,.28), transparent 18rem),
        radial-gradient(circle at 8% 82%, rgba(212,235,194,.35), transparent 20rem),
        linear-gradient(
            135deg,
            #FFF5F8 0%,
            #FFF8F7 50%,
            #FFF3F6 100%
        ) !important;

    overflow-x:hidden;
}

/* floating blobs */

.stApp::before{
    content:"";
    position:fixed;
    width:320px;
    height:320px;
    border-radius:50%;
    background:rgba(212,235,194,.28);
    left:-120px;
    bottom:40px;
    filter:blur(8px);
    z-index:-1;
}

.stApp::after{
    content:"";
    position:fixed;
    width:240px;
    height:240px;
    border-radius:50%;
    background:rgba(255,192,220,.22);
    right:-80px;
    top:-40px;
    filter:blur(8px);
    z-index:-1;
}

/* =========================================================
STREAMLIT CLEANUP
========================================================= */

#MainMenu,
footer,
header{
    visibility:hidden;
}

.stDeployButton{
    display:none;
}

[data-testid="collapsedControl"]{
    display:none !important;
}

section.main > div{
    padding-top:0 !important;
}

/* =========================================================
BLOCK CONTAINER
========================================================= */

.main .block-container{
    max-width:980px !important;

    padding-top:.5rem !important;
    padding-bottom:2rem !important;

    margin:auto !important;
}

/* =========================================================
SIDEBAR
========================================================= */

section[data-testid="stSidebar"]{
    width:170px !important;
    min-width:170px !important;
    max-width:170px !important;

    background:linear-gradient(
        180deg,
        rgba(255,240,245,.96) 0%,
        rgba(255,240,245,.93) 65%,
        rgba(212,235,194,.82) 100%
    ) !important;

    border-right:1px solid rgba(232,192,197,.55);

    box-shadow:10px 0 30px rgba(232,192,197,.12);
}

section[data-testid="stSidebar"] .block-container{
    padding:.8rem .7rem !important;
}

/* sidebar header */

.sidebar-brand{
    display:flex;
    align-items:center;
    gap:10px;

    padding:.5rem .2rem .9rem;

    border-bottom:1px solid rgba(232,192,197,.45);

    margin-bottom:.7rem;
}

.brand-icon{
    width:34px;
    height:34px;

    border-radius:11px;

    background:linear-gradient(
        135deg,
        #FFA8D6,
        #838F58
    );

    display:flex;
    align-items:center;
    justify-content:center;

    color:white;
    font-size:.95rem;
    font-weight:700;
}

.brand-small{
    font-size:.58rem;
    font-weight:800;
    letter-spacing:.08em;
    text-transform:uppercase;

    color:#758952;
}

.brand-big{
    font-size:.92rem;
    font-weight:900;

    color:#2F2330;
}

/* sidebar buttons */

section[data-testid="stSidebar"] .stButton{
    margin:0 !important;
    padding:0 !important;
}

section[data-testid="stSidebar"] .stButton > button{

    width:100% !important;

    height:36px !important;

    border:none !important;

    background:transparent !important;

    border-radius:10px !important;

    display:flex !important;
    align-items:center !important;
    justify-content:flex-start !important;

    padding:0 .7rem !important;

    color:#6F8150 !important;

    font-size:.82rem !important;
    font-weight:600 !important;

    box-shadow:none !important;

    transition:all .15s ease !important;
}

section[data-testid="stSidebar"] .stButton > button:hover{
    background:rgba(255,168,214,.18) !important;
    color:#D94E91 !important;
}

.active-nav .stButton > button{
    background:linear-gradient(
        90deg,
        rgba(255,168,214,.85),
        rgba(249,209,217,.62)
    ) !important;

    color:#2F2330 !important;

    font-weight:700 !important;
}

/* sidebar footer */

.sidebar-footer{
    position:fixed;

    left:.8rem;
    bottom:1rem;

    width:145px;

    padding:.75rem;

    border-radius:14px;

    background:rgba(212,235,194,.42);

    border:1px solid rgba(181,196,154,.30);

    text-align:center;

    font-size:.66rem;
    line-height:1.6;

    color:#758952;
}

/* =========================================================
GLOBAL BUTTONS
========================================================= */

.main .stButton > button{

    border-radius:999px !important;

    font-weight:700 !important;

    height:46px !important;
    min-height:46px !important;

    font-size:.92rem !important;

    transition:all .18s ease !important;
}

.main .stButton > button:hover{
    transform:translateY(-1px);

    box-shadow:0 8px 20px rgba(217,78,145,.16) !important;
}

.main .stButton > button[kind="primary"]{

    background:linear-gradient(
        135deg,
        #F48ABD,
        #D94E91
    ) !important;

    color:white !important;

    border:none !important;
}

.main .stButton > button[kind="secondary"]{

    background:rgba(255,255,255,.72) !important;

    border:1.5px solid rgba(117,137,82,.45) !important;

    color:#758952 !important;
}

/* =========================================================
SCROLLBAR
========================================================= */

::-webkit-scrollbar{
    width:5px;
}

::-webkit-scrollbar-track{
    background:#FFF0F5;
}

::-webkit-scrollbar-thumb{
    background:#F4A0B8;
    border-radius:999px;
}

</style>
""", unsafe_allow_html=True)
