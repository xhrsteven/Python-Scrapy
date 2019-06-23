# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import base64
import requests

class BqbPipeline(object):
    def process_item(self, item, spider):
        url = "http://qq.yh31.com"+ item['addr']
        print('xxxxxxxxxx=%s' % url)

        headers = {
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept': 'text-javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
            'Connenction': 'keep-alive',
            'User-Agent': 'Mozilla/5.0(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
            'Upgrade-Insecure-Requests': '1'
        }
        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8'

        with open('E:\\GitHub\\Python-Scrapy\\bqb\\data\\%d.gif' % item['name'], 'wb') as ft:
            ft.write(response.content)

        return item
