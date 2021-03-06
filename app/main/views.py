from flask import render_template
from . import main
from ..requests import get_news,get_articles
from ..models import News,Articles

# Views
@main.route('/')
def index() :
    """
    view root page function that returns the index page and data
    """

    general = get_news()

    title = "Now you know "
    return render_template('index.html', title = title, general = general)

@main.route('/articles/<string:id>')
def news(id):
    """
    view news page that returns the news details page and its data
    """
    articles = get_articles(id)
    news = "first new for you"
    return render_template('news.html',news = news,articles=articles)
