# -*- coding: utf-8 -*-
import scrapy


class WigLinkSpider(scrapy.Spider):
    name = 'wigs'
    start_urls = ['https://www.wigs.com/collections/wigs.html/']

    custom_settings={ 'FEED_URI': "wiglinks_%(time)s.json",
                    'FEED_FORMAT': 'json'}

    def parse(self, response):
        wig_selector = '.product-index'

        for wig in response.css(wig_selector):
            link_selector = 'a::attr(href)'

            yield {
                'link': wig.css(link_selector).extract_first(),
            }

        next_page = response.xpath("//a[contains(.,'>')]/@href").extract_first()

        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback = self.parse
            )
            
            
            
            
            
            
