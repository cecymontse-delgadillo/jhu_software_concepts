## GradCafe Scraper

A Python project that scrapes graduate school admission results from TheGradCafe and parses the data into structured JSON.

#Features

 - Scrapes paginated search results from TheGradCafe.
 - Extracts structured applicant data (e.g. university, program, GRE scores, GPA, etc.).
 - Saves raw HTML and cleaned JSON data.

# Project Structure

.
├── lib
│   ├── base_scrape.py         # Generic base scraper class using urllib3
│   └── base_clean.py          # Generic base cleaner class
├── models
│   ├── Applicant.py           # Applicant data model
├── data
│   ├── grandcafe_scrape_raw_data.html           # Last scrape html data
├── scrape.py      # Scraper implementation for GradCafe
├── clean.py       # Cleaner for extracted GradCafe applicant data
├── applicant_data.jason       # JSON format Applicant data with +10K resultsgit
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation

Requirements

Python 3.7+

Install dependencies:

pip install -r requirements.txt

Usage

Scraping Raw HTML

python grandcafe_scraper.py

This saves raw HTML data into grandcafe_scrape_raw_data.html.

Cleaning Data

python grandcafe_cleaner.py

This processes the HTML and saves cleaned applicant data to applicant_data.json.

Customizing the Scraper

You can change the search filters by modifying the base URL in grandcafe_scraper.py:

base_url = "https://www.thegradcafe.com/survey/?q=&sort=newest&institution=&program=&degree=&season=&decision=&decision_start=YYYY-MM-DD"

Notes

Be respectful to TheGradCafe's servers: do not hammer requests, and use delays.

This scraper is intended for educational and personal use.

License

MIT License


