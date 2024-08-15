from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import pandas as pd
import timing  # 매수/매도 추천 시스템 모듈

# 데이터베이스 설정
Base = declarative_base()
engine = create_engine('sqlite:///data/stock_news.db', echo=True)
Session = sessionmaker(bind=engine)

# 뉴스 데이터 모델
class News(Base):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    title = Column(String)
    content = Column(String)

# 추천 데이터 모델
class Recommendation(Base):
    __tablename__ = 'recommendations'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    symbol = Column(String)
    recommendation = Column(String)

Base.metadata.create_all(engine)

def save_news(date, title, content):
    """뉴스를 데이터베이스에 저장하는 함수"""
    session = Session()
    new_news = News(date=date, title=title, content=content)
    session.add(new_news)
    session.commit()
    session.close()

def get_today_news():
    """오늘의 뉴스를 데이터베이스에서 가져오는 함수"""
    session = Session()
    today_news = session.query(News).filter(News.date == datetime.now().date()).all()
    session.close()
    return pd.DataFrame([(news.title, news.content) for news in today_news], columns=['Title', 'Content'])

def save_recommendation(date, symbol, recommendation):
    """추천을 데이터베이스에 저장하는 함수"""
    session = Session()
    new_rec = Recommendation(date=date, symbol=symbol, recommendation=recommendation)
    session.add(new_rec)
    session.commit()
    session.close()

def get_today_recommendations():
    """오늘의 추천을 가져오고, 없으면 새로 생성하는 함수"""
    session = Session()
    today_recs = session.query(Recommendation).filter(Recommendation.date == datetime.now().date()).all()
    session.close()
    
    if not today_recs:
        # timing.py의 main 함수 실행
        results = timing.main()
        for symbol, recommendation in results.items():
            save_recommendation(datetime.now().date(), symbol, recommendation)
        return pd.DataFrame(results.items(), columns=['Symbol', 'Recommendation'])
    else:
        return pd.DataFrame([(rec.symbol, rec.recommendation) for rec in today_recs], columns=['Symbol', 'Recommendation'])