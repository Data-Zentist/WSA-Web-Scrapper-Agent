from crewai_tools import ScrapeWebsiteTool,SeleniumScrapingTool
from langchain.tools import tool
from Utility.Bs4Scaraper import scrape_with_bs4
from Utility.SeleniumScraper import scrape_with_selenium
import subprocess
import os

class Tools():
    # @tool("scrape_website")
    # def scrape_website_tool(website_url):
    #     """Scrapes the content of the specified website."""
    #     return ScrapeWebsiteTool(website_url)
    
    @tool("scrape_website_bs4")
    def scrape_with_bs4_tool(website_url):
        """Scrapes the content of the specified website. using beautifulSoap4"""
        result = scrape_with_bs4(website_url)
        return result  


    @tool("scrape_website_selenium")
    def selanium_scaraper_tool(website_url,css_element='.main-content'):
        """Scrapes the content of the specified website. using selenium"""
        # return SeleniumScrapingTool(website_url,css_element)
        return scrape_with_selenium(website_url)

    @tool("scrape_website_spider")
    def run_scrapy_spider_tool(start_url):
        """Scrapes the content of the specified website. using spider"""
        # Run the scrapy spider using subprocess and capture the output
        scrapy_project_dir = 'F:\DataZentist\Task1\my_scraper'
        src_project_dir='F:\DataZentist\Task1'

        os.chdir(scrapy_project_dir)

        result = subprocess.run(
            ['scrapy', 'crawl', 'c_spider', '-a', f'start_url={start_url}'],
            capture_output=True, text=True
        )
        os.chdir(src_project_dir)
    
        return result
    
    def tools():
        return [
            Tools.run_scrapy_spider_tool,
            Tools.selanium_scaraper_tool,
            Tools.scrape_with_bs4_tool
            # Tools.crawl_website_tool
        ]
    
