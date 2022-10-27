import json
from flask import g

def register_request_handlers(app):
    """Hooks before/after request handlers to app instance """

    @app.after_request
    def wrap_response_body(response):
        """Wraps JSON payload for all non-error responses
        for API standardization.
        """

        data = response.get_json()

        if data and "error" in data:
            # Skip response modification if received from errorhandler
            return response

        response.data = json.dumps({"data": data})
        return response
    
