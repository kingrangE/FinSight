import streamlit as st
from src import main_page, trade_api_page, summary_recommendation_page, auth_page

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["홈", "자동 매매 API", "기사 요약 및 추천", "로그인/회원가입"])

if page == "홈":
    main_page.main()
elif page == "자동 매매 API":
    trade_api_page.main()
elif page == "기사 요약 및 추천":
    summary_recommendation_page.main()
elif page == "로그인/회원가입":
    auth_page.main()
