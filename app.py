from flask import Flask
from extensions import db

app = Flask(__name__)

# database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# disable warnings
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# connect db with app
db.init_app(app)

# import models AFTER db setup
from models import User

# create tables
with app.app_context():
    db.create_all()

print("Database and tables created successfully!")