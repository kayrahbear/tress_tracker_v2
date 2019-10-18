# -*- coding: utf-8 -*-
import scrapy


class WigLinkSpider(scrapy.Spider):
    name = 'wig_links'
    start_urls = ['https://www.namebrandwigs.com/collections/all-items?_=pf&pf_pt_product_type=wig&pf_pt_product_type=Enhancer']

    custom_settings={ 'FEED_URI': "wiglinks_nbw.json",
                    'FEED_FORMAT': 'json'}

    def parse(self, response):
        wig_selector = '.grid__item'

        for wig in response.css(wig_selector):
            link_selector = 'a::attr(href)'

            yield {
                'link': wig.css(link_selector).extract_first(),
            }

        next_page = response.xpath("//a[contains(.,'→')]/@href").extract_first()

        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback = self.parse
            )
            
            
            
            
            
            
