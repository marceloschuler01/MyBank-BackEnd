from functools import wraps
import logging
from core.exceptions.not_found_data_exception import NotFoundedDataException

def verify_if_it_was_found_data(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result:
            return result
        logging.error(str(args)+str(kwargs))
        raise NotFoundedDataException
    return wrapper
