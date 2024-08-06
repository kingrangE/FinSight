import streamlit as st

def main():
    st.title('로그인 및 회원가입')
    login_option = st.radio('로그인 방식 선택', ['카카오톡', '구글', '깃헙'])
    
    if login_option == '카카오톡':
        st.write('카카오톡 로그인')
    elif login_option == '구글':
        st.write('구글 로그인')
    elif login_option == '깃헙':
        st.write('깃헙 로그인')
    
    if st.button('회원가입'):
        st.write("회원가입 기능 예시")
