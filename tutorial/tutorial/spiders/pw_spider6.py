import scrapy


# Type in search text and take a screenshot after search on Twitch
class PWSpider(scrapy.Spider):
    name = "pw_spider6"

    def start_requests(self):
        url = "https://www.twitch.tv/directory/game/Art"
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

        await page.locator('input[autocomplete="twitch-nav-search"]').type("Painting", delay=100)
        await page.keyboard.press("Enter")
        await page.wait_for_selector('.search-results .tw-link[href*="all/tags"]')
        # await page.wait_for_timeout(7000)
        await page.screenshot(path="full_page.png", full_page=True)

        await page.close()

    async def errback(self, failure):
        page = failure.request.meta["playwright_page"]
        await page.close()
