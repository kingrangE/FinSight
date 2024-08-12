import schedule
import time
import threading
from crawler import crawl_news
import requests

def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

def schedule_crawl():
    schedule.every(1).hour.do(lambda: post_articles_to_server(crawl_news()))
    scheduler_thread = threading.Thread(target=run_schedule)
    scheduler_thread.start()

def post_articles_to_server(articles):
    response = requests.post('http://127.0.0.1:5000/add_articles', json={'articles': articles})
    if response.status_code == 201:
        print('크롤링한 데이터가 DB에 성공적으로 저장되었습니다.')
    else:
        print('데이터 저장에 실패했습니다.')