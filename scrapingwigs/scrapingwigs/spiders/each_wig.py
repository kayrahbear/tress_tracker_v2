import json
import scrapy

from scrapingwigs.items import Wig


class EachWigSpider(scrapy.Spider):
    name = "EachWig"

    def start_requests(self):
        with open("wiglinks_nbw.json", "r") as f:
            data = json.loads(f.read())
        for item in data[:10]:
            yield scrapy.Request(f"https://www.namebrandwigs.com{item['link']}")

    custom_settings = {"FEED_URI": "each_wig.json", "FEED_FORMAT": "json"}

    def parse(self, response):
        print(f"procesing: {response.url}")

        # from scrapy.shell import inspect_response

        # inspect_response(response, self)

        product_json = response.xpath(
            '//script[@type="application/json"]//text()'
        ).getall()[-1]

        product_tree = json.loads(product_json)

        scraped_wig = Wig()

        for variant in product_tree["variants"]:
            scraped_wig["wig_url"] = response.url
            scraped_wig["wig_name"] = product_tree["title"]
            scraped_wig["brand"] = product_tree["vendor"]
            scraped_wig["price"] = variant["price"]
            scraped_wig["main_image"] = f"http:{product_tree['featured_image']}"
            scraped_wig["color_name"] = variant["option1"]
            scraped_wig["color_swatch"] = variant["featured_image"]["src"]
            scraped_wig["tags"] = product_tree["tags"]

            yield scraped_wig
