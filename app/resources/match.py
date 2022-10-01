from flask_restful import Resource
from app.models.person import PersonModel

class FindMatch(Resource):
	def get(self, id):
		d = PersonModel.objects(pk=id).first()
		print(d.location)
		matches = PersonModel.objects(location__within_spherical_distance=[d.location, 5/3963.2])
		return [{
			'first_name': m['first_name'],
			'topic': m['topic']
		} for m in matches]
