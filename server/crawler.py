import requests
from bs4 import BeautifulSoup
from datetime import datetime

def crawl_news():
    url = 'https://news.naver.com/breakingnews/section/101/258'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    articles = []
    for article in soup.find_all('div', class_='sa_text'):
        title_tag = article.find('a', class_='sa_text_title')
        if title_tag:
            title = title_tag.find('strong').get_text().strip()
            link = title_tag['href']
            articles.append({
                'title': title,
                'link': link,
                'date': datetime.now().strftime('%Y-%m-%d')
            })
    
    return articles