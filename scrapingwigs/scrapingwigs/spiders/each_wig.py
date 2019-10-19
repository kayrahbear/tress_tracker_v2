import json

import js2xml
import scrapy

from scrapingwigs.items import Wig


class EachWigSpider(scrapy.Spider):
    name = "EachWig"

    def start_requests(self):
        with open("wiglinks_nbw.json", "r") as f:
            data = json.loads(f.read())
        # for item in data:
        yield scrapy.Request(f"https://www.namebrandwigs.com{data[1]['link']}")

    custom_settings = {"FEED_URI": "each_wig.json", "FEED_FORMAT": "json"}

    def parse(self, response):
        print(f"procesing: {response.url}")

        product_json = response.xpath(
            '//script[@type="application/json"]//text()'
        ).getall()[-1]

        product_tree = json.loads(product_json)

        scraped_wig = Wig()
        colors = []
        price = []

        scraped_wig["wig_id"] = product_tree["handle"]
        scraped_wig["wig_name"] = product_tree["title"]
        scraped_wig["brand"] = product_tree["vendor"]
        scraped_wig["main_image"] = f"http:{product_tree['featured_image']}"
        scraped_wig["cap_size"] = product_tree["variants"][0]["option2"]

        yield scraped_wig
