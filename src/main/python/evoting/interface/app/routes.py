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

@main.route('/abstimmung')
def abstimmung():
    return render_template('abstimmung.html')

@main.route('/abstimmungen')
def abstimmungen():
    return render_template('abstimmungen.html')

@main.route('/ergebnisse')
def ergebnisse():
    return render_template('ergebnisse.html')
