# -*- coding: utf-8 -*-
import scrapy


class WigLinkSpider(scrapy.Spider):
    name = "WigLinks"
    start_urls = [
        "https://www.namebrandwigs.com/collections/all-items.html?_=pf&pf_pt_product_type=wig&pf_pt_product_type=Enhancer"
    ]

    custom_settings = {"FEED_URI": "wiglinks_nbw.json", "FEED_FORMAT": "json"}

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url,
                self.parse,
                meta={"splash": {"endpoint": "render.html", "args": {"wait": 1.0}}},
            )

    def parse(self, response):
        # # https://docs.scrapy.org/en/latest/topics/shell.html#invoking-the-shell-from-spiders-to-inspect-responses
        # from scrapy.shell import inspect_response

        # inspect_response(response, self)

        wigs_links_on_page = response.xpath(
            "//div[contains(@class,'bc-al-exist')]//a/@href"
        ).getall()

        for link in wigs_links_on_page:

            yield {"link": link}

        next_page = response.xpath("//a[contains(.,'→')]/@href").extract_first()

        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                self.parse,
                meta={"splash": {"endpoint": "render.html", "args": {"wait": 1.0}}},
            )
