from textwrap import dedent
from crewai import Task
from crewai.task import TaskOutput
from crewai.tasks.output_format import OutputFormat
from crewai.project import output_json
from pydantic import BaseModel
from typing import List

# Define a Pydantic model for each product item
class ProductItemModel(BaseModel):
    product_title: str
    product_price: str
    product_description: str
    product_rate: str
    product_no_of_reviews: str

# Define the model for the output which is a list of products
class ScrapedDataModel(BaseModel):
    products: List[ProductItemModel]  # A list of product items

class ScrapeWebsiteTask():
    # def crawl_website_task(self, agent, URL):
    #     return Task(
    #         description=dedent(f"""\
    #                 Start from the provided base {URL} and collect every URL from the website.
    #                 Your final answer MUST be a list of all the URLs on the website.
    #             """ ),
    #         expected_output='A complete list of URLs from the website.',
    #         agent=agent,
    #         async_execution=False,
    #     )
    
    @output_json
    def scrape_website_task(self, agent, URL):
        return Task(
            description=dedent(f"""\
                Your objective is to scrape the necessary data from the provided website URL. The data you collect should be relevant to the purpose specified below and must be accurate and well-structured.

                Steps:

                Navigate to the URL: Use the provided URL to access the website.{URL}
                Identify Key Data Elements: Determine the specific data that needs to be extracted based on the provided requirements. This could include text, images, tables, or any other content visible on the page.
                Scrape the Data: Efficiently extract the identified data while ensuring no crucial information is missed. If the website requires interaction (e.g., clicking, scrolling), make sure to handle these appropriately.
                """),
            expected_output=dedent("""Your final answer MUST be a structured data file containing the scraped data in [JSON/CSV/etc.] 
                format, ready for further processing or analysis.
                Example Output:
                {
                    {
                        "product-title": "Product Title",
                        "product-price": "Product Price",
                        "product-description": "Product Description",
                        "product-rate": "Product Rate",
                        "product-no-of-reviews": "Product No. of Reviews"
                    },
                    {{...}}
                }
                                   
                """),
            agent=agent,
            async_execution=False,
            output_json=ScrapedDataModel
        )
        # Identify the Key pages: use the above base URL and identify the key pages that need to be scraped.(Example: https://www.example.com/category-name2/product-id1, https://www.example.com/category-name3/product-id12)