"""
base_scraper.py - Base scraper module
-------------------------------------------------
This module defines a base class `Scraper` that provides foundational tools for building web scrapers.
Classes:
    Scraper: Provides specific implementation for get_page() and save_raw_data(). 
    A subclass for `Scraper` will need to implement specific scraping logic.
Features:
    - Uses `urllib3` and a connection pool. 
    - It supports pagination and includes a utility to save raw HTMLScraping logic and data persistence.
    - It saves raw html data in html file for later cleanup
Dependencies:
    - os
    - urllib3
"""
import os
from urllib3 import PoolManager

# Base scraper class
class Scraper:
    # Initialize the scraper with a base URL(str) and request delay(int, optional).
    def __init__(self, base_url, delay=1):
        # URL without page number appended
        self.base_url = base_url 
        # Delay between requests to avoid hammering the server 
        self.delay = delay 
        # Use a connection pool       
        self.http = PoolManager()  

    # Abstract method to be implemented by subclasses for scraping logic.
    def scrape_data(self):
        raise NotImplementedError("Subclases must implement this function")

    # Fetch a specific page number from the target site.
    def get_page(self, page_number):
        url = f"{self.base_url}&page={page_number}"
        response = self.http.request('GET', url)
        if response.status == 200:
            return response.data.decode("utf-8")
        
    # Save raw HTML content to a file in the current working directory.
    def save_raw_data(self, filename, content):
        try:
            directory= os.getcwd()
            # Create the directory if it doesn't exist
            if not os.path.exists(directory):
                os.makedirs(directory)
                print(f"Directory '{directory}' created.")
            else:
                print(f"Directory '{directory}' already exists.")

            # Define the full file path
            file_path = os.path.join(directory, filename)

            with open(file_path, "w") as file:
                file.write(content)
                print(f"File '{filename}' written to directory '{directory}'.")
            return file_path
        except Exception as e:
            print(f"File '{filename}' not created {e}")