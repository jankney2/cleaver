from flask import render_template

from jinja2 import TemplateNotFound
from . import info

@info.route('/')
def hello_world():
    return render_template('auth/register.html')
