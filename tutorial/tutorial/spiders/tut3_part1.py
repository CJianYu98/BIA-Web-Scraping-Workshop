import scrapy


class QuotespiderSpider(scrapy.Spider):
    name = "quotespider"
    start_urls = [
        "http://quotes.toscrape.com/",
        "https://quotes.toscrape.com/page/2/",
        "https://quotes.toscrape.com/page/3/",
    ]

    def parse(self, response):
        quote_list = response.css("div.quote")
        for quote in quote_list:
            title = quote.css("span.text::text").get().replace("\u201c", "").replace("\u201d", "")
            author = quote.css("small.author::text").get()
            tags = quote.css("meta.keywords").attrib["content"]

            # Create a dictionary of information that we want our from one product
            yield {"title": title, "author": author, "tags": tags}
