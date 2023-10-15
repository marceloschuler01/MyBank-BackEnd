from flask_restful import reqparse

class ReqParserAdapter:
    @staticmethod
    def RequestParser():
        return reqparse.RequestParser()
