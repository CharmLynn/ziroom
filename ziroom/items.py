# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ZiroomItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    imageurl= scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    houseid = scrapy.Field()
    area = scrapy.Field()
    layout = scrapy.Field()
    floor = scrapy.Field()
    subway = scrapy.Field()
    balcony = scrapy.Field()
    style = scrapy.Field()
    price = scrapy.Field()
    location = scrapy.Field()