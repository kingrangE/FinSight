import streamlit as st
import pandas as pd

def main():
    st.title('오늘의 뉴스')
    
    # 뉴스 목록
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
        # 더 많은 뉴스 제목 추가
    ]
    
    # 상위 5개 뉴스만 표시
    for title, link in news_list[:5]:
        st.markdown(f"<a style='font-size:20px; color:white; text-decoration:none;' href='{link}'>{title}</a>", unsafe_allow_html=True)
    
    # 더보기 버튼
    if st.button('More', key='more_news'):
        with st.expander("전체 뉴스 보기", expanded=True):
            news_html = "<div style='height: 200px; overflow-y: scroll;'>"
            for title, link in news_list[5:]:
                news_html += f"<a style='font-size:20px; color:white; text-decoration:none;' href='{link}'>{title}</a><br>"
            news_html += "</div>"
            st.markdown(news_html, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.header('오늘 매수 추천 주식')
        for i in range(5):
            st.markdown(f"<span style='font-size:20px; color:white;'>{f'매수 추천 주식 {i+1}'}</span>", unsafe_allow_html=True)
        if st.button('More', key='more_buy_stocks'):
            with st.expander("전체 매수 추천 주식 보기", expanded=True):
                stocks_html = "<div style='height: 200px; overflow-y: scroll;'>"
                for i in range(10):
                    stocks_html += f"<span style='font-size:20px; color:white;'>{f'매수 추천 주식 {i+6}'}</span><br>"
                stocks_html += "</div>"
                st.markdown(stocks_html, unsafe_allow_html=True)

    with col2:
        st.header('오늘 매도 추천 주식')
        for i in range(5):
            st.markdown(f"<span style='font-size:20px; color:white;'>{f'매도 추천 주식 {i+1}'}</span>", unsafe_allow_html=True)
        if st.button('More', key='more_sell_stocks'):
            with st.expander("전체 매도 추천 주식 보기", expanded=True):
                stocks_html = "<div style='height: 200px; overflow-y: scroll;'>"
                for i in range(10):
                    stocks_html += f"<span style='font-size:20px; color:white;'>{f'매도 추천 주식 {i+6}'}</span><br>"
                stocks_html += "</div>"
                st.markdown(stocks_html, unsafe_allow_html=True)

    # # 채팅 기능
    # st.title('채팅')
    # st.subheader('채팅 기록')

    # if 'chat_history' not in st.session_state:
    #     st.session_state['chat_history'] = []

    # for message in st.session_state['chat_history']:
    #     st.write(message)
    
    # user_message = st.text_input('채팅 입력', key='chat_input')
    # if st.button('전송', key='send_button'):
    #     if st.session_state['chat_input']:
    #         st.session_state['chat_history'].append(st.session_state['chat_input'])
    #         st.session_state['chat_input'] = ''  # 입력란 초기화
    #         st.experimental_rerun()  # 상태를 업데이트하고 UI를 다시 그립니다

if __name__ == "__main__":
    main()
