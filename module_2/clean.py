from base_clean import ScrapeCleaner
from Applicant import Applicant
from bs4 import BeautifulSoup
import re


class GrandCafeApplicantScraperCleaner(ScrapeCleaner):
        
    def clean_data(self, data):
        try: 
            soup = BeautifulSoup(data, 'html.parser')
            rows =  soup.find_all('tr')
            applicants =[]
            temp_group_tr = []

            for i, row in enumerate(rows):
                row_class = row.get('class')
                
                #Start of a new applicant - <tr> without class
                if not row_class:
                    if temp_group_tr:
                        applicants.append(temp_group_tr)
                        temp_group_tr=[]
                    temp_group_tr.append(row)
                elif 'tw-border-none' in row_class:
                    temp_group_tr.append(row)
                    next_class = rows[i + 1].get('class') if i + 1 < len(rows) else None
                    if not next_class or 'tw-border-none' not in next_class:
                        applicants.append(temp_group_tr)
                        temp_group_tr = []

            # Append the last group if any
            if temp_group_tr:
                applicants.append(temp_group_tr)

            results = []
            for group in applicants:
                # Combine HTML rows
                applicant_html = ''.join(str(row) for row in group)
                applicant_soup = BeautifulSoup(applicant_html, 'html.parser')
                basic_data = applicant_soup.find_all('td')
                # Skip if essential columns are missing
                if len(basic_data) < 4:
                    continue 
                # Applicant optional tags
                tags = applicant_soup.select('div div')
                # Comments
                comments = applicant_soup.find('p')

                # Extract fields program and dregree with Regex
                text_lines = re.findall(r'[^\n\r]+', basic_data[1].get_text())
                program = text_lines[0] if len(text_lines) > 0 else ''
                degree = text_lines[1] if len(text_lines) > 1 else ''
                 # Find applicant URL with suffix and strip the fragment
                url = f"https://www.thegradcafe.com{applicant_soup.find('a', href=lambda href: href and href.startswith("/result/"))['href']}"

                #Create an Applicant instance
                applicant = Applicant(
                    program=program,
                    university=basic_data[0].get_text(strip=True),
                    date_added=basic_data[2].get_text(strip=True),
                    url=url,  
                    status=basic_data[3].get_text(strip=True),
                    degree=degree,
                    comments=comments.get_text(strip=True).replace("\n", " ").replace("\t", "") if comments else ''
                    #comments = re.sub()
                )
                # Extract metadata from tags
                for tag in tags:
                    text = tag.get_text(strip=True)
                    if 'GRE V' in text:
                        applicant.gre_v = text
                    elif 'GRE AW' in text:
                        applicant.gre_aw = text
                    elif 'GRE' in text:
                        applicant.gre = text
                    elif 'GPA' in text:
                        applicant.gpa = text
                    elif 'International' in text or 'American' in text:
                        applicant.nationality = text
                    else:
                        applicant.term = text

                results.append(applicant.to_json())
            return results
        except Exception as e:
            print(f"Error cleaning scraped information: {e}")
            return []


if __name__ == "__main__":
    cleaner = GrandCafeApplicantScraperCleaner("grandcafe_scrape_raw_data.html")
    raw_data = cleaner.load_data()
    cleaned_results = cleaner.clean_data(raw_data)
    cleaner.save_data(cleaned_results,"applicant_data.json")