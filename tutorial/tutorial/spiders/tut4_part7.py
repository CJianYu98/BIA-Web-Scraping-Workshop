import logging

import scrapy
from scrapy_playwright.page import PageMethod

from ..utils import should_abort_request


# Improving Scrapy performance by setting custom settings, abort unnecessary requests, on Lazada website
class LazadaSpider(scrapy.Spider):
    name = "pw_lazada"
    page_number = 1

    custom_settings = {
        # "PLAYWRIGHT_DEFAULT_NAVIGATION_TIMEOUT": "100000",
        "PLAYWRIGHT_ABORT_REQUEST": should_abort_request,
    }

    def start_requests(self):
        yield scrapy.Request(
            url="https://www.lazada.com.my/shop-laptops-gaming/",
            meta={
                "playwright": True,
                "playwright_page_methods": [
                    # PageMethod("wait_for_selector", '[data-tracking="product-card"]'),
                    PageMethod("wait_for_selector", ".RfADt a"),
                ],
            },
        )

    def parse(self, response):
        # products_selector = response.css('[data-tracking="product-card"]')
        products_selector = response.css(".RfADt a")

        for product in products_selector:
            print(response.url)
            # link = response.urljoin(product.xpath(".//a[text()]/@href").get())
            link = response.urljoin(product.css("a::attr(href)").get())
            yield scrapy.Request(link, callback=self.parse_product, meta={"playwright": False})

        if self.page_number < 2:
            self.page_number += 1
            page_2_url = response.urljoin(f"?page={self.page_number}")

            yield scrapy.Request(
                page_2_url,
                meta={
                    "playwright": True,
                    "playwright_page_methods": [
                        # PageMethod("wait_for_selector", '[data-tracking="product-card"]'),
                        PageMethod("wait_for_selector", ".RfADt a"),
                    ],
                },
            )

    def parse_product(self, response):
        yield {
            "Product": response.css(".pdp-mod-product-badge-title::text").get(),
            "Price": response.css(".pdp-price_color_orange::text").get(),
        }
