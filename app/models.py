from flask import current_app as app

db=app.db


class Users(db.Model):
    __tablename__ = 'cleaver_users'
    _id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(100))
    email = db.Column('email', db.String(100))

    def __repr__(self):
        return f'User id={self.id} name={self.name} '

    @classmethod
    def create_or_update(cls):
        pass