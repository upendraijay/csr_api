from flask import Flask
from .config import Config

app = Flask(__name__) #This line creates an instance of the Flask class and assigns it to the variable app. 
app.config.from_object(Config)

from app import routes # This line imports the routes module from the app package. By importing them here, they become part of the current module's namespace, allowing their contents to be accessed directly within the app/__init__.py module.