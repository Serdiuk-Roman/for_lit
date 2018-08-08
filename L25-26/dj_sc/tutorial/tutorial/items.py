# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class PostItem(Item):
    title = Field()
    text = Field()
    img = Field()


class PorterItem(Item):
    designer_name = Field()
    link = Field()
    product_name = Field()
    price = Field()
    currency = Field()
    size = Field()
    description = Field()
    images = Field()
