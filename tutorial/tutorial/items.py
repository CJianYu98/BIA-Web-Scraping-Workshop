# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotesTutorialItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    author = scrapy.Field()
    tag = scrapy.Field()


class OscarWinningFilmItem(scrapy.Item):
    year = scrapy.Field()
    title = scrapy.Field()
    nominations = scrapy.Field()
    awards = scrapy.Field()
    best_picture = scrapy.Field()
