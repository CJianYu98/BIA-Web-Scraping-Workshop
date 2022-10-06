# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst

from .utils import (
    extract_courts_product_curr_price,
    extract_courts_product_old_price,
    extract_courts_product_price_currency,
    process_country_name,
    process_courts_product_name,
    remove_currency
)


class QuotesTutorialItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    tag = scrapy.Field()

#Tut 2 part 3
class BookItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field(input_processor = MapCompose(remove_tags) , output_processor = TakeFirst())
    price = scrapy.Field(input_processor = MapCompose(remove_tags,remove_currency) , output_processor = TakeFirst())

class CountryItem(scrapy.Item):
    name = scrapy.Field(
        input_processor=MapCompose(process_country_name), output_processor=TakeFirst()
    )
    capital = scrapy.Field(output_processor=TakeFirst())
    population = scrapy.Field(output_processor=TakeFirst())
    area = scrapy.Field(output_processor=TakeFirst())


class CourtsItem(scrapy.Item):
    name = scrapy.Field(
        input_processor=MapCompose(process_courts_product_name), output_processor=TakeFirst()
    )
    curr_price = scrapy.Field(
        input_processor=MapCompose(extract_courts_product_curr_price), output_processor=TakeFirst()
    )
    old_price = scrapy.Field(
        input_processor=MapCompose(extract_courts_product_old_price), output_processor=TakeFirst()
    )
    currency = scrapy.Field(
        input_processor=MapCompose(extract_courts_product_price_currency),
        output_processor=TakeFirst(),
    )


class OscarWinningFilmItem(scrapy.Item):
    year = scrapy.Field()
    title = scrapy.Field()
    nominations = scrapy.Field()
    awards = scrapy.Field()
    best_picture = scrapy.Field()
