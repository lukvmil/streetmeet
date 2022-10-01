from flask_restful import Resource
from app.models import UserModel
from datetime import datetime

class FindMatch(Resource):
	def get(self, id):
		if not UserModel.objects.count(): return []
		d = UserModel.objects(pk=id).first()
		matches = UserModel.objects(location__within_spherical_distance=[d.location, 5/3963.2])
		valid_matches = []
		for m in matches:
			if datetime.now() > m.timeout:
				m.delete()
			else:
				valid_matches.append({
					'id': m.id,
					'username': m.username,
					'topic': m.topic
				})

		return valid_matches
