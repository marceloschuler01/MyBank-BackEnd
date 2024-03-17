class BadRequest(Exception):
    def __init__(self, status=400, message='', value=None, **kwargs):
        self.status = status
        self.message = message
        self.value = value
        self.info = kwargs
