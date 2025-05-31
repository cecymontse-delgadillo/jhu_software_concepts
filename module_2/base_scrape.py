import os

# Base scraper class
class Scraper:
    def __init__(self, base_url):
        self.base_url = base_url

    def scrape_data(self):
        raise NotImplementedError("Subclases must implement this function")
    
    def save_data(self):
        raise NotImplementedError("Subclases must implement this function")


    def save_raw_data(self, directory, filename, content):
        try:
            # Create the directory if it doesn't exist
            if not os.path.exists(directory):
                os.makedirs(directory)
                print(f"Directory '{directory}' created.")
            else:
                print(f"Directory '{directory}' already exists.")

            # Define the full file path
            file_path = os.path.join(directory, filename)

            with open(file_path, "w") as file:
                file.write(content)
                print(f"File '{filename}' written to directory '{directory}'.")
            return file_path
        except Exception as e:
            print(f"File '{filename}' not created {e}")