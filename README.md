# Zywa Card Status API 🚀
[![Python3](https://img.shields.io/badge/made%20with-Python3-yellow?style=plastic&logo=python)](https://www.python.org/downloads/)
[![PostgreSQL](https://img.shields.io/badge/database%20with-postgres-blue?style=plastic&logo=postgresql)](https://www.postgresql.org/)
[![Flask](https://img.shields.io/badge/api%20with-flask-green?style=plastic&logo=flask)](https://flask.palletsprojects.com/en/3.0.x/)
<br>

Welcome to the Zywa Backend Engineer Assignment, where I contribute to the making card status checking a breeze! Whether you're the evaluator trying to find out how I implement the `/get_card_status`, or you're just geeking out over integrating APIs, you've come to the right place. 🎉

<details>
<summary>Table of Contents</summary>

- [Zywa Card Status API 🚀](#zywa-card-status-api-🚀)
  * [What's Inside 📦](#whats-inside-📦)
  * [Getting Started 🌱](#getting-started-🌱)
    + [Prerequisites](#prerequisites)
    + [Setup and Installation](#setup-and-installation)
  * [Running the Application 🎉](#running-the-application-🎉)
  * [Interacting with API 🎮](#interacting-with-api-🎮)
  * [Running with Docker 🐳 ](#running-with-docker-🐳)
    + [Prerequisites](#prerequisites-1)
    + [Build the Docker Image](#build-the-docker-image)
    + [Run the Container](#run-the-container)
    + [Access the Application](#access-the-application)
  * [Framework/Language Choice 🛠️](#frameworklanguage-choice-🛠️)
    + [Why Python and Flask?](#why-python-and-flask)
    + [Why PostgreSQL?](#why-postgresql)
  * [Architectural Decisions 🏛️](#architectural-decisions-🏛️)
    + [Data Handling and API Design](#data-handling-and-api-design)
  * [Possible Improvements ✨](#possible-improvements-✨)
  * [License 📜](#license-📜)
  * [Acknowledgements 👏🏾](#acknowledgements-👏🏾)

</details>


## What's Inside 📦

- `data/`: Contains all the CSV files with card status info.
- `static/`: Home to the stylish CSS and dynamic JavaScript files.
- `templates/`: Where the HTML files live, waiting to be rendered.
- `.env`: Well, it's a secret! (But not from you, environment variables live here.)
- `.gitignore`: The little guardian that keeps our secrets safe from Git.
- `card_status_api.py`: The heart of the assignment, serving up all the status info you need.
- `create_database.sql`: The blueprint for the database.
- `db_config.py`: Holds the keys to the database kingdom.  
- `Dockerfile` : Ensures that everyone, everywhere, can run our app in the same environment.    
- `populate_database.py`: Fills the database with all the initial data it needs to thrive.
- `README.md`: You're reading it!  
- `requirements.txt`: Lists all the necessary Python packages to ensure that the environment is replicated perfectly. Just like a recipe for the environment.  

## Getting Started 🌱

Follow these steps to get your own version of the card status api up and running:

### Prerequisites

Make sure you have these installed:
- Python 🐍 (3.8 or later preferred)
- PostgreSQL 🐘
- A sense of adventure 🧭

### Setup and Installation

1. **Clone this repository**:
    ```bash
    git clone https://github.com/Ozziekins/zywa
    cd zywa
    ```

2. **Create and activate a virtual environment** (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the requirements**:
    ```bash
    pip3 install -r requirements.txt
    ```

4. **Set up your environment variables**:
    - Copy the `.env.example` file to `.env` and customize its contents.

5. **Initialize the database**:
    - Run `create_database.sql` on your PostgreSQL server to create your database and tables.
    - Populate your database with initial data using `populate_database.py`.

## Running the Application 🎉

To launch the Zywa Card Status API, simply run:
```bash
python3 card_status_api.py
```

Then visit `http://127.0.0.1:5000` in your browser to interact with the web interface. 🎈  


## Interacting with API 🎮

- Web Interface: Easy-peasy. Just click on the "User Mobile" or "Card ID" button, follow the prompt, and voilà—status displayed!
- Command Line: For the tech-savvy, POST a JSON to /get_card_status with either user_contact or card_id. The API will do the rest. Here is a sample:  

```
curl -X POST http://localhost:5000/get_card_status -H "Content-Type: application/json" -d '{"user_mobile": "585949014"}'
```

or 

```
curl -X POST http://localhost:5000/get_card_status -H "Content-Type: application/json" -d '{"card_id": "ZYW8827"}'
```

## Running with Docker 🐳  

Running this Card Status API with Docker simplifies the setup process.

### Prerequisites
- Docker: Ensure you have Docker installed and running on your machine. Download it from [Docker's official site](https://www.docker.com/).

### Build the Docker Image

1. **Navigate to the Project Directory**: Open a terminal and make sure you are in the root directory of the Zywa project.

2. **Build the Image**: Run the following command to build your Docker image. Don't forget the dot at the end, representing the current directory!

   ```bash
   docker build -t zywa-card-status-api .
   ```

### Run the Container
After building the image, you can run your application inside a Docker container with the following command:

```bash
docker run -dp 5000:5000 zywa-card-status-api
```

### Access the Application
Open your favorite web browser and navigate to:

```bash
http://localhost:5000
```

You should now see the Card Status API web interface, ready for you to use!

## Framework/Language Choice 🛠️
### Why Python and Flask?
- Python: I chose it for its simplicity and because it has a ton of libraries, such as Pandas for CSV manipulation which I used. Also because well I am comfortable coding with python.   
- Flask: Super straightforward and and it's flexible enough to let the project grow organically if it needs to be expanded upon.  

### Why PostgreSQL?
- Reliable: As a relational databases it was a good options since the data structure seemed to be well-defined and relational.   
- Compliance: PostgreSQL can handle complex queries even though it's not the case for this particular api, it could be useful for expanding.  

## Architectural Decisions 🏛️
### Data Handling and API Design
- Separation: The application logic is separated from the data layer. I mean Flask routes handle HTTP requests, while database interactions are abstracted behind clear interfaces.   
- RESTful API: The API follows REST principles, easy to navigate for the internal tems, and makes getting what you need effortless.  

## Possible Improvements ✨
- Asynchronous Processing: With larger CSV files, processing the data asynchronously could improve performance.  
- Docker Compose: The way I implemented it now uses Docker for deploying rhe application but doesn't handle the database part. But with Docker Compose, both the application and database containers would simplify configuration and make everything work together even smoother.  

## License 📜
This project is proudly licensed under the MIT License. For more details, see the LICENSE file.

## Acknowledgements 👏🏾
- Flask for the web server magic.
- PostgreSQL for database wizardry.
- The open-source community for inspiration and support.

Thank you for viewing my submission for Backend Engineer Assignment at Zywa! 🌈