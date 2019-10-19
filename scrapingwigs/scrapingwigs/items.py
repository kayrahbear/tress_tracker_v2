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
    colors = scrapy.Field()
    cap_size = scrapy.Field()
    hair_type = scrapy.Field()
    length = scrapy.Field()
    weight = scrapy.Field()
    description = scrapy.Field()
