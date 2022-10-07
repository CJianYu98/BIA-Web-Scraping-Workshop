import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser

from ..items import QuotesTutorialItem

# Login using FormRequest
class QuoteSpider(scrapy.Spider):
    name = "tut3_spider3_4"
    start_urls = ["http://quotes.toscrape.com/login"]

    def parse(self, response):
        token = response.css("form input::attr(value)").get()
        return FormRequest.from_response(
            response,
            formdata={
                "csrf_token": token,
                "username": "webscraping@gmail.com",
                "password": "webscraping",
            },
            callback=self.start_scraping,
        )

    def start_scraping(self, response):
        open_in_browser(response)
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
