
from sqlalchemy.exc import IntegrityError

class APIError(Exception):
    """Thrown when a HTTP request is OK but the POST/PUT attempt fails"""
    message = 'An unspecified error in the backend API occured'
    title = "Error in submitting JSON payload."

    def __init__(self, message=None, status=200):
        super().__init__()
        if message:
            self.message = message
        self.status = status

class LoginError(APIError):
    message = 'Username or password is incorrect.' 
