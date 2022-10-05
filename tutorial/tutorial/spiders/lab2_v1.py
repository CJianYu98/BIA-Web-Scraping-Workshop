import scrapy
from scrapy_playwright.page import PageMethod

from ..items import OscarWinningFilmItem


# Oscar Winning film scrape records for year 2015
class PWSpider(scrapy.Spider):
    name = "pw_lab1"

    def start_requests(self):
        url = "https://www.scrapethissite.com/pages/ajax-javascript/"
        yield scrapy.Request(
            url,
            meta=dict(
                playwright=True,
                playwright_include_page=True,
                playwright_page_methods=[
                    PageMethod("click", "id=2015"),
                    PageMethod("wait_for_selector", ".film"),
                ],
                errback=self.errback,
                year=2015,
            ),
        )

    async def parse(self, response):
        page = response.meta["playwright_page"]
        year = response.meta["year"]

        for film in response.css(".film"):
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
