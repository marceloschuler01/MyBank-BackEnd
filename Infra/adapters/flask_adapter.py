from flask import make_response, jsonify, json
from .http_context import HttpContext
import json

class FlaskRequestAdapter(HttpContext):
    def __init__(self, request):
        self.__request = request
        self.response = None

    def get_request(self):
        return {"header": self.__request.headers, "body": self.__request.json, "content_type": self.__request.content_type}
    
    def make_response(self, status:int=200, body:dict={}):
        self.response = make_response(json.dumps(body, default=vars), status)
        return self.response