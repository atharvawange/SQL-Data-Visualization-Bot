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
- **Convert SQL Queries into Visualized Data:** Automatically generate visualizations based on SQL queries.
- **Upload and Process Files:** Supports CSV and Excel file uploads for data processing.
- **Dynamic Data Visualization:** Choose from various visualization types such as tables, line charts, bar charts, and pie charts.
- **Responsive Front-End:** Built with HTML and CSS for a user-friendly interface.
- **Flask-Powered Back-End:** Manages data and API interactions using Flask.

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

```bash
git clone https://github.com/atharvawange/SQL_DataVisualization_Bot.git
cd SQL_DataVisualization_Bot
```
Set Up Virtual Environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
```
Install Dependencies:

```bash
pip install -r requirements.txt
```
Set Up Environment Variables:

Create a .env file in the root directory and add any necessary environment variables (if applicable).

Run the Application:

```bash
python app/app.py
```

## Usage
**1. Access the Web Interface:**

Open your browser and go to http://localhost:5000.

**2. Upload Data:**

Upload a CSV or Excel file through the web interface.

**3. Enter a SQL Query:**

Type a SQL Query to describe the data you want to query.

**4. Select Visualization Type:**

Choose the desired visualization format (e.g., table, line chart, bar chart, pie chart).

**5. View Results:**

The application will display the generated SQL query and the corresponding data visualization.

## API Endpoints
- POST /upload: Upload a CSV or Excel file.
- POST /generate-sql: Generate SQL query from a natural language prompt.
- POST /visualize: Visualize data based on the generated SQL query.

## References
This project utilizes several third-party libraries and resources. For further information or to extend functionality, the following links may be useful:

Flask - The micro web framework used for the back-end.
Pandas - A powerful data analysis and manipulation library.
Matplotlib - A plotting library for creating static, interactive, and animated visualizations.
