import os

class Config:
    """
    General configuration of parent class
    """
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    NEWS_API_TOP_HEADING_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


    pass


class ProdConfig(Config):
    """
    Production configuration child class
    Args:
        Config : the parent configuration class with general configuration settings
    """
    pass


class DevConfig(Config):
    """
    Development configuration child class
    Args:
        Config:  the parent configuration class with general configuration settings
    """
    DEBUG = True

config_options = {
    'development' : DevConfig,
    'produnction' :ProdConfig
}
