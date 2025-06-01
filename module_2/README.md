# GradCafe Scraper

A Python project that scrapes graduate school admission results from TheGradCafe and parses the data into structured JSON.

## Features

 - Scrapes paginated search results from TheGradCafe.
 - Extracts structured applicant data (e.g. university, program, GRE scores, GPA, etc.).
 - Saves raw HTML and cleaned JSON data.

## Project Structure
```
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
```

## Requirements

 * Python 3.10+
 * Beautifulsoup4 4.13.4+
 * urllib3

## Instructions

1. Clone the repository:
```bash
git clone https://github.com/cecymontse-delgadillo/jhu_software_concepts.git
cd jhu_software_concepts/module_2/
```

2. (Optional) Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Scraping Raw HTML

```bash
python scrape.py
```

This saves raw HTML data into grandcafe_scrape_raw_data.html.

### Cleaning Data

```bash
python clean.py
```
This processes the HTML and saves cleaned applicant data to applicant_data.json.

### Customizing the Scraper

You can change the search filters by modifying the base URL in scrape.py:

base_url = "https://www.thegradcafe.com/survey/?q=&sort=newest&institution=&program=&degree=&season=&decision=&decision_start=YYYY-MM-DD"

## Notes

* Be respectful to TheGradCafe's servers: do not hammer requests, and use delays.

# Contact
cdelga15@jhu.edu


