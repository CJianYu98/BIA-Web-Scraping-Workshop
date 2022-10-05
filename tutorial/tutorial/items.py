# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst


def extract_country_name(value):
    return "".join(value).strip()


class QuotesTutorialItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    tag = scrapy.Field()


class CountryItem(scrapy.Item):
    name = scrapy.Field(
        input_processor=MapCompose(extract_country_name), output_processor=TakeFirst()
    )
    capital = scrapy.Field(output_processor=TakeFirst())
    population = scrapy.Field(output_processor=TakeFirst())
    area = scrapy.Field(output_processor=TakeFirst())


class OscarWinningFilmItem(scrapy.Item):
    year = scrapy.Field()
    title = scrapy.Field()
    nominations = scrapy.Field()
    awards = scrapy.Field()
    best_picture = scrapy.Field()
