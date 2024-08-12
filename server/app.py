from flask import Flask, jsonify, request, g
from datetime import datetime
from models import db, Article
from scheduler import schedule_crawl

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///articles.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

initialized = False

@app.before_request
def initialize():
    global initialized
    if not initialized:
        with app.app_context():
            db.create_all()
            schedule_crawl()
        initialized = True

@app.route('/')
def index():
    return 'Welcome to the News Crawler API'

@app.route('/add_articles', methods=['POST'])
def add_articles():
    articles = request.json['articles']
    for article in articles:
        new_article = Article(
            title=article['title'],
            link=article['link'],
            date=datetime.strptime(article['date'], '%Y-%m-%d').date()
        )
        db.session.add(new_article)
    db.session.commit()
    return jsonify({'message': 'Articles added successfully'}), 201

@app.route('/articles', methods=['GET'])
def get_articles():
    articles = Article.query.all()
    output = []
    for article in articles:
        article_data = {
            'title': article.title,
            'link': article.link,
            'date': article.date.strftime('%Y-%m-%d')
        }
        output.append(article_data)
    return jsonify({'articles': output})

if __name__ == '__main__':
    app.run(debug=True)