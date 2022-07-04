import json
from flask import Flask, render_template, session
from flask import request, Blueprint, jsonify, make_response
from marshmallow import Schema, fields
from marshmallow.exceptions import ValidationError

from .db_models import db, List, Task
from .schema import TaskSchema
from .auth import login_required

# Schema for JSON post/put data validation
class ListSchema(Schema):
    name = fields.Str(required=True)
    description = fields.Str()
    id = fields.Integer()

app = Flask(__name__)

bp = Blueprint('lists', __name__, url_prefix='/lists')

# Creates a new task list
@login_required
@bp.route('/', methods=['POST','GET'])
def new_list():

    if request.method == 'POST':
 
        # Data must be of type json
        data = request.get_json()
        if not data:
            return "Data must be of type json",400
  
        # Use schema to check for incorrect request entries
        try:
            ListSchema().load(data)
       
        except ValidationError:
            return "json contained incorrect keys",400
       
        # Insert response data into MySQL DB
       
        new_list = List(
            name = data["name"],
            #description = data["description"],
            userID = session['user_id']
        )
        db.session.add(new_list)
        db.session.commit()
       
        return "list successfully added",200
 
    if request.method == 'GET':
        
        lists = List.query.filter(List.userID == session["user_id"], List.id > -1).all()

        return ListSchema().dumps(lists, many=True), 200
 

# Delete or modify individual list        
@bp.route('/<list_id>', methods=['PUT','DELETE','GET'])
def update_list(list_id):

 
    # Update list with data of request if PUT request
    if request.method == 'PUT':

        data = request.get_json()

        _list = List.query.filter_by(
                id = list_id,
                userID = session["user_id"]).first()
       
        # Update Task object that was retrieved
        for key,val in data.items():
            setattr(_list,key,val)

        db.session.commit()
        return "List was successfully updated",200
 
    # Remove list if DEL request received
    if request.method == 'DELETE':
        
        del_list = List.query.get(list_id)
        db.session.delete(del_list)
        db.session.commit()
        return "List successfully removed", 200

    if request.method == 'GET':

        tasks = Task.query.filter_by(listID = list_id).all()
        return TaskSchema().dumps(tasks, many=True), 200

