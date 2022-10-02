from flask_restful import Resource
from app.models import UserModel
from datetime import datetime

class FindMatch(Resource):
	def get(self, id):
		if not UserModel.objects.count(): return []
		d = UserModel.objects(pk=id).first()
		if not d: abort(400, message="user not found")
		matches = UserModel.objects(location__within_spherical_distance=[d.location, 5/3963.2])
		valid_matches = []
		for m in matches:
			if datetime.now() > m.timeout:
				m.delete()
			else:
				if m.id == id: continue
				valid_matches.append({
					'id': m.id,
					'username': m.username,
					'topic': m.topic,
					'peerId': m.peer_id
				})

		return valid_matches
