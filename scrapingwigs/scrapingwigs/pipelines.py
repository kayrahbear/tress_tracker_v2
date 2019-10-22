import re
import pymongo

from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log
from scrapingwigs.items import Wig
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapingwigsPipeline(object):
    def process_item(self, Wig, spider):
        #move the decimal in the price int
        format_price = Wig['price']/100
        
        #remove the extra characters from the wig name. I wrote a regex!
        wig_name_str =  Wig['wig_name']
        try:
            only_wig_name = re.search(' - (.+?) #', wig_name_str).group(1)
        except AttributeError:
            only_wig_name = wig_name_str
        
        #get those price marks out of the color name
        color_name = Wig['color_name'].split(' +$')[0]

        #ughh why do some of the brands have SALE on the end?!
        brand_name = Wig['brand'].split(" S")[0]

        Wig['price'] = format_price
        Wig['wig_name'] = only_wig_name
        Wig['color_name'] = color_name
        Wig['brand'] = brand_name

        return Wig


class MongoDBPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            self.collection.insert(dict(item))
            log.msg("Question added to MongoDB database!",
                    level=log.DEBUG, spider=spider)
        return item
