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

    custom_settings = {"FEED_URI": "each_wig.csv", "FEED_FORMAT": "csv"}

    def parse(self, response):
        print(f"procesing: {response.url}")

        # from scrapy.shell import inspect_response

        # inspect_response(response, self)

        product_json = response.xpath(
            '//script[@type="application/json"]//text()'
        ).getall()[-1]

        product_tree = json.loads(product_json)

        scraped_wig = Wig()
        colors = []
        price = []

        for variant in product_tree["variants"]:
            color_swatch_tuple = (variant["option1"], variant["featured_image"]["src"])
            colors.append(color_swatch_tuple)
            price.append(variant["price"])

        scraped_wig["wig_id"] = product_tree["handle"]
        scraped_wig["wig_name"] = product_tree["title"]
        scraped_wig["brand"] = product_tree["vendor"]
        scraped_wig["price"] = price
        scraped_wig["main_image"] = f"http:{product_tree['featured_image']}"
        scraped_wig["colors"] = colors
        scraped_wig["hair_type"] = product_tree["tags"]
        scraped_wig["length"] = product_tree["description"]
        scraped_wig["description"] = product_tree["description"]
        scraped_wig["cap_features"] = product_tree["tags"]

        yield scraped_wig
