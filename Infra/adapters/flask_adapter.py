from flask import make_response, jsonify, json
import json

class FlaskMakeResponseAdapter:
    def make_response(self, status:int = 400, body:dict={}, *args, **kwargs):
        return make_response(json.dumps(body, default=vars), status)
