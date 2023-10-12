from functools import wraps
from flask import session

def client_login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'id' in session:
            return func(*args, **kwargs)
        return 'unauthorized', 401
    return wrapper
