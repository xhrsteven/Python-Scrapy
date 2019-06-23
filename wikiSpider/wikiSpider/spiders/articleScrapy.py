from scrapy.selector import Selector
from scrapy import Spider
from wikiSpider.items import Article


class ArticleSpider(Spider):
    name="article"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["http://"]