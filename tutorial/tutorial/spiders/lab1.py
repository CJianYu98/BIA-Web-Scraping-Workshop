import scrapy
from scrapy.loader import ItemLoader

from ..items import CountryItem


class Countriespider(scrapy.Spider):
    name = "lab1_spider"

    start_urls = ["https://www.scrapethissite.com/pages/simple/"]

    def parse(self, response):
        countries = response.css(".country")

        for country in countries:
            loader = ItemLoader(item=CountryItem(), selector=country)
            loader.add_css("name", ".country-name::text")
            loader.add_css("capital", ".country-capital::text")
            loader.add_css("population", ".country-population::text")
            loader.add_css("area", ".country-area::text")

            # c["name"] = country.css(".country-name::text").getall()
            # c["capital"] = country.css(".country-capital::text").get()
            # c["population"] = country.css(".country-population::text").get()
            # c["area"] = country.css(".country-area::text").get()

            yield loader.load_item()
