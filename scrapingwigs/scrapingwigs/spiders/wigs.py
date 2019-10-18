# -*- coding: utf-8 -*-
import scrapy


class WigsSpider(scrapy.Spider):
    name = 'wigs'
    allowed_domains = ['wigs.com/']
    start_urls = ['https://www.wigs.com/collections/wigs.html/']

    def parse(self, response):
        wig_selector = '.product-index'

        for wig in response.css(wig_selector):
            link_selector = 'a::attr(href)'

            yield {
                'link': wig.css(link_selector).extract_first(),
            }
