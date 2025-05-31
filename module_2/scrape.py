from urllib.request import urlopen
from bs4 import BeautifulSoup
from base_scrape import Scraper


class GrandCafeScraper(Scraper):
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
    scraper = GrandCafeScraper("https://www.thegradcafe.com/survey/?q=Masters")
    data = scraper.scrape_data()
    scraper.save_raw_data("/Users/montsedelgadilloolvera/Documents/Masters/Summer 2025/ModernSoftwareConceptsPython/Assignments/jhu_software_concepts/","grandcafe_scrape_raw_data.html", str(data))
