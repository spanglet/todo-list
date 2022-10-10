import os
import tempfile

import pytest
from todoism import create_app
from todoism.db_models import db


@pytest.fixture(scope="module")
def app():

    app = create_app(testing = True)
    
    yield app

    # Cleanup after testing

@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def app_ctx(app):
    with app.app_context():
        yield

class AuthActions(object):
    """Authorization blueprint testing """
    def __init__(self, client):
        self._client = client

    def login(self, username='test', password='test'):
        return self._client.post(
            '/auth/login',
            data={'username': username, 'password': password}
        )

    def logout(self):
        return self._client.get('/auth/logout')


@pytest.fixture
def auth(client):
    return AuthActions(client)
