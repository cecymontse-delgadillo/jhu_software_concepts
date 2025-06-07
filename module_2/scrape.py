"""
scrape.py - Grand Cafe Specialized Scraper module 
-------------------------------------------------
This script defines a specialized scraper class for The GradCafe survey results page.
Features:
- Inherits from a generic Scraper base class.
- Uses BeautifulSoup to parse and extract rows of application data from multiple
paginated web pages. Parsing HTML content to collect <tr> elements from the survey table
- Saves raw scraped data to a local HTML file.
- Includes basic error handling for scraping failures.

Usage:
   $ python scrape.py
"""
from bs4 import BeautifulSoup
import time
from lib.base_scrape import Scraper


class GrandCafeApplicantScraper(Scraper):
    # Specific implementation for GrandCafeApplicantScraper.
    # Scrapes data from multiple paginated survey result pages
    def scrape_data(self): 
        try:
            page_count = 1
            results=[]

            while True:
                html = self.get_page(page_count)
                # Loop will stop once we don't have a valid html or the "No admissions found! str is found"
                if not html or (html.find("No admissions found!") != -1):
                    break
                soup = BeautifulSoup(html, "html.parser")
                rows = soup.select('table tbody tr')
                results.extend(rows)
                page_count += 1
                time.sleep(self.delay)
            return results
        except Exception as e:
            print(f"Error during scraping: {e}")
            return []

# Main execution: creates URL search, scrapes and saves raw data
if __name__ == "__main__":
    # Base URL with placeholders for parameters
    base_url = "https://www.thegradcafe.com/survey/?q={query}&sort={sort}&institution={institution}&program={program}&degree={degree}&season={season}&decision={decision}&decision_start={decision_start}&decision_end={decision_end}&added_start={added_start}&added_end={added_end}"

    # Parameters for filtering the scraping
    params = {
        "query": "", # Specific search
        "sort": "newest", 
        "institution": "", # i.e. Columbia University
        "program": "", # i.e. Economics
        "degree": "Masters", # i.e. Masters
        "season": "", # i.e. Fall 2025
        "decision": "", # i.e. Accepted or Rejected or Interviewed or Wait listed
        "decision_start": "2024-06-01", # format yyyy-mm-dd
        "decision_end": "", # format yyyy-mm-dd
        "added_start": "", # format yyyy-mm-dd
        "added_end": "" # format yyyy-mm-dd
    }

    # Format base URL with parameter values
    # Note: This particular search will bring 536 pages. 
    # In general, each page has 20 applicants included. With this search we can get at least 10K entries    
    formatted_url = base_url.format(**params)
    
    # Initialize scraper and run scraping
    scraper = GrandCafeApplicantScraper(formatted_url)
    data = scraper.scrape_data()

    # Save scraped data to a local file
    scraper.save_raw_data("grandcafe_scrape_raw_data.html", str(data))
