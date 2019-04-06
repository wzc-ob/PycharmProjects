# -*- coding: utf-8 -*-
import scrapy


class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['python123demo.io']
    start_urls = ['http://python123demo.io/']

    def parse(self, response):
        pass
