from flask import Flask, jsonify, request
from flask_restful import Resource, Api, fields, marshal_with, reqparse
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import sqlite3
import os


# Aspects of this were adapted from following page:
# https://github.com/TrevorChan1/EC530-flaskrestful-demo/blob/main/3.%20demo_with_database/app.py

# Define flask app and flask_restful API objects
app = Flask(__name__)
api = Api(app)

# Create user.db table if it doesn't already exist. Source: https://docs.python.org/3/library/sqlite3.html
user_table_connect = sqlite3.connect("users.db")

user_cur = user_table_connect.cursor()

user_cur.execute('''
CREATE TABLE IF NOT EXISTS users (
  id integer PRIMARY KEY,
  first_name varchar(255),
  last_name varchar(255),
  ssn varchar(255),
  username varchar(255),
  password varchar(255),
  email varchar(255),
  time_added timestamp
)''')

user_table_connect.commit()

user_table_connect.close()

# Configure the app to connect to the database 'users.db' SQLite file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'users.db')
db = SQLAlchemy(app)

# Define the SQLite table schema (with the same name) as a db.Model object
class users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(200), nullable = False)
    last_name = db.Column(db.String(200), nullable = False)
    ssn = db.Column(db.String(255), unique = True, nullable = False)
    username = db.Column(db.String(255), nullable = False)
    password = db.Column(db.String(255), nullable = False)
    email = db.Column(db.String(255), unique = True, nullable = False)
    time_added = db.Column(db.DateTime(timezone=True), server_default= func.now())

    def __init__(self, id, first_name, last_name, ssn, username, password, email, time_added):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.ssn = ssn
        self.username = username
        self.password = password
        self.email = email
        self.time_added = time_added

    # Shows what values are returned when this object is queried
    def __repr__(self):
        return self.name

# Define output data schema
user_definition = {
    'user_id' : fields.Integer,
    'first_name' : fields.String,
    'last_name' : fields.String,
    'email' : fields.String
}

class FormatUser(object):
    def __init__(self, id, first_name, last_name, email):
        self.user_id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email


# Define request parser
parser = reqparse.RequestParser()
parser.add_argument('first_name', help="First Name cannot be blank")
parser.add_argument('last_name', help="Last Name cannot be blank")

# get_user uses SQLAlchemy rather than the users dict
def get_user(user_id):
    # If find user, return
    user = users.query.filter_by(id=user_id).first()

    try:
        if (user):
            return FormatUser(user.id, user.first_name, user.last_name, user.email)
        # Otherwise, send error message and error code
        else:
            return {'error' : 'User not found'}, 404
    except Exception as e:
        print(e)

# Define a Resource-type class object to define functions for the RESTful API
class UserAPI(Resource):

    # GET function
    # marshal_with will serialize the API response to follow schema
    @marshal_with(user_definition)
    def get(self, user_id):
        return get_user(user_id)
    
    # PUT / POST function
    @marshal_with(user_definition)
    def post(self, user_id):

        # Parse request for desired values name and secret
        try:
            args = parser.parse_args()

            # NEW: Start SQLite db session, insert and commit
            new_user = users(user_id, args['first_name'], args['last_name'], args['ssn'], 
                             args['username'], args['password'], args['email'], args['time_added'])
            db.session.add(new_user)
            db.session.commit()

            return FormatUser(user_id, args['first_name'], args['last_name'], args['email'])
        except Exception as e:
            print(e)
            return e

    # DELETE function for deleting resources from the API
    def delete(self, user_id):

        # NEW: Use db session to find and delete user
        try:
            user = users.query.filter_by(id=user_id).first()
            if (user):
                db.session.delete(user)
                db.session.commit()
            else:
                return {'error' : 'User not found'}, 404
        except Exception as e:
            return e
    

# Use the API object to connect the Resource objects to paths on the Flask server
# Once running the app, can test that it's working: curl http://127.0.0.1:5000
# Example PUT curl http://localhost:5000/todo1 -d "data=Remember the milk" -X PUT
    
# /<datatype: input_name> = a way to have variable paths
api.add_resource(UserAPI, '/user/<int:user_id>')

if __name__ == '__main__':
    app.run(port=8000, debug=True)