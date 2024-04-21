from flask import Flask, jsonify, request
from flask_restful import Resource, Api, fields, marshal_with, reqparse, abort
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import os

# Aspects of this were adapted from following page:
# https://github.com/TrevorChan1/EC530-flaskrestful-demo/blob/main/3.%20demo_with_database/app.py

# Define flask app and flask_restful API objects
app = Flask(__name__)
api = Api(app)

# Create database.db table if it doesn't already exist. Source: https://docs.python.org/3/library/sqlite3.html
user_table_connect = sqlite3.connect("users.db")

user_cur = user_table_connect.cursor()

user_cur.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    ssn INT NOT NULL, 
    email TEXT NOT NULL,                         
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    role INT NOT NULL)''')

user_table_connect.commit()

user_table_connect.close()

# Configures the userManagement API to connect to the database 'database.db' SQLite file (since SQLite db is locally stored)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'users.db')
db = SQLAlchemy(app)


# Defines the SQLite table schema with the same name as a db.Model object
class users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(32), nullable = False)
    last_name = db.Column(db.String(32), nullable = False)
    ssn = db.Column(db.Integer, nullable = False)
    email = db.Column(db.String(200), nullable = False)
    username = db.Column(db.String(200), nullable = False)
    password = db.Column(db.String(200), nullable = False)
    role = db.Column(db.Integer, nullable = False)
    

    def __init__(self, id, first_name, last_name, ssn, email, username, password, role):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.ssn = ssn
        self.email = email
        self.username = username
        self.password = password
        self.role = role
        

    # Shows what values are returned when this object is queried
    def __repr__(self):
        return self.username


# Defines the output data schema
user_definition = {
    'user_id' : fields.Integer,
    'first_name' : fields.String,
    'last_name' : fields.String,
    'ssn' : fields.Integer,
    'email' : fields.String,
    'username' : fields.String,
    'password' : fields.String,
    'role' : fields.Integer
}

class FormatUser(object):
    def __init__(self, uid, first_name, last_name, ssn, email, username, password, role):
        self.user_id = uid
        self.first_name = first_name
        self.last_name = last_name
        self.ssn = ssn
        self.email = email
        self.username = username
        self.password = password
        self.role = role
        


# Define request parser
parser = reqparse.RequestParser()
parser.add_argument('first_name', required=True, help="First Name cannot be blank")
parser.add_argument('last_name', required=True, help="Last Name cannot be blank")
parser.add_argument('ssn', required=True, help="ssn cannot be blank")
parser.add_argument('email', required=True, help="ssn cannot be blank")
parser.add_argument('username', required=True, help="username cannot be blank")
parser.add_argument('password', required=True, help="username cannot be blank")
parser.add_argument('role', required=True, help="username cannot be blank")


def get_user(user_id):
    # If find user, return
    user = users.query.filter_by(id=user_id).first()

    try:
        if (user):
            return FormatUser(user.id, user.first_name, user.last_name, user.ssn, user.email, user.username, user.password, user.role)
        # Otherwise, send error message and error code
        else:
            return {'error' : 'no such user found'}, 404
    except Exception as e:
        print(e)

# Define a Resource-type class object to define functions for the RESTful API
class UserAPI(Resource):

    # GET function
    @marshal_with(user_definition)
    def get(self, user_id):
        check = users.query.filter_by(id=user_id).first()
        if not check:
            abort(404, message="User ID doesn't exist")
        return get_user(user_id)
    
    # PUT / POST function
    @marshal_with(user_definition)
    def post(self, user_id):

        # Parse request for desired values name and secret

        args = parser.parse_args()
        check = users.query.filter_by(id=user_id).first()
        if check:
            abort(409, message="User ID taken")
            
        else:
        # Start SQLite db session to insert and commit
            new_user = users(user_id, args['first_name'], args['last_name'], args['ssn'], 
                             args['email'], args['username'], args['password'], args['role'])
            db.session.add(new_user)
            db.session.commit()

        return FormatUser(user_id, args['first_name'], args['last_name'], args['ssn'], 
                             args['email'], args['username'], args['password'], args['role'])

        
    # DELETE function for deleting resources from the API
    def delete(self, user_id):

        # NEW: Use db session to find and delete user
    
        user = users.query.filter_by(id=user_id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
        else:
            return {'error' : 'no such user found'}, 404
    

# Use the API object to connect the Resource objects to paths on the Flask server
    
# /<datatype: input_name> = a way to have variable paths
api.add_resource(UserAPI, '/user/<int:user_id>')

# api.add_resource(UserAPI, '/user/<int:user_id>', '/user_role/<int:user_id>/<int:entry_id>')

if __name__ == '__main__':
    app.run(port=8000, debug=True)


