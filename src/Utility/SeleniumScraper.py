from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_with_selenium(start_url):
    results = []
    
    # Set up the Selenium WebDriver (e.g., using Chrome)
    driver = webdriver.Chrome()  # Make sure you have ChromeDriver installed and in your PATH

    def parse_page(url):
        driver.get(url)

        # Wait until the products are loaded
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.product-item strong.product-title a')))

        # Extract product links and follow them
        product_links = [a.get_attribute('href') for a in driver.find_elements(By.CSS_SELECTOR, 'div.product-item strong.product-title a')]
        for link in product_links:
            parse_product_page(link)

        # Extract pagination links and follow them
        next_pages = [a.get_attribute('href') for a in driver.find_elements(By.CSS_SELECTOR, 'div.psControls.paging a')]
        for next_page in next_pages:
            parse_page(next_page)

    def parse_product_page(url):
        driver.get(url)

        # Wait until the product title is loaded
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.main-title h1 span')))

        product_title = driver.find_element(By.CSS_SELECTOR, 'div.main-title h1 span').text
        product_price = [span.text for span in driver.find_elements(By.CSS_SELECTOR, 'div.new-price span')[:2]]
        product_description = [p.text for p in driver.find_elements(By.CSS_SELECTOR, 'div.main div p')]
        product_rate = driver.find_element(By.CSS_SELECTOR, 'div.heading span.small span').text
        product_no_of_reviews = driver.find_elements(By.CSS_SELECTOR, 'div.heading span.small span')
        product_no_of_reviews = product_no_of_reviews[1].text if len(product_no_of_reviews) > 1 else None

        results.append({
            'product-title': product_title,
            'product-price': product_price,
            'product-description': product_description,
            'product-rate': product_rate,
            'product-no-of-reviews': product_no_of_reviews,
        })

    parse_page(start_url)
    driver.quit()

    return results