import json
import scrapy

class EachWigSpider(scrapy.Spider):
    name = "EachWigSpider"

    def start_requests(self):
        with open('wiglinks.json', 'r') as f:
            data = json.loads(f.read())
        for item in data:
            yield scrapy.Request(f"https://www.wigs.com{item['link']}")


    custom_settings={ 'FEED_URI': "each_wig.json",
                'FEED_FORMAT': 'json'}

    def parse(self, response):
        print("procesing:"+response.url)

        wig_name = response.css('.product-title-main::text').get()
        brand = response.css('.bh_vendor_name::text').get()
        price = response.css('.product-price::text').get()
        # hair_type = response.xpath("//tr[contains(.,'Hair Type:')]//td[2]").get()

        scraped_wig = {
            'wig_name': wig_name,
            'brand': brand,
            'price': price
        }

        yield scraped_wig
