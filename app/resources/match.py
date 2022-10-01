from app.models.person import PersonModel

class FindMatch(Resource):
	def get(self, id):
		d = PersonModel.objects(pk=id).first()
		matches = PersonModel.objects(point__geo_within_sphere=[d.location, 5/3963.2])
		return matches