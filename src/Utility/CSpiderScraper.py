import scrapy
from scrapy.crawler import CrawlerProcess
from urllib.parse import urlparse
from scrapy.signalmanager import dispatcher
from scrapy import signals

class CSpiderSpider(scrapy.Spider):
    name = "c_spider"

    def __init__(self, start_url, *args, **kwargs):
        super(CSpiderSpider, self).__init__(*args, **kwargs)
        self.start_urls = [start_url]
        self.allowed_domains = [urlparse(start_url).netloc]
        self.scraped_data = []

    def parse(self, response):
        for link in response.css('div.product-item strong.product-title a::attr(href)').getall():
            yield response.follow(link, callback=self.parse_categories)

        next_pages = response.css('div.psControls.paging a::attr(href)').getall()
        for next_page in next_pages:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(next_page_url, callback=self.parse)

    def parse_categories(self, response):
        product_data = {
            'product-title': response.css('div.main-title h1 span::text').get(),
            'product-price': response.css('div.new-price span::text').getall()[:2],
            'product-description': response.css('div.main div p::text').getall(),
            'product-rate': response.css('div.heading span.small span::text').getall()[0] if response.css('div.heading span.small span::text').getall() else None,
            'product-no-of-reviews': response.css('div.heading span.small span::text').getall()[1] if len(response.css('div.heading span.small span::text').getall()) > 1 else None,
        }
        self.scraped_data.append(product_data)

def run_spider(user_url):
    # Capture the scraped data in-memory using Scrapy signals
    process = CrawlerProcess()

    spider = CSpiderSpider(start_url=user_url)
    dispatcher.connect(spider_closed, signal=signals.spider_closed)
    
    # Start the crawling process
    process.crawl(spider)
    process.start()

    return spider.scraped_data

# Handler for the signal when the spider closes
def spider_closed(spider):
    print("Spider closed, scraping complete.")