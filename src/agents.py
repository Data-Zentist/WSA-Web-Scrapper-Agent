from textwrap import dedent
from crewai import Agent
from tools import Tools
from langchain_groq import ChatGroq
import os

class ScrapeWebsiteAgent():

    def __init__(self):
        self.llm = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model=os.getenv("GROQ_MODEL_NAME")
        )

    # def crawler_agent(self):
    #     return Agent(
    #         role='Web Crawler',
    #         goal='Collect all URLs from the provided base URL.',
    #         tools=[Tools.crawl_website_tool],
    #         backstory="You are an efficient web crawler designed to extract every URL from a given website.",
    #         verbose=True,
    #         llm=self.llm
    #     )

    def scrape_agent(self):
        return Agent(
            role="Scrape Website Agent",
            goal='Scrape the necessary data from the provided website URL.The data you collect should be relevant to the purpose specified and must be accurate and well-structured.',
            tools=[
                Tools.run_scrapy_spider_tool,
                Tools.scrape_with_bs4_tool,
                Tools.selanium_scaraper_tool
                ],
            backstory=dedent(f"""\
                As a Scraper Specialist, your mission is to efficiently and accurately extract relevant data from the provided website URL. 
                This involves navigating the webpage, identifying and capturing the necessary information, 
                and storing it in a structured format for easy access and further processing. 
                You should ensure the data is comprehensive, clean, and adheres to the task's specific requirements, 
                while respecting the website's terms of service and minimizing any impact on the website's performance.
                """),
            verbose=True,
            llm=self.llm
        )