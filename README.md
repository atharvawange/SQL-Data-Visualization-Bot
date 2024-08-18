# Data Query and Visualization Web Application

This project provides a web application that allows users to upload data (in CSV or Excel format), generate SQL queries using natural language prompts, and visualize the results. The project utilizes the Hugging Face model `defog/sqlcoder2` for converting prompts into SQL queries.

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [References](#references)

## Features
- Convert natural language prompts into SQL queries.
- Upload and process CSV or Excel files.
- Visualize data using Pandas and Matplotlib.
- Responsive front-end built with HTML and CSS.
- Powered by Flask for the back-end and API.

## Project Structure
```plaintext
.
├── app/
│   ├── templates/
│   │   ├── index.html        # Front-end HTML template
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css    # CSS for styling
│   ├── __init__.py           # Initialize Flask app
│   ├── main.py               # Main entry point for running the app
│   ├── model.py              # Hugging Face model logic for generating SQL
│   ├── utils.py              # Utility functions for executing SQL and visualizing data
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation

Installation

Clone the Repository:
bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name

Set Up Virtual Environment:
bash
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate

Install Dependencies:
bash
pip install -r requirements.txt

Set Up Environment Variables:
Create a .env file in the root directory and add any necessary environment variables (if applicable).

Run the Application:
bash
python main.py
Usage
Access the Web Interface:
Open your browser and go to http://localhost:5000.

Upload Data:
Upload a CSV or Excel file through the web interface.

Enter a Prompt:
Type a natural language prompt describing the data you want to query.

Select Visualization Type:
Choose the desired visualization (e.g., table, line chart, bar chart, pie chart).

View Results:
The application will display the generated SQL query and the corresponding data visualization.

API Endpoints
POST /upload: Upload a CSV or Excel file.
POST /generate-sql: Generate SQL query from natural language prompt.
POST /visualize: Visualize data based on the generated SQL query.

References
This project makes use of several third-party libraries and resources. If you're looking to understand or extend the functionality, you may find the following links helpful:

[Flask](#https://flask.palletsprojects.com/en/3.0.x/) - The micro web framework used for the back-end.
[Pandas](#https://pandas.pydata.org/) - A powerful data analysis and manipulation library.
[Matplotlib](https://matplotlib.org/) - A plotting library used for creating static, interactive, and animated visualizations.
[Hugging Face Transformers](https://huggingface.co/defog/sqlcoder2) - The library used for natural language processing and model integration.
[SQLAlchemy](https://www.sqlalchemy.org/) - A SQL toolkit and Object-Relational Mapping (ORM) library for Python.
[Bootstrap](https://getbootstrap.com/) - (Optional) If you used Bootstrap for CSS styling, you can include this.
[Jinja2](https://jinja.palletsprojects.com/en/2.10.x/) - The templating engine used with Flask to render HTML templates.
