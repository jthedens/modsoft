from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def landing_page():
    return render_template('landing.html')

@main.route('/login')
def login():
    return render_template('login.html')

@main.route('/register')
def register():
    return render_template('register.html')
