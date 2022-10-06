from email.quoprimime import quote
import scrapy


class QuotespiderSpider(scrapy.Spider):
    name = "quotespider1_1"
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        # quote_list = response.css("div.quote")
        quote_list = response.xpath('//div[@class="quote"]')
        for quote in quote_list:
            # Using CSS selector
            title = quote.css("span.text::text").get().replace("\u201c", "").replace("\u201d", "")

            author = quote.css("small.author::text").get()

            tags_ls = quote.css("a.tag")
            tags = [tag.css("::text").get() for tag in tags_ls]
            # tags = quote.css('meta.keywords').attrib['content']

            # Using Xpath
            # title = quote.xpath('span[@class="text"]/text()').get()
            # author = quote.xpath('span/small[@class="author"]/text()').get()
            # tags = quote.xpath("div[@class='tags']/a[@class='tag']/text()").getall()

            #     # Create a dictionary of information that we want our from one product
            yield {"title": title, "author": author, "tags": tags}
