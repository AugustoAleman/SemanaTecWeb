from multiprocessing.sharedctypes import SynchronizedString
from os import name
from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from models.assignment import AssignmentSchema,Assignment
from models.user import User,UserSchema
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from logging import exception
from flask_jwt import JWT, jwt_required, current_identity


app = Flask(__name__)
bcrypt = Bcrypt(app)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bswpvfruqeweer:0557a2689bbf4bc9fc1436d7b8b621e464f5b63f2868ca9b8659ddd58ed4527b@ec2-44-209-158-64.compute-1.amazonaws.com:5432/d35om21l185i8s'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'super-secret'

def authenticate(username, password):
    user = User.query.filter(User.email==username).first()
    if user and bcrypt.check_password_hash(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return User.query.filter(User.id==user_id).first()

jwt = JWT(app, authenticate, identity)


@app.route('/')
def hello_world():
    return "My API is running"

@app.route('/user/list')
def first_api(name):
    users=User.get(name)
    users_schema = UserSchema
    return users_schema.dumps(users)

@app.route('/user/assignments/<id>')
def get_user_assignments(id):
    user=User.query.filter(User.id==id).first()
    assignments=Assignment.query.filter(Assignment.users.contains(user)).all()
    assignment_schema=AssignmentSchema(many=True)
    return assignment_schema.dumps(assignments)

@app.route('/user/create',methods=['POST'])
def creat_usuario():
    body=request.get_json()
    print(body)
    body["password"]=bcrypt.generate_password_hash(body["password"])
    user_schema=UserSchema()
    user=user_schema.load(body,session=db.session)
    user.save()
    
    return user_schema.dump(user)


@app.route('/assignment/create',methods=['POST'])
def create_assignment():
    body=request.get_json()
    assignment_schema=AssignmentSchema()
    assignment=assignment_schema.load(body,session=db.session)
    assignment.save()
    return assignment_schema.dump(assignment)    

@app.route('/assignment/assign',methods=['POST'])
def assign():
    body=request.get_json()
    assignment_schema=AssignmentSchema()
    assignment=assignment_schema.load(body,session=db.session)
    assignment.save()
    return assignment_schema.dump(assignment) 

@app.route('/api/user/search', methods=['GET'])
def getUserBySearch():
        body=request.get_data()
        fields = {}
        users = {}
        if "name" in request.args:
            fields["name"] = request.args["name"]
        if "email" in request.args:
            fields["email"] = request.args["email"]
        if "id" in request.args:
            fields["id"] = request.args["id"]
        
        users = User.query.filter_by(**fields).first()
        search=users(body,session=db.session)
        search.save()
        return users.dump(search) 
 



