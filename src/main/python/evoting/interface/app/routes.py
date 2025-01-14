from flask import Blueprint, render_template, request, redirect, url_for, flash, session

from src.main.python.evoting.application.controllers.AbstimmungsController import AbstimmungController
from src.main.python.evoting.application.dekoratoren.dekoratoren import log_method_call, handle_exceptions
from src.main.python.evoting.application.controllers.BürgerController import BuergerController
from datetime import datetime
from src.main.python.evoting.infrastructure.repositories.UserRepository import BuergerRepository

main = Blueprint('main', __name__)

# Dummy-Daten für Abstimmungen // nach Datenbank-Update wieder löschen
abstimmungen = [
    {
        "abstimmungs_id": "1",
        "titel": "Neue Parkanlage",
        "beschreibung": "Soll eine neue Parkanlage im Stadtzentrum gebaut werden?",
        "startdatum": datetime(2024, 1, 1),
        "enddatum": datetime(2024, 1, 31),
        "abstimmungsstatus": True,
    },
    {
        "abstimmungs_id": "2",
        "titel": "Schulreform",
        "beschreibung": "Soll die neue Schulreform eingeführt werden?",
        "startdatum": datetime(2024, 2, 1),
        "enddatum": datetime(2024, 2, 28),
        "abstimmungsstatus": False,
    },
]
teilgenommene_abstimmungen = [
    {"id": 1, "titel": "Neue Parkanlage", "stimme": "Ja", "status": "Offen"},
    {"id": 2, "titel": "Schulreform", "stimme": "Nein", "status": "Geschlossen"},
]

ergebnisse = [
    {"id": 2, "titel": "Schulreform", "ergebnis": "70% Ja, 30% Nein"}
]
aktueller_buerger = {
    "buergerid": 1,
    "vorname": "Max",
    "nachname": "Mustermann",
    "geburtstag": "1990-01-01",
    "adresse": "Musterstraße 1",
    "plz": "12345",
    "email": "max.mustermann@example.com",
    "rolle": "Bürger",
    "authentifizierungsstatus": True
}

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
            session['user_passwort'] = passwort
            session['user_name'] = buerger_daten['voller_name']  # Name speichern
            session['user_id'] = buerger_daten['buergerid']
            #flash("Login erfolgreich!", "success")
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
        vorname = request.form['vorname']
        nachname = request.form['nachname']
        geburtstag = request.form['geburtstag']
        adresse = request.form['adresse']
        plz = request.form['plz']
        email = request.form['email']
        passwort = request.form['password']


        try:
            # Benutzer zur Datenbank hinzufügen
            buerger_erstellen = BuergerController()
            buerger_daten = buerger_erstellen.erstelle_buerger(vorname, nachname, geburtstag, adresse, plz, email, passwort)
            flash("Registrierung erfolgreich! Bitte melden Sie sich an.", "success")

            if buerger_daten:
                return redirect(url_for('main.login'))

            return redirect(url_for('register.html'))

        except Exception as e:
            flash(f"Registrierung fehlgeschlagen: {e}", "danger")

    return render_template('register.html')

@main.route('/dashboard')
def dashboard():
    abstimmung_controller = AbstimmungController()
    email = session['user_email']  # Beispiel-Daten
    daten = abstimmung_controller.finde_abstimmungen_fuer_buerger(email)


    return render_template(
        'dashboard.html',
        user_name=session['user_name'],
        abstimmungen=daten,
        teilgenommene_abstimmungen=teilgenommene_abstimmungen,
        ergebnisse=ergebnisse
    )

@log_method_call
@handle_exceptions
@main.route('/abstimmung', methods=['GET', 'POST'])
def abstimmung():
    abstimmung_id = request.args.get('id')  # Versucht, den Parameter 'id' zu holen
    abstimmung_controller = AbstimmungController()

    if request.method == 'POST':
        # Daten aus dem Formular holen
        buergerid = session['user_id']
        stimme = request.form.get('vote')

        print(buergerid, stimme, abstimmung_id)

        # Überprüfen, ob Abstimmung und Bürger-ID vorhanden sind
        if not abstimmung_id or not buergerid:
            flash("Abstimmung oder Bürger-ID fehlt!", "error")
            return redirect(request.url)

        try:
            # Speichere die Stimme in die Datenbank
            abstimmung_controller.abstimmen(abstimmung_id, buergerid, stimme)
            flash("Deine Stimme wurde erfolgreich gespeichert!", "success")
            print('wurde gespeichert')
        except Exception as e:
            flash(f"Fehler beim Speichern der Stimme: {e}", "error")
            return redirect(request.url)

    # Hole Abstimmungsdaten für GET-Methode
    daten = abstimmung_controller.finde_abstimmung(abstimmung_id)
    return render_template('abstimmung.html', abstimmung=daten)

@main.route('/abstimmungen')
def abstimmungen_uebersicht():
    """
    Route, um alle Abstimmungen anzuzeigen, die für den Bürger zugänglich sind.
    """
    abstimmung_controller = AbstimmungController()
    email = session['user_email'] # Beispiel-Daten
    daten = abstimmung_controller.finde_abstimmungen_fuer_buerger(email)

    # Weitergabe an das Template
    return render_template("abstimmungen.html", abstimmungen=daten)


@main.route('/ergebnisse')
def ergebnis_übersicht():
    return render_template('ergebnisse.html', ergebnisse=ergebnisse)

@main.route('/profil')
def profil():
    if 'user_email' not in session:
        flash("Bitte loggen Sie sich zuerst ein.", "danger")
        return redirect(url_for('main.login'))

    # Benutzer aus der Datenbank anhand der gespeicherten E-Mail abrufen
    buerger_aufrufen = BuergerRepository()
    buerger_daten = buerger_aufrufen.finde_buerger_nach_email(session['user_email'])

    if not buerger_daten:
        flash("Benutzerprofil konnte nicht gefunden werden.", "danger")
        return redirect(url_for('main.dashboard'))

    return render_template('profil.html', buerger=buerger_daten)

@main.route('/logout')
def logout():
    session.pop('user_email', None)
    flash("Sie wurden erfolgreich ausgeloggt.", "info")
    return redirect(url_for('login'))