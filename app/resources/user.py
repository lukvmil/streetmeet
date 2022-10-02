from flask import request
from flask_restful import Resource, abort
from datetime import datetime, timedelta
from app.models import UserModel
from uuid import uuid4
import json

class CreateUser(Resource):
    def post(self):
        data = request.get_json()
        peer_id = data['peerId']
        del data['peerId']
        data['peer_id'] = peer_id
        p = UserModel(**data)
        p.id = str(uuid4())
        p.timeout = datetime.now() + timedelta(seconds=15)
        p.save()

        return json.loads(p.to_json())
        
class KeepAlive(Resource):
    def post(self, id):
        d = UserModel.objects(pk=id).first()
        if not d: abort(400, message="user not found")
        d.timeout=datetime.now() + timedelta(seconds=15)
        d.save()

        return {'expiration': str(d.timeout)}

    


