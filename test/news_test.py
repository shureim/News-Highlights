import unittest
from app.models import News

class NewsTest(unittest.TestCase):
    """
    test class to test the behaviour of the news class
    """
    def setUp(self) :
        """
        setup method will run before every test
        """
        self.new_news = News("James Reinl", "After trade deal win, Trump doubles down on China", "No plans for China-US negotiations over trade war", "http:\/\/www.aljazeera.com\/news\/2018\/10\/trade-deal-win-trump-doubles-china-181004042022058.html", "https:\/\/www.aljazeera.com\/mritems\/Images\/2018\/8\/29\/80285b02a3b34ae8b31bc78eec9d59a6_18.jpg", "US President Donald Trump's new trade deal with Canada")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))
