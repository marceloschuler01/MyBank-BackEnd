from Infra.adapters.flask_adapter import FlaskMakeResponseAdapter
import logging
from functools import wraps

def make_response(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        response: dict = func(*args, **kwargs)
        logging.info("\n Making Response...")
        logging.info(response)
        logging.info("\n")
        adapter: FlaskMakeResponseAdapter = FlaskMakeResponseAdapter()
        return adapter.make_response(**response)
    return wrapper
