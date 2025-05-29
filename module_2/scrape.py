from urllib.request import urlopen
from bs4 import BeautifulSoup

def scrape_data(): 
    URL = "https://e-catalogue.jhu.edu/course-search"
    try:
        page = urlopen(URL)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text()
        print(text)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    scrape_data()
