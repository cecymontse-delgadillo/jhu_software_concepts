import psycopg

class DatabaseUtils: 
    def __init__(self, dbname, user, password):
        self.dbname = dbname
        self.user = user
        self.password = password

    def get_db_connection(self):
        connection = psycopg.connect(
            dbname=self.dbname,
            user=self.user,
            password= self.password
        )
        return connection
    

