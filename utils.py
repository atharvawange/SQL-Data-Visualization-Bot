import pandas as pd
import matplotlib.pyplot as plt
import sqlalchemy # type: ignore

def execute_query(file_path, query):
    # Load data into a Pandas DataFrame
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        df = pd.read_excel(file_path)
    
    # Create a SQLite in-memory database and load the DataFrame into it
    engine = sqlalchemy.create_engine('sqlite://', echo=False)
    df.to_sql('data', con=engine, index=False, if_exists='replace')
    
    # Execute the SQL query
    result_df = pd.read_sql_query(query, con=engine)
    
    return result_df

def generate_visualization(df, viz_type):
    output_path = 'app/static/plot.png'
    
    if viz_type == 'bar':
        df.plot(kind='bar')
    elif viz_type == 'line':
        df.plot(kind='line')
    elif viz_type == 'pie':
        df.plot(kind='pie', y=df.columns[0], autopct='%1.1f%%')
    else:
        df.plot(kind='table')
    
    plt.savefig(output_path)
    return output_path
