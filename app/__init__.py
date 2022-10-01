from flask import Flask, request
from flask_restful import Api

main = Flask('StreetMeet')
api  = Api(main)

@main.route('/')
def home():
    return "Hello, world!"