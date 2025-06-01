from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
from base_scrape import Scraper


class GrandCafeApplicantScraper(Scraper):
    def scrape_data(self): 
        try:
            page_count = 1
            results=[]

            while page_count<=500:
                html = self.get_page(page_count)
                if not html:
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
        


if __name__ == "__main__":
    scraper = GrandCafeApplicantScraper("https://www.thegradcafe.com/survey/?q=&sort=newest&institution=&program=&degree=&season=&decision=&decision_start=2024-06-01&decision_end=&added_start=&added_end=")
    data = scraper.scrape_data()
    scraper.save_raw_data("grandcafe_scrape_raw_data.html", str(data))
