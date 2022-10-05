import scrapy


# OpenCart Login, typing in username and password then click to login
class PWSpider(scrapy.Spider):
    name = "pw_spider5"

    def start_requests(self):
        url = "https://demo.opencart.com/admin/"
        yield scrapy.Request(
            url,
            meta=dict(
                playwright=True,
                playwright_include_page=True,
                errback=self.errback,
            ),
        )

    async def parse(self, response):
        page = response.meta["playwright_page"]

        await page.fill("id=input-username", "demo")
        await page.fill("id=input-password", "demo")
        await page.click(".btn-primary")
        await page.wait_for_timeout(5000)

        await page.close()

    async def errback(self, failure):
        page = failure.request.meta["playwright_page"]
        await page.close()
