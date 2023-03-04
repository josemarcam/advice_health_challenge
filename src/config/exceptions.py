from flask import Flask

from src.shared.http import Response
from src.shared.exceptions import (
    NotFoundException,
    ForbiddenException,
    UnauthorizedException,
)


def init_app(app: Flask):


    @app.errorhandler(NotFoundException)
    def not_found_error(error: NotFoundException):
        return Response().force_type(
            response=error.status_code, 
            data=error.to_dict(),
            message=error.message
        )

    @app.errorhandler(ForbiddenException)
    def forbidden_error(error: ForbiddenException):
        return Response().force_type(
            response=error.status_code,
            data=error.to_dict(),
            message=error.message
        )
    
    @app.errorhandler(UnauthorizedException)
    def unauthorized_error(error: UnauthorizedException):
        return Response().force_type(
            response=error.status_code,
            data=error.to_dict(),
            message=error.message
        ) 