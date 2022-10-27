import pytest

from todoism.db_models import db

def test_login_required(client):

    response = client.get('/lists/')
    assert response.json['error']['message'] == "Login is required"

    response = client.get('/lists/0')
    assert response.json['error']['message'] == "Login is required"

def test_lists(client, auth, app):
    
    auth.register()
    auth.login()

    response = client.get('/lists/')
    assert response.status_code == 201
    assert len(response.json['data']) == 1
    assert response.json['data'][0]['name'] == 'Today'

    response = client.post(
        '/lists/', json={
            'name': 'Website Tasks',
            'description': 'Next tasks for website project',
        })

    assert 'error' not in response.json
    assert response.json['data']['ok']

    with app.app_context():
        assert db.session.execute(
                "SELECT * FROM list WHERE name = 'Website Tasks'"
            ).fetchone() is not None

@pytest.fixture
def new_list(auth, client):

    auth.login()

    response = client.post('/lists/', json = {
        'name': 'New List',
        'description': 'Make a new list with API'
    })

    return response.json['data']

@pytest.mark.parametrize(('name', 'description'), (
    ('Work', 'Work-related goals and tasks.'),
    ('School Activities', 'School assignments/homework'),
    ('Personal Goals (Current)', 'Self-Improvement goals outside work'),
))
def test_add_lists(client, auth, name, description):

    auth.login()
    
    response =  client.post('/lists/', json={
            'name': name,
            'description': description,
        })
    assert 'error' not in response.json
    assert response.json['data']['ok'] == True


def test_get_list(client, new_list):

    response = client.get('/lists/' + str(new_list['id']))

    assert 'error' not in response.json
    assert response.json['data']['name'] == 'New List'

def test_list_unauthorized(client, auth, new_list):
    
    auth.register('badtest', 'badtest123')
    auth.login('badtest', 'badtest123')

    response = client.get('/lists/' + str(new_list['id']))
    
    assert 'error' in response.json
    assert response.status_code == 403

def test_update_list(client, new_list, app):

    id = str(new_list['id'])
    new_name = 'Even Newer List'

    response = client.put('/lists/' + id, json={
        'name': new_name
        })
    assert 'error' not in response.json

    response = client.get('/lists/' + id)
    assert response.json['data']['name'] == new_name


def test_delete_list(client, new_list, app):

    id = str(new_list['id'])

    response = client.delete('/lists/' + id)
    assert 'error' not in response.json
    assert response.status_code == 200

    response = client.get('/lists/' + id)
    assert response.status_code == 404
    
    with app.app_context():
        assert db.session.execute(
                "SELECT * FROM list WHERE id = '" + id + "'"
            ).fetchone() is None
