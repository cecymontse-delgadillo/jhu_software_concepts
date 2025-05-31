from base_clean import ScrapeCleaner
from bs4 import BeautifulSoup

class GrandCafeScraperCleaner(ScrapeCleaner):
        
    def clean_data(self, data):
        try: 
            soup = BeautifulSoup(data, 'html.parser')
            rows =  soup.find_all('tr')
            results = []
            for row in rows:
                print(row)
                cols = row.find_all('td')
                if len(cols) >=4:
                    result = {
                        'program': f"{cols[2].get_text(strip=True)},{cols[1].get_text(strip=True)}",
                        #'comments': cols[6].get_text(strip=True),
                        'date_added': cols[3].get_text(strip=True),
                        'url': "https://...",
                        'status': f"{cols[4].get_text(strip=True)}",
                    }
                    results.append(result)
            return results
        except Exception as e:
            print(f"Error cleaning scraped information: {e}")
            return []
        

if __name__ == "__main__":
    cleaner = GrandCafeScraperCleaner("/Users/montsedelgadilloolvera/Documents/Masters/Summer 2025/ModernSoftwareConceptsPython/Assignments/jhu_software_concepts/grandcafe_scrape_raw_data.html")
    raw_data = cleaner.load_data()
    cleaned_results = cleaner.clean_data(raw_data)
    cleaner.save_data(cleaned_results,"applicant_data.json")