from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from src.main.python.evoting.application.dekoratoren.dekoratoren import log_method_call, handle_exceptions
from src.main.python.evoting.application.controllers.BürgerController import BuergerController
from src.main.python.evoting.domain.entities.Buerger import Buerger
from src.main.python.evoting.domain.entities import Abstimmung
from datetime import datetime

main = Blueprint('main', __name__)

@log_method_call
@handle_exceptions
@main.route('/')
def landing_page():
    return render_template('landing.html')

# Login-Route
@log_method_call
@handle_exceptions
@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        passwort = request.form['password']

        try:
            # Benutzer in der Datenbank suchen (Platzhalter-Funktion)
          buerger_aufrufen = BuergerController()
          buerger_daten = buerger_aufrufen.finde_buerger(email, passwort)

          if "error" in buerger_daten:
              flash(buerger_daten["error"], "danger")
              return redirect(url_for('main.login'))

          session['user_email'] = email
          session['user_name'] = buerger_daten.get('voller_name', 'Unbekannter Benutzer')
          flash("Login erfolgreich!", "success")
          return redirect(url_for('main.dashboard'))

        except ValueError as e:
            flash(str(e), "danger")

    return render_template('login.html')

# Registrierung-Route
@log_method_call
@handle_exceptions
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

            return redirect(url_for('register.html'))

        except Exception as e:
            flash(f"Registrierung fehlgeschlagen: {e}", "danger")

    return render_template('register.html')

@main.route('/dashboard')
def dashboard():
  if 'user_name' not in session:
    print("Benutzername fehlt in der Session. Umleitung zur Login-Seite.")
    return render_template('login.html')

    print("Benutzername gefunden:", session['user_name'])
    print("Abstimmungen:", abstimmungen)
    print("Teilgenommene Abstimmungen:", teilgenommene_abstimmungen)
    print("Ergebnisse:", ergebnisse)

  return render_template(
    'dashboard.html',
    user_name=session['user_name'],
    # abstimmungen=abstimmung,
    # teilgenommene_abstimmungen=teilgenommene_abstimmungen,
    # ergebnisse=ergebnisse
  )

@main.route('/abstimmung/<int:id>', methods=['GET', 'POST'])
def abstimmung(id):
    # Dummy-Daten (später durch Datenbankabfrage ersetzen)
    abstimmung = next((a for a in abstimmungen if a["abstimmungs_id"] == str(id)), None)

    if not abstimmung:
        return "Abstimmung nicht gefunden", 404

    if request.method == 'POST':
        # Verarbeitung der Stimme (ersetze später durch Datenbankintegration)
        stimme = request.form['vote']
        print(f"Stimme '{stimme}' wurde für Abstimmung {id} abgegeben.")
        return f"Danke für Ihre Stimme: {stimme}"

    return render_template('abstimmung.html', abstimmung=abstimmung)

@main.route('/abstimmungen')
def abstimmungen_uebersicht():
    return render_template('abstimmungen.html', abstimmungen=abstimmungen)

@main.route('/ergebnisse')
def ergebnis_übersicht():
    return render_template('ergebnisse.html', ergebnisse=ergebnisse)

@main.route('/profil')
def profil():
    return render_template('profil.html', buerger=aktueller_buerger) #ersetzen, wenn Datenbank Zugriff

@main.route('/logout')
def logout():
    session.pop('user_email', None)
    flash("Sie wurden erfolgreich ausgeloggt.", "info")
    return redirect(url_for('login'))
