# Data Query and Visualization Web Application

The DataViz App is a Flask web application that allows users to upload CSV or excel files, enter SQL queries, and visualize the resulting data. The visualizations can be in various formats, including tables, line charts, bar charts, and pie charts. This project uses Flask for the web framework, Pandas for data manipulation, Matplotlib for visualization, and SQLite for SQL query execution.

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [References](#references)

## Features
- Convert SQL queries into Visualized Data.
- Upload and process CSV or Excel files.
- Visualize data using Pandas and Matplotlib.
- Responsive front-end built with HTML and CSS.
- Powered by Flask for the back-end and API.

## Project Structure
```plaintext
.
├data_viz_app/
├── app/                      Contains the main application code.
│ ├── init.py                 Initializes the Flask app.
│ ├── app.py                  Entry point for the application.
│ ├── model.py                Loads and manages the Hugging Face model for SQL generation.
│ ├── routes.py               Defines the routes and logic for handling file uploads and SQL queries.
│ ├── utils.py                Contains utility functions for SQL execution and data visualization.
│ ├── templates/              HTML templates for the web application.
│ │ └── index.html            Main template file.
│ └── static/                 Static files like CSS and JavaScript.
│ └── CSS/                    Contains CSS files for styling.
│ └── style.css               Stylesheet for the application.
└── requirements.txt          Lists the Python dependencies for the project.Lists the Python dependencies for the project.
└── README.md                 Project documentation
```
## Installation

Clone the Repository:
bash
git clone [[https://github.com/yourusername/your-repo-name.git](https://github.com/atharvawange/SQL_DataVisualization_Bot.git)](https://github.com/atharvawange/SQL_DataVisualization_Bot.git)

cd SQL_DataVisualization_Bot

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
python app/main.py
Usage
Access the Web Interface:
Open your browser and go to http://localhost:5000.

Upload Data:
Upload a CSV or Excel file through the web interface.

Enter a SQL Query:
Type a SQL Query describing the data you want to query.

Select Visualization Type:
Choose the desired visualization (e.g., table, line chart, bar chart, pie chart).

View Results:
The application will display the generated SQL query and the corresponding data visualization.

## API Endpoints
POST /upload: Upload a CSV or Excel file.
POST /generate-sql: Generate SQL query from natural language prompt.
POST /visualize: Visualize data based on the generated SQL query.

### References

This project makes use of several third-party libraries and resources. If you're looking to understand or extend the functionality, you may find the following links helpful:

- [Flask](https://flask.palletsprojects.com/en/3.0.x/) - The micro web framework used for the back-end.
- [Pandas](https://pandas.pydata.org/) - A powerful data analysis and manipulation library.
- [Matplotlib](https://matplotlib.org/) - A plotting library used for creating static, interactive, and animated visualizations.
