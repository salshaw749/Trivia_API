import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}/{}".format('postgres:123456@localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.new_question = {
            'question': 'ARE YOU OKAY?',
            'answer': 'I THINK',
            'category': 1,
            'difficulty': 5 
        }

    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_get_available_categories(self):
        # Getting the response by making the client make a request
        res=self.client().get('/categories')
        data = json.loads(res.data)

        # to check the status code
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['categories'])
        self.assertTrue(len(data['categories']))

    def test_get_paginated_questions(self):
        res = self.client().get('/questions?page=1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)

        self.assertTrue(data['list_of_questions'])
        self.assertTrue(data['number_of_total_questions'])
        self.assertTrue(data['categories'])

    def test_404_get_paginated_questions(self):
        res = self.client().get('/questions?page=1000')
        data=json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['message'],'resource not found')

    def test_delete_questions(self):
        res=self.client().delete('/questions/12')
        data=json.loads(res.data)

        q = Question.query.filter(Question.id == 12).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)
        self.assertEqual(data['deleted'], 12)
        
    def test_422_if_dosent_exist(self):
        res = self.client().delete('/questions/1000')
        data=json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['message'],'unprocessable')

    def test_creating_questions(self):
        res=self.client().post('/questions', json=self.new_question)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['created'])
        self.assertTrue(data['total_question'])
    
    def test_405_if_questions_creation_not_allowed(self):
        res=self.client().post('/questions/45', json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['message'],'method not allowed')

    def test_serching_questions(self):
        res = self.client().post('/questions/search', json={'search': "YOU"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['questions'])
        self.assertTrue(data['total_questions'])

    def test_404_serching_questions_if_not_include(self):
        res = self.client().post('/questions/search', json={'search': "dd"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['message'],'resource not found')

    def test_get_questions_bycategory(self):
        res = self.client().get('/categories/3/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['questions'])

    def test_404_get_questions_wrong_bycategory(self):

        res = self.client().get('/categories/1000/questions')
        data=json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['message'],'resource not found')
    
    def test_quiz(self):
        res = self.client().post('/quizs', json={'previous_questions': [3],"category": '3'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['question'])

    def test_400_wrong_quiz_input(self):
        res = self.client().post('/quizs', json={'previous_questions': [3],"category": "a"})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['message'],'bad request')  









        





# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()