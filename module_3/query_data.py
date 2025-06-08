from lib.database_utils import DatabaseUtils
from models.Question import Question, Questionaries

class GrandCafeAnalysis: 
    def execute_analysis(self):
        conninfo = "postgresql:///grandcafedatabase"
        db = DatabaseUtils(conninfo, 5, 10)
        questionary = []
        question_1 = Question(
            question= "How many entries do you have in your database who have applied for Spring 2025?",
            query = "SELECT COUNT(*) FROM Applicants WHERE term = 'Spring 2025';",
            query_description= "Using a Select statement with a count(*) function will return the number of rows in Applicants matches the criterion. " \
            "In this case the term we are looking is 'Spring 2025'",
            answer=" Applicant count: {}"
        )
        question_2 =Question(
            question= "What percentage of entries are from international students (not American or Other) (to two decimal places)? ",
            query = "SELECT CAST((ROUND ((COUNT(*)*100.0)/ (SELECT COUNT(*) FROM Applicants),2)) AS FLOAT) AS Percentage FROM Applicants WHERE US_OR_INTERNATIONAL <> 'American';",
            query_description= "This query calculates the percentage of non-American applicants by leveraging a nested SELECT statement. " \
            "The inner query computes the total number of applicants, while the outer query calculates the percentage of non-Americans by dividing the count of non-American applicants by the total number of applicants and multiplying by 100.0. " \
            "The result is rounded to 2 decimal places and labeled as 'Percentage'. To ensure accurate decimal representation, we cast the result to a float, avoiding any potential Decimal object notation in the output.",
            answer=" Percent International: {}"
        )
        question_3 =Question(
            question= "What is the average GPA, GRE, GRE V, GRE AW of applicants who provide these metrics?",
            query = "SELECT CAST(ROUND(AVG(gpa)::NUMERIC, 2) AS FLOAT) as GPA_avg, CAST(ROUND(AVG(gre)::NUMERIC, 2) AS FLOAT) as GRE_avg, CAST(ROUND(AVG(gre_v)::NUMERIC,2) AS FLOAT) as GRE_V_avg, CAST(ROUND(AVG(gre_aw)::NUMERIC,2) AS FLOAT) as GRE_AW_avg FROM Applicants;",
            query_description= "This query calculates the average of GPA, GRE, GRE_V, and GRE_AW using a SELECT statement with the AVG function. " \
            "To ensure precise results, the AVG function is cast to NUMERIC, and the ROUND function is applied to limit the output to 2 decimal places. " \
            "Finally, the result is cast to a float to guarantee accurate decimal representation and avoid Decimal object notation in the output.",
            answer=" Averate GPA: {}, Average GRE: {}, Average GRE V: {}, Average GRE AW: {}"

        )
        question_4 =Question(
            question= "What is their average GPA of American students in Spring 2025?",
            query = "SELECT CAST(ROUND(AVG(gpa)::NUMERIC,2) AS FLOAT) as GPA_avg FROM Applicants WHERE term = 'Spring 2025' AND US_OR_INTERNATIONAL = 'American'; ",
            query_description= "This query calculates the average GPA of American students in Spring 2025. Using a SELECT statement with the AVG function," \
            " it computes the average GPA and rounds the result to 2 decimal places using the ROUND function. " \
            "To ensure accurate calculations, the AVG result is cast to NUMERIC, and the result is cast to a float to guarantee precise decimal representation.",
            answer=" Averate GPA American: {}"
        )
        question_5 =Question(
            question= "What percent of entries for Spring 2025 are Acceptances (to two decimal places)?",
            query = "SELECT CAST((ROUND ((COUNT(*)*100.0)/ (SELECT COUNT(*) FROM Applicants WHERE term = 'Spring 2025'),2)) AS FLOAT) AS Percentage FROM Applicants WHERE status ~* 'Accepted' AND term = 'Spring 2025';",
            query_description= "This query calculates the acceptance rate for Spring 2025 applicants. " \
            "A nested SELECT statement is used to count the total number of applicants and the number of applicants with an 'Accepted' status (case-insensitive). " \
            "The acceptance rate is then calculated and rounded to 2 decimal places using the ROUND function." \
            " Finally, the result is cast to a float to ensure precise decimal representation.",
            answer=" Acceptance percent: {}"
        )
        question_6 =Question(
            question= "What is the average GPA of applicants who applied for Spring 2025 who are Acceptances?",
            query = "SELECT CAST(ROUND(AVG(gpa)::NUMERIC,2) AS FLOAT) AS Average FROM Applicants WHERE status ~* 'Accepted' AND term = 'Spring 2025';",
            query_description= "This query calculates the average GPA of applicants who were accepted for the term Spring 2025. It uses the AVG() aggregation function to compute the mean GPA from applicants whose status" \
            "The status matches 'Accepted' using a case-insensitive regular expression (~*), and term is 'Spring 2025'. It uses ROUND to display only two decimal places. ",
            answer=" Average GPA Acceptance: {}"
        )
        question_7 =Question(
            question= "How many entries are from applicants who applied to JHU for a masters degrees in Computer Science?",
            query = "SELECT COUNT(*) FROM Applicants WHERE program ~* 'JHU' OR program ~* 'Johns Hopkins' AND degree ='Masters' AND program ~* 'Computer Science';",
            query_description= "This query counts the number of applicants who applied to a Master's program in Computer Science at Johns Hopkins University. " \
            "The program field must match either 'JHU' or 'Johns Hopkins' using case-insensitive regular expressions (~*). The degree must be 'Masters'." \
            " The program must also include 'Computer Science' (again using case-insensitive regex).",
            answer=" JHU Masters Computer Science count: {}"
        )

        questionary.append(question_1)
        questionary.append(question_2)
        questionary.append(question_3)
        questionary.append(question_4)
        questionary.append(question_5)
        questionary.append(question_6)
        questionary.append(question_7)
        for question in questionary:
            answer = db.get_query(question.get_query())
            question.update_answer(answer)
        return questionary
    

if __name__ == "__main__":
    gc_analysis = GrandCafeAnalysis()
    Questionaries(gc_analysis.execute_analysis()).to_doc("query_data.txt")





