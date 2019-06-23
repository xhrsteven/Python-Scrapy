import base64
import scrapy
from bqb.items import  BqbItem

__author__ = '100378367'

class BqbSpider(scrapy.Spider):
    name = 'bqb'

    def start_requests(self):
        start_url = ['http://qq.yh31.com/zjbq/0420255.html']

        for url in start_url:
            headers = {
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Accept':'text-javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
                'Connenction': 'keep-alive',
                'User-Agent': 'Mozilla/5.0(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
                'Upgrade-Insecure-Requests': '1'
            }

    def parse(self, response):
        print("33333333333333333333333333")

        img_urls = response.xpath("//div[@id='fontzoom']/p/img")

        a = 0

        for img_url in img_urls:
            url = img_url.xpath("@src").extract()
            print("MMMMMMMMMMM = %s" % url)
            item = BqbItem()
            item['name'] = a
            item['addr'] = url[0]
            a +=1

            yield item

