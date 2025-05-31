from urllib.request import urlopen
from bs4 import BeautifulSoup
from base_scrape import Scraper

class GrandCafeScraper(Scraper):
    def scrape_data(self): 
        try:
            page = urlopen(self.base_url)
            html = page.read().decode("utf-8")
            soup = BeautifulSoup(html, "html.parser")
            tbody = soup.find("tbody", class_="tw-divide-y tw-divide-gray-200 tw-bg-white")
            if tbody:
                results = tbody.find_all('tr')
            return results
        except Exception as e:
            print(f"Error during scraping: {e}")
            return []

if __name__ == "__main__":
    scraper = GrandCafeScraper("https://www.thegradcafe.com/survey/?q=Masters")
    data = scraper.scrape_data()
    scraper.save_data(data, "raw_results.json")
