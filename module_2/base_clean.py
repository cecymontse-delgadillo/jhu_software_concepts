import json

class ScrapeCleaner:
    
    def __init__(self, raw_data_filepath):
        self.raw_data_filepath = raw_data_filepath
    
    def load_data(self):
        try:
            # Attempt to open and read the file
            with open(self.raw_data_filepath, "r") as file:
                content = file.read()
            return content
        except FileNotFoundError:
            print(f"Error: The file '{self.raw_data_filepath}' does not exist.")
        except PermissionError:
            print(f"Error: You do not have permission to read the file '{self.raw_data_filepath}'.")
        except Exception as e:
            # Catch other unforeseen errors
            print(f"An unexpected error occurred: {e}")

    def clean_data(self):
        raise NotImplementedError("Subclases must implement this function")


    def save_data(self, data, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Data saved to {filename}")