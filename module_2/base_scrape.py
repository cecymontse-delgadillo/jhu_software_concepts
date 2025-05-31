import json

# Base scraper class
class Scraper:
    def __init__(self, base_url):
        self.base_url = base_url

    def scrape_data(self):
        raise NotImplementedError("Subclases must implement this function")
    
    def save_data(self,data,filename):
        with open(filename,'w', encoding='utf-8') as f:
            json.dump(data,f, ensure_ascii=False, indent=4)
        print(f"Raw data from {self.base_url} saved to {filename}")