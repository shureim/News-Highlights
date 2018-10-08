from flask import render_template
from . import main
from ..requests import get_news

# Views
@main.route('/')
def index() :
    """
    view root page function that returns the index page and data
    """

    sources = get_news('sources')

    title = "Now you know "
    return render_template('index.html', title = title, sources = sources)
#
# @main.route('/news/<int:news_id>')
# def news(news_id) :
#     """
#     view news page that returns the news details page and its data
#     """
#     news = "first new for you"
#     return render_template('news.html', id =news_id, news = news)
