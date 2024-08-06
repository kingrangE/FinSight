import streamlit as st
import pandas as pd

def display_news():
    st.title('오늘의 뉴스')
    news_list = [
        ("뉴스 제목 1", "#"),
        ("뉴스 제목 2", "#"),
        ("뉴스 제목 3", "#"),
        ("뉴스 제목 4", "#"),
        ("뉴스 제목 5", "#"),
        ("뉴스 제목 6", "#"),
        ("뉴스 제목 7", "#"),
        ("뉴스 제목 8", "#"),
        ("뉴스 제목 9", "#"),
        ("뉴스 제목 10", "#"),
    ]

    for title, link in news_list[:5]:
        st.markdown(f"[{title}]({link})")

    if st.button('More'):
        with st.expander("전체 뉴스 보기"):
            for title, link in news_list[5:]:
                st.markdown(f"[{title}]({link})")

def display_stocks():
    st.title('오늘 매수/매도 추천 주식')
    col1, col2 = st.columns(2)

    with col1:
        st.header('오늘 매수 추천 주식')
        for i in range(5):
            st.write(f'매수 추천 주식 {i+1}')
        if st.button('More 매수 주식'):
            with st.expander("전체 매수 추천 주식 보기"):
                for i in range(10):
                    st.write(f'매수 추천 주식 {i+6}')

    with col2:
        st.header('오늘 매도 추천 주식')
        for i in range(5):
            st.write(f'매도 추천 주식 {i+1}')
        if st.button('More 매도 주식'):
            with st.expander("전체 매도 추천 주식 보기"):
                for i in range(10):
                    st.write(f'매도 추천 주식 {i+6}')

def display_chat():
    st.title('채팅')
    st.subheader('채팅 기록')

    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    if 'chat_input' not in st.session_state:
        st.session_state['chat_input'] = ''

    for message in st.session_state['chat_history']:
        st.write(message)
    
    user_message = st.text_input('채팅 입력', key='chat_input')
    if st.button('전송'):
        if st.session_state['chat_input']:
            st.session_state['chat_history'].append(st.session_state['chat_input'])
            st.session_state['chat_input'] = ''  # 입력란 초기화
            st.experimental_rerun()  # 상태를 업데이트하고 UI를 다시 그립니다

def main():
    display_news()
    display_stocks()
    display_chat()
