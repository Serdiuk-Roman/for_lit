# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class PostItem(scrapy.Item):
    title = scrapy.Field()
    text = scrapy.Field()
    img = scrapy.Field()


class ClothingItem(scrapy.Item):
    designer_name = scrapy.Field()
    product_name = scrapy.Field()
    product_price = scrapy.Field()
    product_currency = scrapy.Field()
    product_size = scrapy.Field()
    product_description = scrapy.Field()
    img = scrapy.Field()


class ShoesItem(scrapy.Item):
    pass
