# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider,Request
from urllib.parse import urlencode
import json
from images360.items import ImageItem

class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['images.so.com']
    start_urls = ['http://images.so.com/']

    def parse(self, response):
        result = json.loads(response.text)
        for image in result.get('list'):
            item = ImageItem()
            item['id'] = image.get('id')
            item['url'] = image.get('qhimg_url')
            item['title'] = image.get('title')
            item['thumb'] = image.get('qhimg_thumb')
            yield item


    def start_requests(self):
        data = {'ch': 'beauty','listtype': 'new','temp': '1'}
        base_url = 'http://images.so.com/zjl?'
        for page in range(1,self.settings.get('MAX_PAGE') +1):
            data['sn'] = page * 30
            params = urlencode(data)
            url = base_url +params
            yield Request(url,self.parse)