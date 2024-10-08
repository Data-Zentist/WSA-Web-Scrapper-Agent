# 🌐 Web Scraper Project

This project is a powerful and flexible web scraper developed using Crew AI tools, designed to efficiently extract data from various websites. Leveraging the capabilities of BeautifulSoup, Selenium, and Scrapy, this scraper is built to handle a wide range of scraping tasks, from simple HTML parsing to dynamic content extraction.

## ✨ Features

- **Multi-Tool Integration**: Combines the strengths of BeautifulSoup, Selenium, and Scrapy to handle different types of web content.
- **Dynamic Content Handling**: Uses Selenium to interact with JavaScript-heavy websites, ensuring data is captured even when content is dynamically loaded.
- **Robust Parsing**: BeautifulSoup is employed for straightforward HTML parsing, ideal for sites with static content.
- **Scalable Scraping**: Scrapy’s framework allows for scalable and efficient data scraping, with the ability to handle multiple pages and complex site structures.
- **Customizable & Extensible**: Easily configurable to target specific websites, with options to add custom scraping rules and handling logic.

## 💼 Use Cases

- **Data Collection**: Ideal for gathering large datasets from web pages for analysis, research, or machine learning purposes.
- **Price Monitoring**: Can be adapted to track product prices across multiple e-commerce platforms.
- **Content Aggregation**: Useful for aggregating content from blogs, news sites, and other content-rich websites.

## 🚀 Getting Started

To get started with this web scraper:

1. **Clone the repository** to your local machine.
    ```bash
    git clone https://github.com/Data-Zentist/WSA-Web-Scrapper-Agent.git
    cd WSA-Web-Scrapper-Agent
    ```
2. **Create a new Python virtual environment** to ensure a clean workspace.
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3. **Install the required dependencies** listed in `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```
4. **Create a Groq API key** by signing up at [Groq](https://groq.com/).
5. **Configure the environment variables**:
    - Rename `.env.example` to `.env`.
    - Open the `.env` file and paste your Groq API key in the `GROQ_API_KEY` field.
    - Choose the desired model (e.g., `llama3-70b-8192`) and paste the model name in the `GROQ_MODEL_NAME` field.
    ```bash
    GROQ_API_KEY=your_api_key_here
    GROQ_MODEL_NAME=llama3-70b-8192
    ```
6. **Customize the scraper configuration** for your target websites.
7. **Run the scraper** using the provided scripts to start collecting data.
    ```bash
    python src/main.py
    ```
## ⚠️ Disclaimer

Please note that this project uses AI models developed by third parties. We do not claim responsibility for the performance, accuracy, or outputs generated by these models. The model and its outputs are provided "as is," without warranty of any kind. Users are advised to review and verify the outputs before using them in any application.

