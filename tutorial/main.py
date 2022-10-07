from scrapy.utils.project import get_project_settings

from tutorial.spiders.tut1_part1 import QuotespiderSpider
from tutorial.spiders.tut2_part1 import BookspiderSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def main():
    settings = get_project_settings()
    process = CrawlerProcess(settings)  # apply project settings to both Spider
    # process = CrawlerProcess()

    process.crawl(QuotespiderSpider)
    process.crawl(BookspiderSpider)
    process.start()  # both spiders will crawl at the same time


if __name__ == "__main__":
    main()
