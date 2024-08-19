from flask import Blueprint, render_template, request
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Use a non-GUI backend
import matplotlib.pyplot as plt
import io
import base64
from app.utils import execute_sql_query
import os
print(os.path.abspath('app/static'))


main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET', 'POST'])
def index():
    error_message = None
    img_str = None
    if request.method == 'POST':
        file = request.files.get('file')
        query = request.form.get('sql_query')
        visualization_type = request.form.get('visualization_type')

        if file and query:
            df = pd.read_csv(file)
            result_df = execute_sql_query(df, query)
            if not result_df.empty:
                img = generate_plot(result_df, visualization_type)
                img_str = base64.b64encode(img).decode('utf-8')
            else:
                error_message = "No data found or SQL query is invalid."

    return render_template('index.html', img_data=img_str, error_message=error_message)

def generate_plot(df, visualization_type):
    fig, ax = plt.subplots()
    if visualization_type == 'table':
        ax.axis('off')
        table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')
    elif visualization_type == 'line':
        df.plot(kind='line', ax=ax)
    elif visualization_type == 'bar':
        df.plot(kind='bar', ax=ax)
    elif visualization_type == 'pie':
        df.plot(kind='pie', ax=ax, subplots=True)
    else:
        ax.text(0.5, 0.5, 'Unsupported Visualization Type', horizontalalignment='center', verticalalignment='center')
    plt.tight_layout()
    img = io.BytesIO()
    plt.savefig(img, format='png')
    plt.close(fig)
    img.seek(0)
    return img.read()
