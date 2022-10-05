import scrapy
from scrapy_playwright.page import PageMethod

from ..items import QuotesTutorialItem


## Scraping multiple pages
class PWSpider(scrapy.Spider):
    name = "pw_spider2"

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

        next_page = response.css(".next a::attr(href)").get()

        if next_page is not None:
            next_page_url = f"http://quotes.toscrape.com{next_page}"
            yield scrapy.Request(
                next_page_url,
                meta=dict(
                    playwright=True,
                    playwright_include_page=True,
                    playwright_page_methods=[
                        PageMethod("wait_for_selector", "div.quote"),
                    ],
                    errback=self.errback,
                ),
            )

    async def errback(self, failure):
        page = failure.request.meta["playwright_page"]
        await page.close()
