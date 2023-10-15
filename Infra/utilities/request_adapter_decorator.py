from Infra.adapters.flask_adapter import FlaskRequestAdapter
from flask import request
from functools import wraps

def request_adapter(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        kwargs['request'] = FlaskRequestAdapter(request=request)
        return func(*args, **kwargs)
    return wrapper
