import scrapy
from scrapy_playwright.page import PageMethod

from ..items import OscarWinningFilmItem


# Oscar Winning film scrape all the years
class PWSpider(scrapy.Spider):
    name = "pw_lab2"

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
        link = "https://www.scrapethissite.com/pages/ajax-javascript/"

        page = response.meta["playwright_page"]
        years = response.css(".year-link::text").getall()

        for year in years:
            yield scrapy.Request(
                f"{link}#{year}",
                callback=self.parse_table,
                meta=dict(
                    playwright=True,
                    playwright_include_page=True,
                    playwright_page_methods=[
                        # PageMethod("click", f"id={year}"),
                        PageMethod("wait_for_selector", ".film"),
                    ],
                    errback=self.errback,
                    year=year,
                ),
            )

        # for film in response.css(".film"):
        #     oscar_film_item = OscarWinningFilmItem()
        #     oscar_film_item["title"] = film.css(".film-title::text").get()
        #     oscar_film_item["nominations"] = film.css(".film-nominations::text").get()
        #     oscar_film_item["awards"] = film.css(".film-awards::text").get()
        #     oscar_film_item["best_picture"] = (
        #         "Yes" if film.css(".film-best-picture i").get() else "No"
        #     )
        #     yield oscar_film_item

        # await page.click("h3+ .year-link")
        # await page.click("id=2014")
        # await page.wait_for_selector("th")
        # await page.wait_for_timeout(3000)

        # await page.close()

    async def parse_table(self, response):
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
