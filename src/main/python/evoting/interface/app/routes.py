from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from src.main.python.evoting.application.controllers.BürgerController import BuergerController
from src.main.python.evoting.infrastructure.services.UserService import BuergerService
from src.main.python.evoting.infrastructure.repositories.UserRepository import BuergerRepository

main = Blueprint('main', __name__)

@main.route('/')
def landing_page():
    return render_template('landing.html')

# Login-Route
@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        passwort = request.form['password']

        try:
            #repository = BuergerRepository()
            #service = BuergerService(repository)
            #controller = BuergerController()
            # Benutzer in der Datenbank suchen
            buerger_aufrufen = BuergerController()
            buerger_daten = buerger_aufrufen.finde_buerger(email,passwort)

            if buerger_daten:
                # Benutzer erfolgreich eingeloggt
                #session['user_email'] = email  # Benutzer speichern
                #flash("Login erfolgreich!", "success")
                return redirect(url_for('main.abstimmungen'))  # Weiterleitung
        except ValueError as e:
            # Fehlgeschlagener Login
            flash(str(e), "danger")

    return render_template('login.html')

# Registrierung-Route
@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        buergerid = request.form['buergerid']
        vorname = request.form['vorname']
        nachname = request.form['nachname']
        geburtstag = request.form['geburtstag']
        adresse = request.form['adresse']
        plz = request.form['plz']
        email = request.form['email']
        passwort = request.form['password']
        rolle = request.form['rolle']
        authentifizierungsstatus = request.form['authentifizierungsstatus']

        try:
            # Benutzer zur Datenbank hinzufügen
            buerger_erstellen = BuergerController()
            buerger_daten = buerger_erstellen.erstelle_buerger(buergerid, vorname, nachname, geburtstag, adresse, plz, email, passwort, rolle, authentifizierungsstatus)
            flash("Registrierung erfolgreich! Bitte melden Sie sich an.", "success")
            if buerger_daten:
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
