from flask import request
from flask_restful import Resource, abort
from app.models import PersonModel
from app import shared
from datetime import * 

class CreatePerson(Resource):
    def post(self):
        data = request.get_json()
        p = PersonModel(**data)
        p.save()
        
class KeepAlive(Resource):
     def post(self, id):
        d = PersonModel.objects(pk=id).first()
        d.timeout=datetime.now()+ datetime.timedelta(minutes=1)
        d.save()

    


