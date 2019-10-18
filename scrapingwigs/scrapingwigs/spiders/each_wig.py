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

        scraped_wig = {
            'scraped_url': response.url,
            'wig_name': response.xpath("//h1[contains(@class,'product-title-main')]/text()").get(),
            'brand': response.xpath("//h2[@id='bh_vendor_name']/text()").get(),
            'price': response.xpath("//span[contains(@class,'product-price')]/text()").get(),
            'hair_type': response.xpath("//tr[contains(.,'Hair Type:')]//td[2]//text()").get()
        }

        yield scraped_wig
