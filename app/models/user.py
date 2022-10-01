from mongoengine import Document
from mongoengine.fields import *

class UserModel(Document):
    id = StringField(primary_key=True)
    username = StringField()
    location = GeoPointField()
    topic = StringField()
    timeout = DateTimeField()
    peer_id = StringField()