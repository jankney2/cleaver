from flask import render_template

from jinja2 import TemplateNotFound
from . import public_views

@public_views.route('/yeet')
def hello_world():
    return 'yeet'
    # return render_template('auth/register.html')
