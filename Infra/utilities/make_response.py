from Infra.adapters.flask_adapter import FlaskMakeResponseAdapter
from flask import make_response, jsonify
import logging
from functools import wraps

def make_response(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        response: dict = func(*args, **kwargs)
        logging.info("\n" * 3)
        logging.info(response)
        logging.info("\n" * 3)
        adapter: FlaskMakeResponseAdapter = FlaskMakeResponseAdapter()
        return adapter.make_response(**response)
    return wrapper
