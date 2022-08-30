from flask import Flask


app=Flask(__name__)
app.config['SECRET_KEY']='my_chemical_romance'
app.config['SQLALCHEMY_DATABSE_URI']='sqlite:///db.sqlite'


#     register blueprints
from info import info as info_blueprint
app.register_blueprint(info_blueprint)




