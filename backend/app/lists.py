import json
from flask import Flask, render_template, session
from flask import request, Blueprint, jsonify, make_response
from marshmallow import Schema, fields
from marshmallow.exceptions import ValidationError

from .db_models import db, List, Task
from .schema import TaskSchema, ListSchema
from .auth import login_required

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
        ListSchema().load(data)
       
        # Insert response data into MySQL DB
        new_list = List(
            name = data["name"],
            userID = session['user_id']
        )
        db.session.add(new_list)
        db.session.commit()
       
        return "list successfully added",200
 
    if request.method == 'GET':
        
        lists = List.query.filter(List.userID == session["user_id"],
                    List.id > -1).all()

        return ListSchema().dumps(lists, many=True), 200
 
@bp.route('/<list_id>', methods=['PUT','DELETE','GET'])
def update_list(list_id):
    """Delete or modify existing list owned by requester"""
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
 
    if request.method == 'DELETE':
        
        del_list = List.query.get(list_id)
        db.session.delete(del_list)
        db.session.commit()
        return "List successfully removed", 200

    if request.method == 'GET':

        tasks = Task.query.filter_by(listID = list_id).all()
        return TaskSchema().dumps(tasks, many=True), 200

