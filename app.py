import streamlit as st
import pandas as pd
from scripts.crawler import crawl_news
from scripts.db_operations import get_today_news, get_today_recommendations
from scripts.slack_notifier import send_newsletter
import schedule
import time
import threading

def main():
    st.title('주식 분석 대시보드')
    
    # 뉴스 표시
    st.header('오늘의 뉴스')
    news_df = get_today_news()
    st.table(news_df)
    
    # 추천 표시
    st.header('매수/매도 추천')
    rec_df = get_today_recommendations()
    st.table(rec_df)

def background_tasks():
    # 매일 오전 9시에 뉴스 크롤링
    schedule.every().day.at("09:00").do(crawl_news)
    
    # 매 시간마다 추천 시스템 실행 (db_operations.py에서 실행)
    schedule.every(1).hour.do(get_today_recommendations)
    
    # 매일 오후 5시에 뉴스레터 전송
    schedule.every().day.at("17:00").do(send_newsletter)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    # 백그라운드 작업 시작
    bg_thread = threading.Thread(target=background_tasks)
    bg_thread.start()
    
    # Streamlit 앱 실행
    main()