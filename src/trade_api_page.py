import streamlit as st

def main():
    st.title('자동 매매 API 연결')
    
    api_option = st.selectbox('API 선택', ['Binance', '증권사'])
    
    if api_option == 'Binance':
        st.text_input('API Key')
        st.text_input('API Secret')
    elif api_option == '증권사':
        broker_option = st.selectbox('증권사 선택', ['KB', '영웅문'])
    
    st.subheader('매수/매도 기록')
    st.write('매수/매도 기록 테이블 예시')
    
    st.metric('총 수익', '예시 금액')
