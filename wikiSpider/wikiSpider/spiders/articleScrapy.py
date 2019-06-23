from scrapy import Spider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider

from wikiSpider.items import Article


class ArticleSpider(CrawlSpider):
    name="article"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["http://en.wikipedia.org/wiki/Python_%28programming_language%29"]
    rules = [Rule(LinkExtractor(allow=('(/wiki/)(?!:)*$'),),
                                    callback="parse_item",follow=True)]

    def parse(self, response):
        item = Article()
        title = response.xpath('//h1/text()')[0].extract()
        print("Title is :" + title)
        item['title'] = title
        return item

# scrapy crawl article -o articles.csv -t csv
# scrapy crawl article -o articles.json -t json
# scrapy crawl article -o articles.xml -t xml
