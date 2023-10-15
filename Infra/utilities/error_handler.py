from functools import wraps
import traceback
import logging

def error_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(traceback.format_exc())
            logging.error(str(e))
            return 500, 'Internal Error'
    return wrapper
