import scrapy
from scrapy.loader import ItemLoader

from ..items import CourtsItem


class CourtsSpider(scrapy.Spider):
    name = "tut3_spider3_7"

    start_urls = ["https://www.courts.com.sg/computing-mobile/smart-phones/all-smart-phones"]

    def parse(self, response):
        products = response.css(".equal-height-col .product-item")

        for product in products:
            prices = product.css(".weee .price::text").getall()
            curr_price = prices[0]
            old_price = prices[1] if len(prices) == 2 else None

            loader = ItemLoader(item=CourtsItem(), selector=product)
            loader.add_css("name", ".onclick-item-link .product-item-name .product-item-link::text")
            loader.add_value("curr_price", curr_price)
            loader.add_value("old_price", old_price)
            loader.add_value("currency", curr_price)

            yield loader.load_item()
