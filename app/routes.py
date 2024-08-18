from flask import Blueprint, request, render_template, jsonify
from .model import generate_sql
from .utils import execute_query, generate_visualization

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/generate-sql', methods=['POST'])
def get_sql():
    data = request.json
    prompt = data.get('prompt')
    sql_query = generate_sql(prompt)
    return jsonify({'sql_query': sql_query})

@main.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file_format = file.filename.split('.')[-1]
    
    if file_format == 'csv':
        df = pd.read_csv(file)
    elif file_format in ['xls', 'xlsx']:
        df = pd.read_excel(file)
    else:
        return jsonify({'error': 'Unsupported file format'}), 400

    chart_type = request.form.get('chart_type', 'line')
    sql_query = request.form.get('sql_query', None)

    if sql_query:
        df = execute_query(sql_query)

    img_base64 = generate_visualization(df, chart_type)
    return jsonify({'image': img_base64})
