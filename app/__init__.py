from flask import Flask
from config import Config
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)
app.config['DEBUG'] = True
app.config['TESTING'] = True

from app import routes
