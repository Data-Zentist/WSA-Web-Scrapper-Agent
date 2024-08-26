import scrapy
from scrapy.crawler import CrawlerProcess
from urllib.parse import urlparse
from scrapy.signalmanager import dispatcher
from scrapy import signals

class CSpiderSpider(scrapy.Spider):
    name = "c_spider"

    def __init__(self, start_url, elements=None, *args, **kwargs):
        super(CSpiderSpider, self).__init__(*args, **kwargs)
        self.start_urls = [start_url]
        self.allowed_domains = [urlparse(start_url).netloc]
        self.scraped_data = []

        if elements is None:
            elements = {
                'product-title': 'div.main-title h1 span::text',
                'product-price': 'div.new-price span::text',
                'product-description': 'div.main div p::text',
                'product-rate': 'div.heading span.small span::text',
                'product-no-of-reviews': 'div.heading span.small span::text'
            }

        self.elements = elements

    def parse(self, response):
        for link in response.css('div.product-item strong.product-title a::attr(href)').getall():
            yield response.follow(link, callback=self.parse_product)

        next_pages = response.css('div.psControls.paging a::attr(href)').getall()
        for next_page in next_pages:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(next_page_url, callback=self.parse)

    def parse_product(self, response):
        product_data = {
            'product-title': response.css(self.elements['product-title']).get(),
            'product-price': response.css(self.elements['product-price']).getall()[:2],
            'product-description': response.css(self.elements['product-description']).getall(),
            'product-rate': response.css(self.elements['product-rate']).getall()[0] if response.css(self.elements['product-rate']).getall() else None,
            'product-no-of-reviews': response.css(self.elements['product-no-of-reviews']).getall()[1] if len(response.css(self.elements['product-no-of-reviews']).getall()) > 1 else None,
        }
        self.scraped_data.append(product_data)

def run_spider(user_url, user_elements=None):
    process = CrawlerProcess()

    spider = CSpiderSpider(start_url=user_url, elements=user_elements)
    dispatcher.connect(spider_closed, signal=signals.spider_closed)
    
    # Start the crawling process
    process.crawl(spider)
    process.start()

    return spider.scraped_data

# Handler for the signal when the spider closes
def spider_closed(spider):
    print("Spider closed, scraping complete.")