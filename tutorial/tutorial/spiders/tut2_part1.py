import scrapy

from ..items import BookItem


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    start_urls = ["http://books.toscrape.com/"]

    def parse(self, response):
        items = BookItem()

        book_list = response.css("article.product_pod")

        for book in book_list:
            title = book.css("h3 a").attrib["title"]
            price = book.css("p.price_color::text").get()

            items["title"] = title
            items["price"] = price

            yield items
