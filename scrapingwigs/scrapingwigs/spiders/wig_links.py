# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver


class WigLinkSpider(scrapy.Spider):
    name = 'WigLinks'
    start_urls = ['https://www.namebrandwigs.com/collections/all-items?_=pf&pf_pt_product_type=wig&pf_pt_product_type=Enhancer']

    custom_settings={'FEED_URI': "wiglinks_nbw.json",
                    'FEED_FORMAT': 'json'}

    def parse(self, response):
        wigs_on_page = response.css('.grid__item').getall()

        for wig in wigs_on_page:
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
            
            
            
            
            
            
