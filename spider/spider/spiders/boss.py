# -*- coding: utf-8 -*-
import scrapy


class BossSpider(scrapy.Spider):
    name = 'boss'
    allowed_domains = ['www.zhipin.com']
    start_urls = ['https://www.zhipin.com/c101020100/e_102/?query=UI设计师']

    def parse(self, response):
        a = response.xpath('//*[@id="main"]/div/div[3]/ul/li[1]')
        print(a)
        print(1)
        pass
