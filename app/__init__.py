from flask import Flask, request
from flask_restful import Api
from flask_cors import CORS
from mongoengine import connect
from app.resources import CreateUser, KeepAlive, FindMatch

connect('streetmeet')

main = Flask('StreetMeet')
api  = Api(main)
cors = CORS(main, origins=['https://lukvmil.github.io'])

@main.route('/')
def home():
    return "Hello, world!"

api.add_resource(CreateUser, '/api/user', '/user/')
api.add_resource(KeepAlive,'/api/user/<id>')
api.add_resource(FindMatch, '/api/match/<id>')