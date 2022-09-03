from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_session import Session
from . import models



def page_not_found_handler():
    return 'Page not found dumbass'

def server_error_handler():
    return 'yo we had a problem with our server. working on that!'

def create_app(environment: str = None):
    app=Flask(__name__)
    app.config['SECRET_KEY']='my_chemical_romance'

    if environment:
        app_env=environment
    else:
        app_env=os.environ.get('APP_ENV', 'DEV')

    # database config
    db = SQLAlchemy(app)

    if app_env=='PROD':
        app.config['SQLALCHEMY_DATABSE_URI'] = 'sqlite:///db.sqlite'
    if app_env=='DEV':
        app.config['SQLALCHEMY_DATABSE_URI']='localhost:'

    db.create_all()
    #     register blueprints
    app.register_error_handler(404, page_not_found_handler)
    app.register_error_handler(500, server_error_handler)

    from app.info import info as info_blueprint
    app.register_blueprint(info_blueprint)

    return app



