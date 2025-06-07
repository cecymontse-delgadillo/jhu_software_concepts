class Question:
    # Initializes Applicant.
    def __init__(self, question:str, answer: str, query:str):
        self.question= question
        self.answer = answer
        self.query = query

class Questionaries: 
    def __init__(self, question_list):
        self.questions = question_list
