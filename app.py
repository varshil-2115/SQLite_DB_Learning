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

    # create new user
    # new_user = User(
    #     username="varshil",
    #     email="varshil@gmail.com",
    #     password="1234"
    # )

    # add user to database session
    # db.session.add(new_user)

    # save changes
    # db.session.commit()

print("Database and tables created successfully!")