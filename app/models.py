from flask import current_app as app

db=app.db


class Users(db.model):
    __tablename__ = 'cleaver_users'
    _id=db.column('id', db.Integer, primary_key=True)
    name=db.column('name', db.String(100))
    email=db.column('email', db.String(100))

    def __repr__(self):
        return f'User id={self.id} name={self.name} '