from mongoengine import Document
from mongoengine.fields import *

class PersonModel(Document):
    account = StringField(primary_key=True)
    first_name = StringField()
    location = PointField()
    topic = StringField()
    timeout = DateTimeField()