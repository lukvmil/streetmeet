from flask import request
from flask_restful import Resource, abort
from datetime import datetime, timedelta
from app.models import UserModel
from uuid import uuid4

class CreateUser(Resource):
    def post(self):
        data = request.get_json()
        p = UserModel(**data)
        p.id = str(uuid4())
        p.timeout = datetime.now() + timedelta(minutes=1)
        p.save()

        return {'id': p.id, 'expiration': str(d.timeout)}
        
class KeepAlive(Resource):
    def post(self, id):
        d = UserModel.objects(pk=id).first()
        d.timeout=datetime.now()+ timedelta(minutes=1)
        d.save()

        return {'expiration': str(d.timeout)}

    


