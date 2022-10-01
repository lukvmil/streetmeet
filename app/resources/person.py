from flask import request
from flask_restful import Resource, abort
from app.models import PersonModel
from app import shared

class CreatePerson(Resource):
    def post(self):
        data = request.get_json()
        p = PersonModel(**data)
        p.save()
        
# class KeepAlive(Resource):
#     def post(self):
        
