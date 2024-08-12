import streamlit as st
from src import main_page, trade_api_page, summary_recommendation_page, auth_page

st.sidebar.title("FinSight")

# HTML을 사용하여 여백 추가
st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.markdown("<br>", unsafe_allow_html=True)

page = st.sidebar.selectbox(
    "  페이지 선택",
    ["메인화면", "자동 매매", "기사 요약 및 추천", "로그인/회원가입"]
)

if page == "메인화면":
    main_page.main()
elif page == "자동 매매":
    trade_api_page.main()
elif page == "기사 요약 및 추천":
    summary_recommendation_page.main()
elif page == "로그인/회원가입":
    auth_page.main()
