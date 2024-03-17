from functools import wraps
from Infra.exceptions.bad_request import BadRequest
import traceback
import logging
import werkzeug

def error_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except BadRequest as e:
            info = {'message': e.message, 'value': e.value, 'info': e.info}
            return info, e.status
        except werkzeug.exceptions.UnsupportedMediaType:
            return "Content-Type must be application/json", 415
        except werkzeug.exceptions.BadRequest as e:
            raise e
        except Exception as e:
            logging.error(traceback.format_exc())
            logging.error(str(e))
            return 'Internal Error', 500
    return wrapper
