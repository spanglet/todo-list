import pytest
from flask import g, session

from todoism.db_models import db


REG_URL = '/auth/register'
LOGIN_URL = '/auth/login'


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

    
@pytest.mark.parametrize(('username', 'password', 'message'), (
    ('abcd', 'abcdefgh', "Duplicate entry 'abcd' for key 'user.username'"),
    ('bobby', 'abcdefgh', "Duplicate entry 'bobby' for key 'user.username'"),
    ('jimbo', 'abcdefgh', "Duplicate entry 'jimbo' for key 'user.username'"),
))
def test_register_duplicate_validation(client, username, password, message):

    data = {
        'username': username,
        'password': password,
    }

    response = client.post(REG_URL, json = data)

    assert 'error' in response.json
    assert response.json['error']['message'] == message
