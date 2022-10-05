import scrapy
from scrapy_playwright.page import PageMethod


# Take screenshot
class PWSpider(scrapy.Spider):
    name = "pw_spider4"

    def start_requests(self):
        url = "https://quotes.toscrape.com/js/"
        yield scrapy.Request(
            url,
            meta=dict(
                playwright=True,
                playwright_include_page=True,
                playwright_page_methods=[
                    PageMethod("wait_for_selector", "div.quote"),
                ],
                errback=self.errback,
            ),
        )

    async def parse(self, response):
        page = response.meta["playwright_page"]
        ele_screenshot = await page.locator(".quote:nth-child(4)").screenshot(path="element.png")
        fp_screenshot = await page.screenshot(path="full_page.png", full_page=True)
        # fp_screenshot contains the image's bytes
        await page.close()

    async def errback(self, failure):
        page = failure.request.meta["playwright_page"]
        await page.close()
