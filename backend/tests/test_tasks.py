import pytest
from datetime import datetime

from flask import g, session

from todoism.db_models import db


def test_tasks(client, auth, app):
    response = client.get('/tasks/')

    assert 'error' in response.json
    assert response.json['error']['message'] == "Login is required"
    
    auth.register()
    auth.login()
    response = client.get('/tasks/')
    assert response.status_code == 200
    assert len(response.json['data']) == 0

    response = client.post(
        '/tasks/', json={
            'name': 'Test task',
            'description': 'This is a task',
            'dueDate': str(datetime(2030, 2, 2)),
            'listID': 1,
        })

    assert 'error' not in response.json
    assert response.json['data']['ok']

    with app.app_context():
        assert db.session.execute(
                "SELECT * FROM task WHERE name = 'Test task'"
            ).fetchone() is not None


def test_get_task(client, auth):

    response = client.get('/tasks/1')
    assert 'error' in response.json

    auth.login()

    response = client.get('/tasks/1')
    assert 'error' not in response.json
    assert response.json['data']['name'] == 'Test task'

def test_update_task(client, auth, app):
    auth.login()

    response = client.put('/tasks/1', json={'name': "Updated task"})
    assert 'error' not in response.json
    assert response.json['data']['ok'] is True

    assert 'error' not in client.get('/tasks/1').json

    with app.app_context():
        assert db.session.execute(
                "SELECT * FROM task WHERE name = 'Test task'"
            ).fetchone() is None

        assert db.session.execute(
                "SELECT * FROM task WHERE name = 'Updated task'"
            ).fetchone() is not None

    
def test_del_task(client, auth):

    auth.login()
    data = client.get('/tasks/').json['data']
    
    assert len(data)
    
    response = client.delete('/tasks/' + str(data[0]['id']))

    assert response.json['data']['ok'] is True
    assert response.json['data']['id'] == data[0]['id']


