# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_title = scrapy.Field()  # 岗位
    compensation = scrapy.Field()  # 薪资
    company = scrapy.Field()  # 公司
    address = scrapy.Field()  # 地址
    seniority = scrapy.Field()  # 工作年薪
    education = scrapy.Field()  # 教育程度
    company_type = scrapy.Field()  # 公司类型
    company_finance = scrapy.Field()  # 融资
    company_quorum = scrapy.Field()  # 公司人数

class JobBoleArticleItem(scrapy.Item):
    title = scrapy.Field()
    create_date = scrapy.Field()
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    front_image_url = scrapy.Field()
    front_image_path = scrapy.Field()
    praise_nums = scrapy.Field()
    fav_nums = scrapy.Field()
    comment_nums = scrapy.Field()
    content = scrapy.Field()
    tags = scrapy.Field()


