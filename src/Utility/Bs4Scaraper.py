import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json

def scrape_with_bs4(start_url,elements=None):

    if elements is None:
        elements = {
            'product-title': 'div.main-title h1 span',
            'product-price': 'div.new-price span',
            'product-description': 'div.main div p',
            'product-rate': 'div.heading span.small span',
            'product-no-of-reviews': 'div.heading span.small span'
        }

    results = []

    def parse_page(url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html5lib')

        # Extract product links and follow them
        product_links = [a['href'] for a in soup.select('div.product-item strong.product-title a')]
        for link in product_links:
            product_url = urljoin(url,link)
            parse_product_page(product_url)

        # Extract pagination links and follow them
        next_pages = [a['href'] for a in soup.select('div.psControls.paging a')]
        for next_page in next_pages:
            next_page_url = urljoin(url,next_page)
            parse_page(next_page_url)

    def parse_product_page(url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html5lib')

        product_title = soup.select_one(elements['product-title'])
        product_price = soup.select(elements['product-price'])
        product_description = soup.select(elements['product-description'])
        product_rate = soup.select_one(elements['product-rate'])
        product_no_of_reviews = soup.select(elements['product-no-of-reviews'])

        results.append({
            'product-title': product_title.text if product_title else None,
            'product-price': [span.text for span in product_price[:2]] if product_price else None,
            'product-description': [p.text for p in product_description] if product_description else None,
            'product-rate': product_rate.text if product_rate else None,
            'product-no-of-reviews': product_no_of_reviews[1].text if product_no_of_reviews and len(product_no_of_reviews) > 1 else None,
        })

    parse_page(start_url)

    return results