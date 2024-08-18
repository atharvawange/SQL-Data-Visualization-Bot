from flask import Flask, request, render_template, send_file
import pandas as pd
import matplotlib.pyplot as plt
from utils import execute_query, generate_visualization
from model import generate_sql
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'app/data/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            return file_path

@app.route('/query', methods=['POST'])
def query():
    prompt = request.form['prompt']
    file_path = request.form['file_path']
    
    # Generate SQL from prompt
    sql_query = generate_sql(prompt)
    
    # Execute SQL and get the result
    df = execute_query(file_path, sql_query)
    
    # Generate visualization
    viz_type = request.form['viz_type']
    output_path = generate_visualization(df, viz_type)
    
    return send_file(output_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
