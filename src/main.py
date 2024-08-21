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

    tasks = ScrapeWebsiteTask()
    agent = ScrapeWebsiteAgent()

    # Create agents
    # web_crawler_agent = agent.crawler_agent()
    web_scraper_agent = agent.scrape_agent()

    # Create tasks
    # crawl_website_task = tasks.crawl_website_task(web_crawler_agent,url)
    scrape_website_task = tasks.scrape_website_task(web_scraper_agent,url)

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
    else:
        print("No valid JSON data to save")


if __name__ == "__main__":
    main()