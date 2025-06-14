# Grand Café Applicant Data Analysis

This project analyzes graduate school applicant data stored in a PostgreSQL database. It includes functionality for creating the database table, importing JSON data, and executing a series of analytical queries to summarize key insights.

## Project Structure

```
.
├── lib
│   ├── database_utils.py      # Database connection and query execution utilities
├── models
│   ├── Question.py            # Defines the Question and Questionaries classes
├── pages
│   ├── pages.py               # Route Definitions via Flask Blueprint
├── static
│   ├── style.css              # Basic CSS for analysis page
├── templates
│   ├── base.html              # This HTML file presents Grand Cafe Analysis backbone
│   ├── questions.html         # This HTML file extend base.html and defines a <div> where questions will be displayed
├── app.py                     # Application Factory for Grand Cafe Analysis
├── load_data.py               # Module to load data from JSON file to DB
├── query_data.pdf             # PDF file with a description of the queries requested in assignment
├── query_data.py              # Module responsible for executing analytical queries against the `Applicants` table in PostgreSQL database.
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

---

## Features

### Data Loading
- Loads applicant data from `applicant_data.json`.
- Creates the `Applicants` table with appropriate fields.
- Cleans and inserts the data into PostgreSQL using the `load_data.py` module.

###  Data Analysis
- Runs multiple predefined SQL queries to analyze:
  - Total applicants for Spring 2025
  - Percentage of international students
  - Averages for GPA and GRE metrics
  - Acceptance rates and filtered metrics
  - Specific program-level application insights (e.g., JHU MS in CS)

If executed directly using $ python query_data.py, results are formatted and saved to `query_data.txt`.

---

##  Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/cecymontse-delgadillo/jhu_software_concepts.git
cd jhu_software_concepts/module_3/
```
### 2. Set up PostgreSQL

Ensure PostgreSQL is installed and a database named grandcafedatabase exists:
```bash
    createdb grandcafedatabase
```
### 3. Install Python dependencies

This project uses the standard library only, but ensure your environment includes:
```bash
    pip install -r requirements.txt
```
## Usage

### Load data into the database

```bash
python load_data.py
```
This will:

   - Drop and recreate the Applicants table

   - Load and clean JSON data

   - Insert applicants into the database

### Run analysis as Flask App
This will:
    Execute predefined queries and populate a Flask app with the details

Option 1: 
```bash
python app.py 
```

Option 2: 
```bash
flask --app app.py run
```
Open your browser and go to:
http://127.0.0.1:5000

### Run analysis as script 

```bash
python query_data.py
```

This will:

    - Execute predefined queries

    - Write formatted answers to query_data.txt


# Query Topics

| Question         | Description                                        |
| ---------------- | -------------------------------------------------- |
| Applicant Count  | How many applicants applied for Spring 2025        |
| International %  | What % of applicants are not American              |
| GPA/GRE Averages | Average GPA, GRE, GRE\_V, GRE\_AW for all students |
| American GPA     | Average GPA of American applicants (Spring 2025)   |
| Acceptance Rate  | % of Spring 2025 applications that are accepted    |
| Accepted GPA     | GPA of accepted students (Spring 2025)             |
| JHU CS Count     | # of JHU Masters in CS applicants                  |


# Contact
cdelga15@jhu.edu