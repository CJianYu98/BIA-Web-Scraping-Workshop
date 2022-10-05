import scrapy


class CourtsSpider(scrapy.Spider):
    name = "lab2_spider"

    start_urls = ["https://www.courts.com.sg/computing-mobile/smart-phones/all-smart-phones"]

    def parse(self, response):

        products = response.css(".equal-height-col .product-item")

        for p in products:
            title = p.css(".onclick-item-link .product-item-name .product-item-link").get()
            print(title)
