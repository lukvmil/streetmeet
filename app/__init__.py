from flask import Flask, request
from flask_restful import Api

from app.resources import CreatePerson

main = Flask('StreetMeet')
api  = Api(main)

@main.route('/')
def home():
    return "Hello, world!"

api.add_resource(CreatePerson, '/person')