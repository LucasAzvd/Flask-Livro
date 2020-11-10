from flask import render_template
from . import views

@auth.route('/login')
def login():
    return render_template('auth/login.html')