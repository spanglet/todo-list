import pytest
from flask import g, session

from todoism.db_models import db


REG_URL = '/auth/register'
LOGIN_URL = '/auth/login'

def test_invalid_mimetype(auth, client):
    auth.login()
    response = client.post(REG_URL, data={
        "username": 'test',
        "password": 'test1234'
    })
    assert 'error' in response.json
    assert response.status_code == 400

@pytest.mark.usefixtures("app_ctx")
def test_register(client):
    assert client.get(REG_URL).status_code == 200
    response = client.post(
        REG_URL, json={'username': 'abcd', 'password': 'abcdefgh'}
    )

    assert 'error' not in response.json
    assert db.session.execute(
            "SELECT * FROM user WHERE username = 'abcd'",
        ).fetchone() is not None


@pytest.mark.parametrize(('username', 'password', 'messages'), (
    ('', '', ['username', 'password']),
    ('abcdefs', '', ['password']),
    ('', 'abcdefbd', ['username']),
))
def test_register_post_validation(client, username, password, messages):
    
    data = {
        'username': username,
        'password': password,
    }
    response = client.post(REG_URL, json = data)

    assert 'error' in response.json
    for message in messages:
        assert message in response.json['error']['message']


@pytest.mark.usefixtures("app_ctx")
@pytest.mark.parametrize(('username', 'password'), (
    ('bobby', 'abcdefgh'), ('jimbo', '1645js73jd'),
    ('awlohinfne', '834220?d;w1'), ('1534,6g5', '12dcg$@,l'),
))
def test_register_post_successful(client, username, password):

    data = {
        'username': username,
        'password': password,
    }
    response = client.post(REG_URL, json = data)

    assert response.status_code == 200
    assert 'error' not in response.json
    assert db.session.execute(
            "SELECT * FROM user WHERE username = '" + username + "'"
        ).fetchone() is not None

    
@pytest.mark.parametrize(('username', 'password'), (
    ('abcd', 'abcdefgh'), ('bobby', 'abcdefgh'),
    ('jimbo', 'abcdefgh'), ('abcd', '12345678'),
))
def test_register_duplicate_validation(client, username, password):

    data = {
        'username': username,
        'password': password,
    }

    response = client.post(REG_URL, json = data)

    assert 'error' in response.json
    assert response.json['error']['message'] == 'Username is already taken'


def test_login(client, auth):
    """Tests /auth/login endpoint for submitting login requests"""
    response = auth.register()
    assert 'error' not in response.json
    assert response.json['data']['ok'] is True

    assert client.get(LOGIN_URL).status_code == 200
    response = auth.login()
    assert 'error' not in response.json

    with client:
        response = client.get(LOGIN_URL)
        assert response.json['data']['sessionActive'] is True
        assert 'user_id' in session
        assert g.user.username == 'test'


@pytest.mark.parametrize(('username', 'password'), (
    ('abcdef', 'test1234'), ('test', 'abcdefgh'),
    (' test ', 'test1234'), ('test', ' test1234 '),
))
def test_login_validate_input(auth, username, password):
    """Tests incorrect login POST request responds with correct message"""
    response = auth.login(username, password)

    assert 'error' in response.json
    assert response.json['error']['message'] == 'Username or password is incorrect.'

def test_logout(client, auth):

    auth.login()

    with client:
        auth.logout()
        assert 'user_id' not in session


   
