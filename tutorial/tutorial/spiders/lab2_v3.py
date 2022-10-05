import scrapy
from scrapy_playwright.page import PageMethod
from scrapy.selector import Selector

from ..items import OscarWinningFilmItem


# Oscar Winning film scrape all the years
class PWSpider(scrapy.Spider):
    name = "lab2_v3"

    def start_requests(self):
        url = "https://www.scrapethissite.com/pages/ajax-javascript/"
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
        years = response.css(".year-link::text").getall()

        for year in years:
            await page.click(f"id={year}")
            await page.wait_for_selector(".film")
            html = await page.content()
            selector = Selector(text=html)

            for film in selector.css(".film"):
                oscar_film_item = OscarWinningFilmItem()
                oscar_film_item["year"] = year
                oscar_film_item["title"] = film.css(".film-title::text").get()
                oscar_film_item["nominations"] = film.css(".film-nominations::text").get()
                oscar_film_item["awards"] = film.css(".film-awards::text").get()
                oscar_film_item["best_picture"] = (
                    "Yes" if film.css(".film-best-picture i").get() else "No"
                )
                yield oscar_film_item

        await page.close()

    async def errback(self, failure):
        page = failure.request.meta["playwright_page"]
        await page.close()
