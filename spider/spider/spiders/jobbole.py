# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import Request
from urllib import parse
from spider.items import JobBoleArticleItem

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        # ”“”
        # 1. 获取文章列表页面中的文章url并交给scrapy下载后并进行解析
        # 2. 获取下一页的url并交给scrapy进行下载， 下载完成后交给parse
        # “”“

        # 解析列表页的所以文章url并竟给scrapy下载后并进行解析
        post_nodes = response.css("#archive .floated-thumb .post-thumb a")
        for post_node in post_nodes:
            image_url = post_node.css("img::attr(src)").extract_first("")
            post_url = post_node.css("::attr(href)").extract_first("")
            yield Request(url = parse.urljoin(response.url, post_url), meta={"front_image_url":image_url}, callback = self.parse_detail)

        # 提取下一页并交给scrapy进行下载
        next_urls = response.css(".next.page-numbers::attr(href)").extract_first()
        if next_urls:
            # yield Request(url = parse.urljoin(response.url, next_urls), callable = self.parse(self, response))
            yield Request(url = parse.urljoin(response.url, next_url), callback = self.parse)

    def parse_detail(self, response):
        article_item = JobBoleArticleItem()

        # 提取文章内容

        # 通过 xpath
        # """
        # # re_selector = response.xpath("/html/body/div[3]/div[3]/div[1]/div[1]/h1")
        # # extract() 获取里面内容
        # title = response.xpath('//*[@id="post-114690"]/div[1]/h1/text()').extract()[0]
        # create_date =  response.xpath('//*[@id="post-114690"]/div[2]/p/text()').extract()[0].strip().replace("·", "").strip()
        # praise_nums = response.xpath('//*[@id="114690votetotal"]/text()').extract()[0]
        # fav_nums = int(response.xpath('//*[@id="post-114690"]/div[3]/div[9]/span[2]/text()').extract()[0])
        # comment_nums = int(response.xpath('//*[@id="post-114690"]/div[3]/div[9]/a/span/text()').extract()[0])
        # match_re = re.match(".*(\d+).*", fav_nums)
        # if fav_nums:
        #     fav_nums = int(match_re.group(1))
        # else:
        #     fav_nums = 0

        # comment_nums = response.xpath('//*[@id="post-114690"]/div[3]/div[9]/a/span/text()').extract()[0]
        # match_re = re.match(".*(\d+).*", comment_nums)
        # if comment_nums:
        #     comment_nums = int(match_re.group(1))
        # else:
        #     comment_nums = 0

        # content = response.xpath('//div[@class="entry"]').extract()[0]

        # tag_list =  response.xpath('//*[@id="post-114690"]/div[2]/p/a/text()').extract()
        # tag_list = [element for element in tag_list if not element.strip().endswith("评论")]
        # tags = ",".join(tag_list)
        # """

        # 通过css 选择器提取字段
        # 文章封面图
        front_image_url = response.meta.get("front_image_url", "")
        #标题
        title = response.css(".entry-header h1::text").extract()[0]
        #创建时间
        create_date = response.css(".entry-meta p::text").extract()[0].strip().replace("·", "").strip()
        # 点赞数
        praise_nums = response.css(".post-adds span h10::text").extract()[0]
        # 收藏数
        fav_nums = response.css(".post-adds .bookmark-btn::text").extract()[0]
        match_re = re.match(".*(\d+).*", fav_nums)
        if fav_nums:
            fav_nums = int(match_re.group[1])
        else:
            fav_nums = 0
        # 评论数
        comment_nums = response.css("a .btn-bluet-bigger::text").extract()[0]
        match_re = re.match(".*(\d+).*", comment_nums)
        if comment_nums:
            comment_nums = int(match_re.group[1])
        else:
            comment_nums = 0

        # 文章内容
        content = response.css(".entry").extract()[0]

        # 标签
        tag_list = response.css(".entry-meta-hide-on-mobile a::text").extract()
        tag_list = [element for element in tag_list if not element.strip().endswith("评论")]
        tags = ",".join(tag_list)

        article_item["title"] = title
        article_item["url"] =  response.url
        article_item["create_date"] = create_date
        article_item["front_image_url"] = [front_image_url]
        article_item["praise_nums"] = praise_nums
        article_item["fav_nums"] = fav_nums
        article_item["comment_nums"] = comment_nums
        article_item["content"] = content
        article_item["tags"] = tags

        yield article_item




        





        