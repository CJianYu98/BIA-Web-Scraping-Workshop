import scrapy
from ..items import BookItem
from scrapy.loader import ItemLoader


class BookspiderSpider(scrapy.Spider):
    name = 'bookspider'
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):        
        book_list = response.css('article.product_pod')
        
        for book in book_list :
            loader = ItemLoader(item = BookItem(),selector = book)
            
            loader.add_css('title', 'h3 a::attr(title)')
            loader.add_css('price', 'p.price_color')
            
            
            # title = book.css('h3 a').attrib['title'] 
            # price = book.css('p.price_color::text').get()
            
            # items['title'] = title
            # items['price'] = price
           
        
            yield loader.load_item()
