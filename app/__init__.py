from flask import Flask, request
from flask_restful import Api
from mongoengine import connect
from app.resources import CreatePerson, KeepAlive, FindMatch

connect('streetmeet')

main = Flask('StreetMeet')
api  = Api(main)

@main.route('/')
def home():
    return "Hello, world!"

api.add_resource(CreatePerson, '/person', '/person/')
api.add_resource(KeepAlive,'/person/<id>')
api.add_resource(FindMatch, '/match/<id>')