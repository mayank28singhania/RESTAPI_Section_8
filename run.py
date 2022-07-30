from new_app import new_app
from db import db

db.init_app(new_app)


@new_app.before_first_request
def create_tables():
    db.create_all()
