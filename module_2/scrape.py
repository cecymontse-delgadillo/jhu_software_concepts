from urllib.request import urlopen
from bs4 import BeautifulSoup

def scrape_data(): 
    url = "https://www.thegradcafe.com/survey/?q=Masters"
    try:
        page = urlopen(url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        results = soup.find_all("tbody", class_="tw-divide-y tw-divide-gray-200 tw-bg-white")
        #text = soup.get_text()
        #spaceless_text = text.replace("\n\n","")
        print(results)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    scrape_data()
