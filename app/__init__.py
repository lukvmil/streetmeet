from flask import Flask, request
from flask_restful import Api
from mongoengine import connect
from app.resources import CreatePerson
from app.resources.person import KeepAlive

connect('streetmeet')

main = Flask('StreetMeet')
api  = Api(main)

@main.route('/')
def home():
    return "Hello, world!"

api.add_resource(CreatePerson, '/person')
api.add_resource(KeepAlive,'/person/<id>' )