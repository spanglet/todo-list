import json

from flask import (
    Flask, Blueprint, request, abort,
    jsonify, make_response, g
)

from todoism.db_models import db, List, Task
from todoism.schema import TaskSchema, ListSchema
from todoism.auth import login_required

bp = Blueprint('lists', __name__, url_prefix='/lists')

list_schema = ListSchema()

@bp.route('/', methods=['POST','GET'])
@login_required
def lists():
    """Create new list or get all lists for logged-in user"""
    if request.method == 'POST':
 
        data = request.get_json()

        data['userID'] = g.user.id
        new_list = list_schema.load(data)
       
        db.session.add(new_list)
        db.session.commit()
       
        return {"ok": True, "id": new_list.id}, 201
 
    else:
        
        query = db.select(List).filter_by(userID = g.user.id)
        lists = db.session.execute(query).scalars().all()

        return list_schema.dump(lists, many=True), 201
 
@bp.route('/<int:list_id>', methods=['PUT','DELETE','GET'])
@login_required
def update_list(list_id):
    """Delete or modify existing list owned by requester"""
    list_ = db.get_or_404(List, list_id)

    if list_.userID != g.user.id:
        abort(403)

    if request.method == 'PUT':

        data = request.get_json()

        for key,val in data.items():
            setattr(list_,key,val)

        db.session.commit()

        return {"ok": True, 'message': 'List was successfully updated'}, 200
 
    elif request.method == 'DELETE':
        
        db.session.delete(list_)
        db.session.commit()

        return {'ok': True}, 200

    else:
        #TODO change response to list, with tasks of list (MARSHMALLOW)

        query = db.select(Task).filter_by(listID = list_id)

        return list_schema.dump(list_), 200


