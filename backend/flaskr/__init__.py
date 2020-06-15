import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
import json
from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10



def paginate(request, questions):
    page = request.args.get('page', 1, type=int)
    start =  (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
# questions
    questionss = [i.format() for i in questions]
    current_questions = questionss[start:end]

    return current_questions

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  
  '''
  @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''
  CORS(app, resources={r"/api/*": {"origins": "*"}})

  '''
  @TODO: Use the after_request decorator to set Access-Control-Allow
  '''
  # CORS Headers 
  @app.after_request
  def after_request(response):
      response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
      response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
      return response

  @app.route('/')
  def test():
    return jsonify({'message':'works'})

  '''
  @TODO: 
  Create an endpoint to handle GET requests 
  for all available categories.
  '''
  @app.route('/categories')
  def retrieve_category():

        categories = Category.query.all()
      
        categories_dict = {}
        for category in categories:
                categories_dict[category.id] = category.type
   
        
        # if len(Category.query.all()) == 0:
        #     abort(404)

    
        return jsonify({
            'success': True,
            'categories' : categories_dict,
            'total_Category': len(Category.query.all())
        })

  '''
  @TODO: 
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''
 
  @app.route('/questions')
  def retrieve_questions():

        questions = Question.query.all()
        current_questions = paginate(request, questions)
        
        categories = Category.query.all()
      
        categories_dict = {}
        for category in categories:
                categories_dict[category.id] = category.type       

        if len(current_questions) == 0:
           abort(404)

        return jsonify({
            'success': True,
            'list_of_questions': current_questions,
            'number_of_total_questions': len(Question.query.all()),
            'categories':categories_dict
      
        })

  '''
  @TODO: 
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''

  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_questions(question_id):

            question = Question.query.get(question_id)

            if question is None:
                abort(422)

            question.delete()

            return jsonify({
                'success': True,
                'deleted': question_id,
            })



  '''
  2	


  @TODO: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''

  @app.route('/questions', methods=['POST'])
  def create_question():


        question = request.json.get('question')
        answer = request.json.get('answer')
        category = request.json.get('category')
        difficulty = request.json.get('difficulty')

        try:
            question = Question(question, answer, category, difficulty)
            question.insert()


            return jsonify({
                'success': True,
                'created': question.id,
                'total_question': len(Question.query.all())
            })

        except:
            abort(422)


  '''
  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''
  @app.route('/questions/search', methods=['POST'])
  def search():

    search = request.json['search']

    questions =  Question.query.order_by(Question.id).filter(Question.question.ilike('%{}%'.format(search)))
    current_questions = paginate(request, questions)

    if not current_questions: 
        abort(404)
      
    else:
      return jsonify({
           "questions": current_questions,
            'total_questions': len(questions.all())
      })








  '''
  @TODO: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 


 

  '''

  @app.route('/categories/<int:id>/questions')
  def get_questions_category(id):
    
            x= str(id)
            selections = Question.query.filter(Question.category == x).all()
            questions  =  [i.format() for i in selections]

            if not questions:
              abort(404)

            else:
              return jsonify({
                    'success': True,
                    'questions': questions,
                })
       

           


  '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  # '''
  @app.route('/quizs', methods=['POST'])
  def get_quiz_question():

        previous_questions = request.json.get('previous_questions')
        category = request.json.get('category')

        try:
            
            selections = Question.query.filter_by(category=category).all()

            questions  =  [i.format() for i in selections]

            result = random.choice(questions )

            return jsonify({
                'success': True,
                'question': result
            })
        
        except:
            abort(400)


  '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''

  @app.errorhandler(404)
  def not_found(error):
        return jsonify({
            "success": False, 
            "error": 404,
            "message": "resource not found"
        }), 404

  @app.errorhandler(422)
  def unprocessable(error):
        return jsonify({
            "success": False, 
            "error": 422,
            "message": "unprocessable"
        }), 422

  @app.errorhandler(405)
  def methodNotAllowed(error):
        return jsonify({
            "success": False, 
            "error": 405,
            "message": "method not allowed"
        }), 405

  @app.errorhandler(400)
  def bad_request(error):
        return jsonify({
            "success": False, 
            "error": 400,
            "message": "bad request"
        }), 400

  @app.errorhandler(500)
  def internal_Server_Error(error):
        return jsonify({
            "success": False, 
            "error": 500,
            "message": "Internal Server Error"
        }), 500       
  return app

    