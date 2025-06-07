from lib.database_utils import DatabaseUtils

db = DatabaseUtils("grandcafedatabase", "montsedelgadilloolvera", "")


def create_applicants_table():
    db.create_table()

def load_grandcafe_data():

