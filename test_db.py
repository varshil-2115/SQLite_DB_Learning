from app import app
from models import User

with app.app_context():

    user = User.query.filter_by(email="varshil@gmail.com").first()

    if user:
        print("User Found")
        print(user.username)

    else:
        print("User Not Found")