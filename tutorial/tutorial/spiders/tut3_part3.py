import scrapy

from ..items import QuotesTutorialItem

# Web crawling using pagination
class QuotespiderSpider(scrapy.Spider):
    name = "tut3_spider3_3"
    start_urls = ["http://quotes.toscrape.com/"]
    page_number = 1

    def parse(self, response):
        items = QuotesTutorialItem()

        all_div_quotes = response.css("div.quote")

        for quotes in all_div_quotes:
            title = quotes.css("span.text::text").get()
            author = quotes.css(".author::text").get()
            tag = quotes.css(".tag::text").get()

            items["title"] = title
            items["author"] = author
            items["tag"] = tag

            yield items

        if self.page_number <= 10:
            self.page_number += 1
            next_page = f"https://quotes.toscrape.com/page/{self.page_number}/"

            yield response.follow(next_page, callback=self.parse)
