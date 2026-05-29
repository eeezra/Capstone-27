import streamlit as st

st.set_page_config(
    page_title="ShadeMate",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# GLOBAL THEME
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Playfair+Display:wght@700;800&display=swap');

:root{

--bg:#FFF0F5;

--pink:#F9D1D9;
--hot:#F48ABD;
--accent:#FFA8D6;

--dusty:#E8C0C5;

--pistachio:#D4EBC2;
--mint:#CFE5B7;
--green:#BADF93;

--matcha:#838F58;
--olive:#758952;

--text:#2F2330;
--muted:#7B6472;

--border:rgba(248,168,214,.42);
}

/* =========================================================
BASE
========================================================= */

html, body, [class*="css"]{
    font-family:'Inter',sans-serif;
}

h1,h2,h3{
    font-family:'Playfair Display',serif;
    color:var(--text);
}

#MainMenu,
footer,
header{
    visibility:hidden;
}

.block-container{
    max-width:1480px;
    padding:2.3rem 2rem 4rem;
}

/* =========================================================
BACKGROUND
========================================================= */

.stApp{

background:
radial-gradient(
circle at 92% 6%,
rgba(255,168,214,.46),
transparent 23rem
),

radial-gradient(
circle at 9% 78%,
rgba(212,235,194,.62),
transparent 23rem
),

linear-gradient(
135deg,
#FFF0F5 0%,
#FFF8F6 48%,
#F4E2E4 100%
);

color:var(--text);
}

/* =========================================================
SIDEBAR
========================================================= */

section[data-testid="stSidebar"]{

background:
linear-gradient(
180deg,
rgba(255,240,245,.96),
rgba(255,240,245,.93) 68%,
rgba(212,235,194,.84)
);

border-right:1px solid rgba(232,192,197,.7);

box-shadow:
12px 0 35px rgba(232,192,197,.16);

width:210px !important;
}

section[data-testid="stSidebar"] > div{
    padding-top:1rem;
}

.sidebar-brand{

display:flex;
align-items:center;
gap:.85rem;

padding:.9rem .75rem 1.15rem;

border-bottom:
1px solid rgba(232,192,197,.72);

margin-bottom:1.2rem;
}

.logo-box{

width:42px;
height:42px;

border-radius:15px;

display:flex;
align-items:center;
justify-content:center;

background:
linear-gradient(
135deg,
var(--accent),
var(--olive)
);

box-shadow:
0 8px 18px rgba(117,137,82,.2);

color:white;
font-size:1.25rem;
}

.brand-name{

font-size:1.2rem;
font-weight:900;

line-height:1;
color:#34431d;
}

.brand-sub{

font-size:.72rem;

letter-spacing:.08em;
text-transform:uppercase;

font-weight:700;

color:var(--olive);
}

/* paksa sidebar selalu tampil */

section[data-testid="stSidebar"]{
    display:block !important;
    visibility:visible !important;
    min-width:210px !important;
}

[data-testid="stSidebarCollapsedControl"]{
    display:none !important;
}

[data-testid="collapsedControl"]{
    display:none !important;
}

/* =========================================================
NAVIGATION
========================================================= */

div[role="radiogroup"] label{

padding:.78rem .95rem !important;

border-radius:1rem !important;

margin:.25rem .15rem !important;

font-weight:800 !important;

color:#758952 !important;
}

div[role="radiogroup"] label:has(input:checked){

background:
linear-gradient(
90deg,
rgba(255,168,214,.82),
rgba(249,209,217,.70)
) !important;

color:#2F2330 !important;

box-shadow:
0 10px 20px rgba(248,138,189,.16);
}

div[role="radiogroup"] label > div:first-child{
display:none;
}

/* =========================================================
SIDEBAR FOOTER
========================================================= */

.sidebar-footer{

position:fixed;

bottom:2rem;
left:1.65rem;

width:180px;

padding:1rem;

text-align:center;

border-radius:1rem;

background:
rgba(212,235,194,.44);

border:
1px solid rgba(181,196,154,.4);

font-size:.75rem;

color:var(--olive);
}

/* =========================================================
BUTTONS
========================================================= */

.main .stButton > button{

border-radius:1rem !important;

font-weight:800 !important;

min-height:52px !important;

transition:all .2s ease !important;
}

.main .stButton > button:hover{

transform:translateY(-1px);

box-shadow:
0 12px 24px rgba(217,78,145,.18);
}

.main .stButton > button[kind="primary"]{

background:
linear-gradient(
135deg,
#F48ABD,
#E7569F
) !important;

color:white !important;

border:none !important;
}

.main .stButton > button[kind="secondary"]{

background:
rgba(255,255,255,.72) !important;

border:
1.5px solid rgba(117,137,82,.45) !important;

color:#758952 !important;
}

/* =========================================================
COMMON CARDS
========================================================= */

.custom-card,
.metric-card,
.product-card{

background:
rgba(255,255,255,.78);

border:1px solid var(--border);

border-radius:1.35rem;

box-shadow:
0 16px 36px rgba(200,107,133,.09);

backdrop-filter:blur(16px);
}

.page-title{

font-size:clamp(2.2rem,3vw,3.4rem);

margin-bottom:.35rem;
}

.page-subtitle{

color:var(--muted);

font-size:1rem;

margin-bottom:2rem;
}

/* =========================================================
LOCK SIDEBAR
========================================================= */

/* Hilangkan tombol collapse sidebar */
[data-testid="collapsedControl"]{
    display:none !important;
}

/* Hilangkan tombol toggle di header */
button[kind="header"]{
    display:none !important;
}

/* Pastikan sidebar tetap tampil */
section[data-testid="stSidebar"]{
    transform:none !important;
    visibility:visible !important;
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

# =========================================================
# SESSION STATE
# =========================================================

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = None

if "uploaded_image" not in st.session_state:
    st.session_state.uploaded_image = None

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("""
    <div class="sidebar-brand">
        <div class="logo-box">✿</div>

        <div>
            <div class="brand-name">
                Beauty Match
            </div>

            <div class="brand-sub">
                Foundation Advisor
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    pages = [
        "Home",
        "Skin Analysis",
        "Results",
        "Foundation",
        "About Method"
    ]

    icons = {
        "Home":"🏠",
        "Skin Analysis":"📷",
        "Results":"📊",
        "Foundation":"✨",
        "About Method":"📖"
    }

    selected = st.radio(
        "",
        pages,
        index=pages.index(st.session_state.page),
        format_func=lambda x: f"{icons[x]}  {x}"
    )

    if selected != st.session_state.page:
        st.session_state.page = selected
        st.rerun()

    st.markdown("""
    <div class="sidebar-footer">
        Beauty Match v1.0<br>
        Capstone Project 2026
    </div>
    """, unsafe_allow_html=True)


from pages_bm.home import render_home
from pages_bm.skin_analysis import render_skin_analysis
from pages_bm.results import render_results
from pages_bm.foundation import render_foundation
from pages_bm.about_method import render_about_method

page = st.session_state.page

if page == "Home":
    render_home()

elif page == "Skin Analysis":
    render_skin_analysis()

elif page == "Results":
    render_results()

elif page == "Foundation":
    render_foundation()

elif page == "About Method":
    render_about_method()
