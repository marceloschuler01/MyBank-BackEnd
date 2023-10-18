from functools import wraps
import traceback
import logging
import werkzeug

def error_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except werkzeug.exceptions.UnsupportedMediaType:
            return "Content-Type must be application/json", 415
        except werkzeug.exceptions.BadRequest as e:
            raise e
        except Exception as e:
            logging.error(traceback.format_exc())
            logging.error(str(e))
            return 'Internal Error', 500
    return wrapper
