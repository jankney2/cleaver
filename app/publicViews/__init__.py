from flask import Blueprint

public_views = Blueprint('public_views', __name__)

from . import views
