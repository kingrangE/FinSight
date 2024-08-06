import streamlit as st

def main():
    st.title('기사 내용 요약 및 매수 추천')
    article_content = st.text_area('기사 내용 입력')
    
    if st.button('요약 및 추천'):
        st.subheader('요약 및 추천 결과')
        st.write('요약 및 추천 내용 예시')
