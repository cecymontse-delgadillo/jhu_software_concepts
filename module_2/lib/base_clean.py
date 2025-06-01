"""
scrape.py - Base cleaner module 
-------------------------------------------------
This module provides a base class `ScrapeCleaner` that facilitates loading,
cleaning, and saving scraped raw data. It is intended to be subclassed for specific
cleaning logic by implementing the `clean_data()` method.

Usage:
    cleaner = ScrapeCleaner("path/to/raw_data.html")
    raw_content = cleaner.load_data()
    cleaned_data = cleaner.clean_data()  # Subclass must implement this
    cleaner.save_data(cleaned_data, "output.json")

"""
import json
import os

class ScrapeCleaner:
    
    def __init__(self, raw_data_filepath):
        self.raw_data_filepath = raw_data_filepath
    
    def load_data(self):
        try:
            # Attempt to open and read the file
            with open(self.raw_data_filepath, "r") as file:
                content = file.read()
            return content
        except FileNotFoundError as e:
            print(f"Error: The file '{self.raw_data_filepath}' does not exist. {e}")
        except PermissionError as e:
            print(f"Error: You do not have permission to read the file '{self.raw_data_filepath}'. {e}")
        except Exception as e:
            # Catch other unforeseen errors
            print(f"An unexpected error occurred: {e}")

    def clean_data(self):
        raise NotImplementedError("Subclases must implement this function")


    def save_data(self, data, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            # Cleans the existing file
            json.dump({},f)
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Data saved to {filename}. {f.name}")