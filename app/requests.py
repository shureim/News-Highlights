import urllib.request,json
from .models import News

# Getting api key
api_key = None

#getting the news base url
base_url =None

def configure_request(app) :
    global api_key,base_url,article_base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    article_base_url = app.config ['NEWS_API_TOP_HEADING_URL']

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
            news_results = process_results(news_results_list)

    return news_results


def process_results(news_list) :
    """
    function that processes the news result and transforms them to a list of objects
    Args:
        news_list : list of dictionaries tha contain news details
    Returns:
        news_results: list of news objects
    """
    news_results = []
    for news_item in news_list :
        id= news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')

        news_object = News(id,name,description,url,category)
        news_results.append(news_object)

        print(news_list)
    return news_results

def get_articles(id):
    """
    function that gets json response to our url request
    """
    get_articles_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_articles_url) as url :

        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_news_response['top_heading'] :
            articles_results_list = get_articles_response['top_heading']
            articles_results = process_results(articles_results_list)

    return articles_results
#
# def process_articles(articles_list):
#         """
#         function that processes the news result and transforms them to a list of objects
#         Args:
#             articles_list : list of dictionaries tha contain articles details
#         Returns:
#             articles_results: list of articles objects
#         """
#         articles_results = []
#         for articles_item in articles_list:
#             author= articles_item.get('author')
#             title = articles_item.get('title')
#             description = articles_item.get('description')
#             site = articles_item.get('urlToImage')
#             url = articles_item.get('url')
#             content = articles_item.get('content')
#
#             articles_object = Articles(author,title,description,site,url,content)
#             articles_results.append(articles_object)
#
#             print(articles_list)
#         return articles_results
