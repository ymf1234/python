# -*- coding: utf-8 -*-
import scrapy
from ..items import SpiderItem

class JobbosspiderSpider(scrapy.Spider):
    name = 'jobbosspider'
    #allowed_domains = ['https://www.zhipin.com/']
    allowed_domains = ['zhipin.com']
    # 定义入口URL
    #start_urls = ['https://www.zhipin.com/c101010100/?query=python&page=1&ka=page-1']    #北京
    #start_urls=['https://www.zhipin.com/c100010000/h_101010100/?query=Python&ka=sel-city-100010000']   #全国
    #start_urls=['https://www.zhipin.com/c101020100/h_101010100/?query=Python&ka=sel-city-101020100']   #上海
    #start_urls=['https://www.zhipin.com/c101280100/h_101010100/?query=Python&ka=sel-city-101280100']     #广州
    #start_urls=['https://www.zhipin.com/c101280600/h_101010100/?query=Python&ka=sel-city-101280600']    #深圳
    #start_urls=['https://www.zhipin.com/c101210100/h_101010100/?query=Python&ka=sel-city-101210100']     #杭州
    #start_urls=['https://www.zhipin.com/c101030100/h_101010100/?query=Python&ka=sel-city-101030100']      #天津
    #start_urls=['https://www.zhipin.com/c101110100/h_101010100/?query=Python&ka=sel-city-101110100']       #西安
    #start_urls=['https://www.zhipin.com/c101200100/h_101010100/?query=Python&ka=sel-city-101200100']        #武汉
    #start_urls=['https://www.zhipin.com/c101270100/h_101010100/?query=Python&ka=sel-city-101270100']         #成都
    start_urls=['https://www.zhipin.com/c100010000/h_101270100/?query=python%E7%88%AC%E8%99%AB&ka=sel-city-100010000']  #爬虫工程师，全国

    # 定义解析规则,这个方法必须叫做parse
    def parse(self, response):
        item = SpiderItem()
        # 获取页面数据的条数
        node_list = response.xpath("//*[@id=\"main\"]/div/div[2]/ul/li")
        # 循环解析页面的数据
        for node in node_list:
            item["job_title"] = node.xpath(".//div[@class=\"job-title\"]/text()").extract()[0]
            item["compensation"] = node.xpath(".//span[@class=\"red\"]/text()").extract()[0]
            item["company"] = node.xpath("./div/div[2]/div/h3/a/text()").extract()[0]
            company_info = node.xpath("./div/div[2]/div/p/text()").extract()
            temp = node.xpath("./div/div[1]/p/text()").extract()
            item["address"] = temp[0]
            item["seniority"] = temp[1]
            item["education"] = temp[2]
            if len(company_info) < 3:
                item["company_type"] = company_info[0]
                item["company_finance"] = ""
                item["company_quorum"] = company_info[-1]
            else:
                item["company_type"] = company_info[0]
                item["company_finance"] = company_info[1]
                item["company_quorum"] = company_info[2]
            yield item
            # 定义下页标签的元素位置
            next_page = response.xpath("//div[@class=\"page\"]/a/@href").extract()[-1]
            # 判断什么时候下页没有任何数据
            if next_page != 'javascript:;':
                base_url = "https://www.zhipin.com"
                url = base_url + next_page
                yield scrapy.Request(url=url, callback=self.parse)




'''
# 斜杠（/）作为路径内部的分割符。
# 同一个节点有绝对路径和相对路径两种写法。
# 绝对路径（absolute path）必须用"/"起首，后面紧跟根节点，比如/step/step/...。
# 相对路径（relative path）则是除了绝对路径以外的其他写法，比如 step/step，也就是不使用"/"起首。
# "."表示当前节点。
# ".."表示当前节点的父节点

nodename（节点名称）：表示选择该节点的所有子节点

# "/"：表示选择根节点

# "//"：表示选择任意位置的某个节点

# "@"： 表示选择某个属性
'''