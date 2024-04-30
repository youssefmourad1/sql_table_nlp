
<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p>

<h3 align="center">SQL File Processor API</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/your-username/sql-file-processor-api.svg)](https://github.com/your-username/sql-file-processor-api/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/your-username/sql-file-processor-api.svg)](https://github.com/your-username/sql-file-processor-api/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> A simple Flask API to extract and process trading information from SQL files.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [TODO](../TODO.md)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

This project is designed to facilitate the extraction of trading data from SQL INSERT statements into a structured CSV format. It uses a Flask-based REST API to accept SQL files, processes them to find relevant trading commands and parameters, and outputs the results in an easy-to-use CSV file.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them:

```bash
Python 3
pip
Flask
Pandas
```

### Installing

A step by step series of examples that tell you how to get a development environment running:

Clone the repo:
```
git clone https://github.com/your-username/sql-file-processor-api.git
cd sql-file-processor-api
```

Install the required packages:
```
pip install -r requirements.txt
```

Start the server:
```
python app.py
```

## 🔧 Running the tests <a name = "tests"></a>

Explain how to run the automated tests for this system. For now, tests can be manual:

### Break down into end to end tests

Test the entire system by uploading a test SQL file through your chosen API client (e.g., Postman or curl).

```bash
curl -X POST -F "file=@path_to_your_test_file.sql" http://localhost:5000/process_sql
```

### And coding style tests

Ensure your code adheres to PEP8 standards:

```bash
flake8
```

## 🎈 Usage <a name="usage"></a>

After starting the server, use the following endpoint to process SQL files:

- **POST /process_sql**: Upload an SQL file to be processed. Returns the path to the output CSV.

## 🚀 Deployment <a name = "deployment"></a>

For deployment on a live system, consider using Gunicorn as the WSGI server with Nginx as the reverse proxy. Refer to the deployment section above for details on setting this up on a server.

## ⛏️ Built Using <a name = "built_using"></a>

- [Flask](https://flask.palletsprojects.com/) - Server Framework
- [Pandas](https://pandas.pydata.org/) - Data Manipulation Library
- [Gunicorn](https://gunicorn.org/) - WSGI Server

## ✍️ Authors <a name = "authors"></a>

- [@your-username](https://github.com/your-username) - Idea & Initial work

See also the list of [contributors](https://github.com/your-username/sql-file-processor-api/contributors) who participated in this project.

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Hat tip to anyone whose code was used
- Inspiration
- References to any articles, papers, or software used
```

This README is a comprehensive guide to your project, making it easier for others to

 understand and contribute. Adjust as necessary for the specifics of your project, including adding any additional documentation or examples as needed.