# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WigLink(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    link = scrapy.Field()


class Wig(scrapy.Item):
    wig_id = scrapy.Field()
    wig_name = scrapy.Field()
    brand = scrapy.Field()
    price = scrapy.Field()
    main_image = scrapy.Field()
    color_name = scrapy.Field()
    color_swatch = scrapy.Field()
    tags = scrapy.Field()