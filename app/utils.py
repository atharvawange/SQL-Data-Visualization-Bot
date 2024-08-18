import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from sqlalchemy import create_engine

# Example database URL
DATABASE_URL = "sqlite:///example.db"  # Replace with your actual database URL
engine = create_engine(DATABASE_URL)

def execute_query(query):
    with engine.connect() as connection:
        result = pd.read_sql_query(query, connection)
    return result

def generate_visualization(df, chart_type="line"):
    fig, ax = plt.subplots()
    if chart_type == "line":
        df.plot(kind="line", ax=ax)
    elif chart_type == "bar":
        df.plot(kind="bar", ax=ax)
    elif chart_type == "pie":
        df.plot(kind="pie", ax=ax, y=df.columns[0])
    else:
        df.plot(kind="table", ax=ax)
    
    # Save to a BytesIO object
    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close(fig)
    img.seek(0)
    img_base64 = base64.b64encode(img.getvalue()).decode('utf-8')
    
    return img_base64
