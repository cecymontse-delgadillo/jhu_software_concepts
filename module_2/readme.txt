Name: Cecilia Delgadillo Olvera (cdelga15@jhu.edu)  

Module Info:  

    Name: Module 2 - Web Scraping 

    Assignment: Practice scraping data from websites 

    Due date: June 01, 2025 

 1. Approach 

A Python The goal of this project is to scrape graduate school admission results from TheGradCafe, extract relevant applicant information, clean and structure the data, and finally save it in JSON format. 

1.1 High-Level Architecture 

The architecture is divided into three primary modules: 

    Scraper Module (BaseScraper and GrandCafeApplicantScraper) 

    Cleaner Module (BaseCleaner and GrandCafeApplicantScraperCleaner) 

    Model Module (Applicant) 

Each module is designed with inheritance and separation of concerns, enabling flexibility, reuse, and easy customization. 

    Scraper (Base class) → GrandCafeApplicantScraper (Specialized implementation) 

    ScrapeCleaner (Base class) → GrandCafeApplicantScraperCleaner (Specialized implementation) 

 

 1.2 Algorithms & Implementation Details 

 Design Patterns & Principles 

    Inheritance & Abstraction: 

    Scraper and Cleaner base classes define interfaces, encouraging DRY and reusable design. 

    Encapsulation: 

    Each class is responsible for one logical piece of functionality. 

    Separation of Concerns: 

    Scraping and cleaning responsibilities are separated for maintainability and clarity. 

1.2.1 Scraping Web Pages - with Pagination support 

    A base Scraper class encapsulates the logic for making HTTP requests and saving raw HTML content. 

    It uses urllib3.PoolManager for efficient connection reuse. 

    GrandCafeApplicantScraper inherits from Scraper and implements the logic for iterating through paginated pages of GradCafe search results. 

    HTML content is fetched using get_page, and all pages are parsed until either a maximum page limit, or no more results are found. 

    Fetched HTML is saved using save_raw_data for later processing. 

1.2.2 Cleaning and Structuring the Data  

    ScrapeCleaner defines the basic interface and I/O methods for loading and saving data. 

    GrandCafeApplicantScraperCleaner inherits from ScrapeCleaner and implements the clean_data method. 

1.2.2.1 Algorithmic Flow in clean_data  

    HTML rows (<tr>) are grouped based on their structure into logical blocks representing one applicant. 

    Each group is converted to an Applicant object with fields like program, university, date_added, status, comments, etc. 

    Optional metadata (e.g., GRE, GPA, nationality) is extracted using text parsing and regex. 

    An applicant's URL is extracted from the anchor tag using BeautifulSoup's find method with a lambda-based filter. 

    Each Applicant instance is converted to a JSON dictionary with the to_json() method, omitting empty fields. 

This design promotes reusability, modularity, and easy extensibility for scraping or cleaning other web sources in the future. 

 

1.2.3 Data Modeling and Transformation 

    Applicant class: 

    Represents a single application record. 

    Includes a to_json() method that serializes non-empty fields. 

    Allows clean JSON output for further analysis or storage. 

 

2. Known bugs 

    Skip some records: In case an applicant record doesn’t have at least 4 ‘<td>’ blocks, it will skip that record.  

 