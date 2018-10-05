import json
# import urllib.request
from urllib2 import urlopen
from .models import News

# Getting api key
api_key = None

#getting the news base url
base_url =None

def configure_request(app) :
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']


def get_news(category):
    """
    function that gets json response to our url request
    """
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources'] :
            news_results_list = get_news_response['sources']
            news_results = prrocess_results(news_results_list)

    return news_results


def prrocess_results(news_list) :
    """
    function that processes the news result and transforms them to a list of objects
    Args:
        news_list : list of dictionaries tha contain news details
    Returns:
        news_results: list of news objects
    """
    news_results = []
    for news_item in news_list :
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        site = news_item.get('url')
        image = news_item.get('urlToImage')
        content = news_item.get('content')

        if image :
            news_object = News(author,title,description,site,image,content)
            news_results.append(news_object)

            print(news_list)
    return news_results



