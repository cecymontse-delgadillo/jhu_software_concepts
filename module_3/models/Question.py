import os
class Question:
    # Initializes Applicant.
    def __init__(self, question,query, query_description, answer):
        self.question= question
        self.query = query
        self.query_description = query_description
        self.answer = answer

    def update_answer(self, values):
        self.answer = self.answer.format(*values)
    
    def get_query(self):
        return self.query
    
    def to_string(self):
        response = f"** {self.question} **\n Answer: {self.answer} \n Query Used: {self.query} \n Description: {self.query_description} \n"
        return response

class Questionaries: 
    def __init__(self, question_list):
        self.questions = question_list
    
    def to_doc(self, filename):
        try:
            directory= f"{os.getcwd()}/data/"
            # Create the directory if it doesn't exist
            if not os.path.exists(directory):
                os.makedirs(directory)
                print(f"Directory '{directory}' created.")
            else:
                print(f"Directory '{directory}' already exists.")

            # Define the full file path
            file_path = os.path.join(directory, filename)

            with open(file_path, "w") as file:
                for question in self.questions:
                    file.write("")
                    file.write(question.to_string())
                print(f"File '{filename}' written to directory '{directory}'.")
            return file_path
        except Exception as e:
            print(f"File '{filename}' not created {e}")

    

