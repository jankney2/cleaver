from flask import session


def logout():
    session.pop('user', None)
    return
