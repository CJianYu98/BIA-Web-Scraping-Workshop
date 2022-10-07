import scrapy
from ..items import ImageItem


# Downloading all Images
class ParisImagesSpider(scrapy.Spider):
    name = "tut3_spider3_5"
    start_urls = ["https://en.wikipedia.org/wiki/Paris"]

    def parse(self, response):
        raw_image_urls = response.css(".image img ::attr(src)").getall()

        for img_url in raw_image_urls:
            # Using Item Class
            item = ImageItem()
            # print(response.urljoin(img_url))
            item["title"] = response.urljoin(img_url).split("/")[-1]
            item["image_urls"] = [
                response.urljoin(img_url)
            ]  # Get the absolute url path, must be a List

            yield item

        #     # If we do not use Item Class
        #     title = response.urljoin(img_url).split("/")[-1]
        #     image_urls = [response.urljoin(img_url)]  # Get the absolute url path

        #     yield {"title": title, "image_urls": image_urls}
