from flask_restful import Resource
from app.models import UserModel

class FindMatch(Resource):
	def get(self, id):
		d = UserModel.objects(pk=id).first()
		matches = UserModel.objects(location__within_spherical_distance=[d.location, 5/3963.2])
		return [{
			'id': m['id'],
			'username': m['username'],
			'topic': m['topic']
		} for m in matches]
