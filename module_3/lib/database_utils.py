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
            with self.get_db_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(create_table_sql)
                    conn.commit()
                    print("Table created succesfully")
        except Exception as e:
            print(f"Error executing query: {e}")
    #Drop table
    def drop_table(self, table_name):
        try: 
            with self.get_db_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(f'DROP TABLE IF exists {table_name};')
                    conn.commit()
                    print("Table dropped succesfully")
        except Exception as e:
            print(f"Error executing query: {e}")

    #function to update, insert, or delete queries
    def execute_query(self, query, params):
        try: 
            if params and isinstance(params, dict):
                params = {k:v for k, v in params.items()}
            with self.get_db_connection() as conn:
                with conn.cursor() as cur:
                        cur.execute(query, params)
                        conn.commit()
                        print(f"Query executed {query}")
        except Exception as e:
            print(f"Error executing query: {e}")
    

    
    #function to select queries
    def get_query(self, query, params):
        try: 
            with self.get_db_connection() as conn:
                with conn.cursor() as cur:
                        cur.execute(query, params)
                        return cur.fetchall()
        except Exception as e:
            print(f"Error executing query: {e}")

    #Overload: Function fo select queries without params
    def get_query(self, query):
        try: 
            with self.get_db_connection() as conn:
                with conn.cursor() as cur:
                        cur.execute(query)
                        return cur.fetchall()
        except Exception as e:
            print(f"Error executing query: {e}")

