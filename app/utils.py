import pandas as pd
import sqlite3

def execute_sql_query(df, query):
    conn = sqlite3.connect(':memory:')  # In-memory SQLite database
    df.to_sql('data', conn, index=False, if_exists='replace')
    
    try:
        result_df = pd.read_sql_query(query, conn)
    except pd.io.sql.DatabaseError as e:
        result_df = pd.DataFrame()  # Return an empty DataFrame on error
        print(f"SQL Query Error: {e}")
    
    conn.close()
    return result_df
