from psycopg import connect, Connection
from psycopg_pool import ConnectionPool
from contextlib import contextmanager

class DatabaseUtils: 
    def __init__(self, db_config, minconn=1, maxconn=5):
        self.db_config = db_config
        try: 
            self.pool = ConnectionPool(conninfo=db_config, min_size=minconn, max_size=maxconn)
        except Exception as e:
            print(f"Error creating connection pool: {e}")

    @contextmanager
    def get_db_connection(self):
        with self.pool.connection() as conn:
            yield conn
        
    
    def create_table(self, create_table_sql):
        try: 
            conn = self.get_db_connection()
            with conn.cursor() as cur:
                cur.execute(create_table_sql)
                conn.commit()
                print("Table created succesfully")
        except Exception as e:
            print(f"Error executing query: {e}")
    #Drop table
    def drop_table(self, table_name):
        try: 
            conn = self.get_db_connection()
            with conn.cursor() as cur:
                cur.execute(f'DROP TABLE IF exists {table_name};')
                conn.commit()
                print("Table dropped succesfully")
        except Exception as e:
            print(f"Error executing query: {e}")

    #function to update, insert, or delete queries
    def execute_query(self, query, params):
        try: 
            conn = self.get_db_connection()
            with conn.cursor() as cur:
                    cur.execute(query, params)
                    conn.commit()
        except Exception as e:
            print(f"Error executing query: {e}")
    
    #function to select queries
    def execute_query(self, query, params):
        try: 
            conn = self.get_db_connection()
            with conn.cursor() as cur:
                    cur.execute(query, params)
                    return cur.fetchall()
        except Exception as e:
            print(f"Error executing query: {e}")

