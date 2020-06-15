# Full Stack Trivia API Backend

This project is about a webpage to manage the trivia app and play the game. 
The project's plan was to develop an API and test suite that would implement a few features and functionality.


## Getting Started

## Back-End


### Installing Dependencies
#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 
NOTE: Make sure you create a database named trivia in the PostgreSQL server before running the tests.
API Documentation

## Front-End 
### Installing Dependencies

#### Installing Node and NPM

This project depends on Nodejs and Node Package Manager (NPM). Before continuing, you must download and install Node (the download includes NPM) from [https://nodejs.com/en/download](https://nodejs.org/en/download/).

#### Installing project dependencies

This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the `frontend` directory of this repository. After cloning, open your terminal and run:

```bash
npm install
```

>_tip_: **npm i** is shorthand for **npm install**


## Running Your Frontend in Dev Mode


Open [http://localhost:3000](http://localhost:3000) to view it in the browser. The page will reload if you make edits.<br>

```bash
npm start
```

## API documentation

### Getting Started
 Here we are going to document each endpoints and how to curl it.
 
 - Base URL: Currently this application is only hosted locally. The backend is hosted at http://127.0.0.1:5000/
 - Authentication: This version does not require authentication or API keys.
 
 ### Error Handling
 
 Errors are returned as JSON in the following format:
 
 ```
 {
    "success": False,
    "error": 404,
    "message": "resource not found"
}

```
The API will return three types of errors:

    400 – bad request
    404 – resource not found
    422 – unprocessable
    405 - method not allowed

### Endpoints

#### GET /categories
 - General: 
    - Returns a list categories.
    - Number of total categories.
    - The success status.
 - Sample: ``` curl http://127.0.0.1:5000/categories ```
 
```
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "success": true, 
  "total_Category": 6
}
```
#### GET /questions
 - General: 
    - Returns a list questions.
    - Apply pagination (every 10 questions in each page).
    - Number of total questions.
    - The success status.
 - Sample: ``` curl http://127.0.0.1:5000/questions ```
 
```
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "list_of_questions": [
    {
      "answer": "Maya Angelou", 
      "category": "4", 
      "difficulty": 2, 
      "id": 5, 
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    }, 
    {
      "answer": "Muhammad Ali", 
      "category": "4", 
      "difficulty": 1, 
      "id": 9, 
      "question": "What boxer's original name is Cassius Clay?"
    }, 
    {
      "answer": "Tom Cruise", 
      "category": "5", 
      "difficulty": 4, 
      "id": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }, 
    {
      "answer": "Edward Scissorhands", 
      "category": "5", 
      "difficulty": 3, 
      "id": 6, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }, 
    {
      "answer": "Brazil", 
      "category": "6", 
      "difficulty": 3, 
      "id": 10, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "answer": "Uruguay", 
      "category": "6", 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
    {
      "answer": "George Washington Carver", 
      "category": "4", 
      "difficulty": 2, 
      "id": 12, 
      "question": "Who invented Peanut Butter?"
    }, 
    {
      "answer": "Lake Victoria", 
      "category": "3", 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": "3", 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }, 
    {
      "answer": "Agra", 
      "category": "3", 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }
  ], 
  "number_of_total_questions": 18, 
  "success": true
}
```

#### DELETE /questions/<int:question_id>
 - General: 
    - Returns the id of deleted question.
    - Returns the success status.
 - Sample: ``` curl -X DELETE http://127.0.0.1:5000/questions/2 ```
 
 ```
 {
  "deleted": 4, 
  "success": true
}

 ```
 
 #### POST /questions
 - General: 
    - Returns the id of created question.
    - Returns a number of total questions.
    - Returns the success status.
    
 - Sample: ``` curl -X POST -H "Content-Type: application/json" -d '{"question":"What is the name of this Developer?","answer":"Sarah","category":"1","difficulty":4}' http://127.0.0.1:5000/questions```
 
 ```
{
  "created": 27, 
  "success": true, 
  "total_question": 18
}

 ```
 
  #### POST /questions/search
 - General: 
    - Returns a questions based on a search.
    - Returns the number of total questions that matched the search.
    
 - Sample: ``` curl -X POST -H "Content-Type: application/json" -d '{"search": "Oscar nomination"}' http://127.0.0.1:5000/questions/search```
 
 ```
{
  "questions": [
    {
      "answer": "Apollo 13", 
      "category": "5", 
      "difficulty": 4, 
      "id": 24, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }
  ], 
  "total_questions": 1
}


 ```
 
 #### GET /categories/<int:id>/questions
 
  - General: 
    - Returns a questions based on a specific category.
    - Returns the  success status.
    
 - Sample: ``` curl http://127.0.0.1:5000/categories/3/questions ```
 
 ```
{
  "questions": [
    {
      "answer": "Lake Victoria", 
      "category": "3", 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": "3", 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }, 
    {
      "answer": "Agra", 
      "category": "3", 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }
  ], 
  "success": true
}
```
 
#### POST /quizs
 
  - General: 
    - Returns a random questions within the given category, and that is not one of the previous questions.
    - Returns the success status.
    
 - Sample: ``` curl http://127.0.0.1:5000/quizs -X POST -H "Content-Type: application/json" -d '{"previous_questions": [3], "category": "3"}'  ```
 
 ```
 {
  "question": {
    "answer": "Agra", 
    "category": "3", 
    "difficulty": 2, 
    "id": 15, 
    "question": "The Taj Mahal is located in which Indian city?"
  }, 
  "success": true
}

 ```
 
# Trivia_API
