from design.connection import db
from flask import current_app
from design.connection import create_app

#createdb(app)

def createdb(app):
    with app.app_context():  
        db.create_all()
