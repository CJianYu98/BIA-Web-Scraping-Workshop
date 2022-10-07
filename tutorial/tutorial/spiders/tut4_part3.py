import scrapy
from scrapy_playwright.page import PageMethod

from ..items import QuotesTutorialItem


# Scroll all the way down
class PWSpider(scrapy.Spider):
    name = "pw_spider3"

    def start_requests(self):
        url = "https://quotes.toscrape.com/scroll"
        yield scrapy.Request(
            url,
            meta=dict(
                playwright=True,
                playwright_include_page=True,
                playwright_page_methods=[
                    PageMethod("wait_for_selector", "div.quote"),
                    PageMethod(
                        "evaluate", "window.scrollBy(0, document.body.scrollHeight)"
                    ),  # scrolls the page relative to its current position. Scrolls down by the length of the page.
                    PageMethod(
                        "wait_for_selector", ".quote:nth-child(100)"
                    ),  # wait for the last quote to render
                ],
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
