import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser

from ..items import QuotesTutorialItem


class QuoteSpider(scrapy.Spider):
    name = "quotes"

    start_urls = ["https://quotes.toscrape.com"]
    # start_urls = ["https://quotes.toscrape.com/login"]
    # start_urls = ["https://www.amazon.sg/gp/bestsellers/electronics/ref=zg_bs_pg_1?ie=UTF8&pg=1"]
    # start_urls = ["https://quotes.toscrape.com/js/"]

    def parse(self, response):
        ### CSS Selector
        t1 = response.css("title::text").extract()
        t2 = response.css("title::text").extract()[0]
        t3 = response.css("title::text").extract_first()
        t4 = response.css("span.text::text").extract()[0]
        t5 = response.css("div.quote::text").extract()

        yield {"1": t1, "2": t2, "3": t3, "4": t4, "5": t5}

        ### Xpath
        # t1 = response.xpath("//title/text()").extract()
        # t2 = response.xpath(
        #     '//*[contains(concat( " ", @class, " " ), concat( " ", "header-box", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "col-md-4", " " ))]//a/text()'
        # ).extract()
        # t3 = response.css("li.next a").xpath("@href").extract()  # both css and xpath
        # t4 = response.css("a").xpath("@href").extract()  # both css and xpath

        # yield {"1": t1, "2": t2, "3": t3, "4": t4}

        ### Get all titles, authors, tags
        # items = QuotesTutorialItem()

        # all_div_quotes = response.css("div.quote")

        # for quotes in all_div_quotes:
        #     title = quotes.css("span.text::text").extract()
        #     author = quotes.css(".author::text").extract()
        #     tag = quotes.css(".tag::text").extract()

        #     items["title"] = title
        #     items["author"] = author
        #     items["tag"] = tag

        #     yield items

        # tags = response.css("div.tags")
        # for t in tags:
        #     print(type(t))
        #     print(t.css("a.tag::text").extract())
        #     print(type(t.css("a.tag").extract()))
        #     break

        ### Web Crawling and following links
        # next_page = response.css("li.next a::attr(href)").get()

        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)

        ### Login
        # token = response.css("form input::attr(value)").get()
        # return FormRequest.from_response(
        #     response,
        #     formdata={"csrf_token": token, "username": "abc", "password": "password"},
        #     callback=self.start_scraping,
        # )

        ### Amazon Best Seller Scraping
        # t1 = response.css("._cDEzb_p13n-sc-css-line-clamp-3_g3dy1::text").getall()
        # yield {"t1": t1}

    # def start_scraping(self, response):
    #     open_in_browser(response)
    #     items = QuotesTutorialItem()

    #     all_div_quotes = response.css("div.quote")

    #     for quotes in all_div_quotes:
    #         title = quotes.css("span.text::text").extract()
    #         author = quotes.css(".author::text").extract()
    #         tag = quotes.css(".tag::text").extract()

    #         items["title"] = title
    #         items["author"] = author
    #         items["tag"] = tag

    #         yield items
