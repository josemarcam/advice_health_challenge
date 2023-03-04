from werkzeug.exceptions import HTTPException
from datetime import datetime
from http import HTTPStatus

class Response:

    # Success responses
    OK = 200
    CREATED = 201

    # Error responses
    NOT_FOUND = 404
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    UNPROCESSABLE_ENTITY = 422

    # Server errors
    INTERNAL_SERVER_ERROR = 500
    

    @classmethod
    def force_type(cls,response=None,message=None, data = {}):
        return ({
            "data": data or None,
            "message":message,
            "timestamp": datetime.now().isoformat()
        }, response)