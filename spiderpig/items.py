# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NovelItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 小说名字
    name = scrapy.Field()

    # 作者
    author = scrapy.Field()

    # 地址
    novelurl = scrapy.Field()

    # 状态
    serialstatus = scrapy.Field()

    # 字数
    serialnumber = scrapy.Field()

    # 类别
    category = scrapy.Field()

    # 编号
    name_id = scrapy.Field()

class ContentItem(scrapy.Item):
    # 小说地址
    novelurl = scrapy.Field()

    # 章节内容
    chaptercontent = scrapy.Field()

    # 章节顺序
    chapterorder = scrapy.Field()

    # 章节链接
    chapterurl = scrapy.Field()

    # 章节名字
    chaptername = scrapy.Field()
