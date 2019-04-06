# -*- coding: utf-8 -*-
import scrapy


class DemoSpider(scrapy.Spider):
    name = 'demo'
    # allowed_domains = ['python123.io']
    start_urls = ['https://www.cnblogs.com/Garvey/p/6691753.html']

    def parse(self, response):
        fname = response.url.split('/')[-1]
        with open(fname,'wb') as f:
        		f.write(response.body)
            
        self.log('Save file %s.'%fname)