class News:
    """
    news class to define news object
    """

    def __init__(self, id, name, description, url,category):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category



class Articles :
    """
    articles class to define articles objects
    """
    def __init__(self,author,title,description,urlToImage,url,content) :
        self.author = author
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.url = url
        self.content = content
