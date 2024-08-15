import requests
from bs4 import BeautifulSoup
from datetime import datetime
from scripts.db_operations import save_news

def crawl_news():
    """
    네이버 금융 뉴스를 크롤링하고 데이터베이스에 저장하는 함수
    """
    url = "https://finance.naver.com/news/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_list = soup.select('.mainNewsList .articleSubject')
    
    for news in news_list:
        title = news.text.strip()
        link = "https://finance.naver.com" + news.find('a')['href']
        
        # 각 뉴스 기사의 내용을 가져옴
        news_response = requests.get(link)
        news_soup = BeautifulSoup(news_response.text, 'html.parser')
        content = news_soup.select_one('#content').text.strip()
        
        # 데이터베이스에 저장
        save_news(datetime.now().date(), title, content)

if __name__ == "__main__":
    crawl_news()