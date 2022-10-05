import scrapy
from scrapy_playwright.page import PageMethod

from ..items import QuotesTutorialItem


### Getting title, author and tag for each quote
class PWSpider(scrapy.Spider):
    name = "pw_spider1"

    def start_requests(self):
        url = "https://quotes.toscrape.com/js/"
        yield scrapy.Request(
            url,
            meta=dict(
                playwright=True,
                playwright_include_page=True,
                playwright_page_methods=[PageMethod("wait_for_selector", "div.quote")],
                errback=self.errback,
            ),
        )

    async def parse(self, response):
        page = response.meta["playwright_page"]
        await page.close()

        for quote in response.css("div.quote"):
            quote_item = QuotesTutorialItem()
            quote_item["title"] = quote.css("span.text::text").get()
            quote_item["author"] = quote.css("small.author::text").get()
            quote_item["tag"] = quote.css("div.tags a.tag::text").getall()
            yield quote_item

    async def errback(self, failure):
        page = failure.request.meta["playwright_page"]
        await page.close()
