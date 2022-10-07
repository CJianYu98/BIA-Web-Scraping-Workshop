import scrapy

from ..items import QuotesTutorialItem

# Web crawling using next page href
class QuotespiderSpider(scrapy.Spider):
    name = "tut3_spider3_2"
    start_urls = ["http://quotes.toscrape.com/"]

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

        next_page = response.css("li.next a::attr(href)").get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
