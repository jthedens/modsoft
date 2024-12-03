from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from ...infrastructure.repositories.UserRepository import find_citizens, add_citizen_to_database

main = Blueprint('main', __name__)

@main.route('/')
def landing_page():
    return render_template('landing.html')

# Login-Route
@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            # Benutzer in der Datenbank suchen
            citizen_data = find_citizens(email, password)
            if citizen_data:
                # Benutzer erfolgreich eingeloggt
                session['user_email'] = email  # Benutzer speichern
                flash("Login erfolgreich!", "success")
                return redirect(url_for('abstimmungen'))  # Weiterleitung
        except ValueError as e:
            # Fehlgeschlagener Login
            flash(str(e), "danger")

    return render_template('login.html')

# Registrierung-Route
@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        try:
            # Benutzer zur Datenbank hinzufügen
            add_citizen_to_database(name, email, password)
            flash("Registrierung erfolgreich! Bitte melden Sie sich an.", "success")
            return redirect(url_for('login'))
        except Exception as e:
            flash(f"Registrierung fehlgeschlagen: {e}", "danger")

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

@main.route('/logout')
def logout():
    session.pop('user_email', None)
    flash("Sie wurden erfolgreich ausgeloggt.", "info")
    return redirect(url_for('login'))
