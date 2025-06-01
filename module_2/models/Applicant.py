"""
Applicant.py  - Applicant defined module
-------------------------------------------------
This module defines the `Applicant` class, which represents a structured format
for applicant data scraped from TheGradCafe website.

Features:
 - The class is designed to store key information about each applicant
 - Offers a to_json() function that has as an output a JSON-compatible dictionary representation with empty fields omitted.
"""
class Applicant:
    # Initializes Applicant.
    def __init__(self, program='', university='', date_added='', url='', status='', term='', nationality='', gre='', gre_v='', degree='', gpa='', gre_aw='', comments=''):
        self.program = f"{program}, {university}"
        self.comments = comments
        self.date_added = date_added
        self.url = url
        self.status = status
        self.term = term
        self.nationality = nationality
        self.gre = gre
        self.gre_v = gre_v
        self.gpa = gpa
        self.gre_aw = gre_aw
        self.degree = degree
        

    # Function to create a json representation of the object. Converts onject to dict and omit any field that is empty
    def to_json(self):
        return {k:v for k, v in self.__dict__.items() if v}