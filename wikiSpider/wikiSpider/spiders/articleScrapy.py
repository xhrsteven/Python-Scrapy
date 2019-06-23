from scrapy import Spider
from scrapy.spiders import Rule
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spiders import CrawlSpider

from wikiSpider.items import Article


class ArticleSpider(CrawlSpider):
    name="article"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["http://en.wikipedia.org/wiki/Python_%28programming_language%29"]
    rules = [Rule(SgmlLinkExtractor(allow=('(/wiki/)(?!:)*$'),),
                                    callback="parse_item",follow=True)]

    def parse(self, response):
        item = Article()
        title = response.xpath('//h1/text()')[0].extract()
        print("Title is :" + title)
        item['title'] = title
        return item

