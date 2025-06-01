from urllib.request import urlopen
from bs4 import BeautifulSoup
from base_scrape import Scraper


class GrandCafeApplicantScraper(Scraper):
    def scrape_data(self): 
        try:
            page = urlopen(self.base_url)
            html = page.read().decode("utf-8")
            soup = BeautifulSoup(html, "html.parser")
            rows = soup.select('table tbody tr')
            return rows
        except Exception as e:
            print(f"Error during scraping: {e}")
            return []
        


if __name__ == "__main__":
    scraper = GrandCafeApplicantScraper("https://www.thegradcafe.com/survey/?q=Masters")
    data = scraper.scrape_data()
    scraper.save_raw_data("grandcafe_scrape_raw_data.html", str(data))
