from dotenv import load_dotenv
from crewai import Crew
from task import ScrapeWebsiteTask
from agents import ScrapeWebsiteAgent
import pandas as pd
import json

def main():
    load_dotenv()

    print("## Welcome to the WebSite Scraping Crew")
    print('------------------------------------------')
    url = input("Enter URL: \n")

    # Ask the user if they want to provide custom elements to scrape
    # custom_elements = input("Do you want to provide custom elements to scrape? (yes/no): \n").lower()

    element_title = input("Enter the CSS selector for the product title (default: 'div.main-title h1 span'): \n") or 'div.main-title h1 span'
    element_price = input("Enter the CSS selector for the product price (default: 'div.new-price span'): \n") or 'div.new-price span'
    element_description = input("Enter the CSS selector for the product description (default: 'div.main div p'): \n") or 'div.main div p'
    element_rate = input("Enter the CSS selector for the product rating (default: 'div.heading span.small span'): \n") or 'div.heading span.small span'
    element_reviews = input("Enter the CSS selector for the number of reviews (default: 'div.heading span.small span'): \n") or 'div.heading span.small span'

    elements = {
        'product-title': element_title,
        'product-price': element_price,
        'product-description': element_description,
        'product-rate': element_rate,
        'product-no-of-reviews': element_reviews
    }

    tasks = ScrapeWebsiteTask()
    agent = ScrapeWebsiteAgent()

    # Create agents
    # web_crawler_agent = agent.crawler_agent()
    web_scraper_agent = agent.scrape_agent()

    # Create tasks
    # crawl_website_task = tasks.crawl_website_task(web_crawler_agent,url)
    scrape_website_task = tasks.scrape_website_task(web_scraper_agent,url,elements)

    # scrape_website_task.context = [crawl_website_task]

    crew = Crew(
        agents=[
            # web_crawler_agent,
            web_scraper_agent
            ], 
        tasks=[
            # crawl_website_task,
            scrape_website_task
            ],
        # max_rpm=29
        )

    result = crew.kickoff()

    if result.json_dict:

        df = pd.DataFrame(result.json_dict)  # Wrap json_data in a list to convert to DataFrame

        df.to_csv('output.csv', index=False)

    elif result:
        df = pd.DataFrame(result)  # Wrap json_data in a list to convert to DataFrame

        df.to_csv('output.csv', index=False)
    else:
        print("No valid JSON data to save")


if __name__ == "__main__":
    main()