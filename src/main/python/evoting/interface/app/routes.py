from flask import Blueprint, render_template, request, redirect, url_for, flash, session
#from ...infrastructure.repositories.UserRepository import find_citizens, add_citizen_to_database
from ...domain.entities import Abstimmung
from datetime import datetime

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
            # Benutzer in der Datenbank suchen (Platzhalter-Funktion)
            citizen_data = find_citizens(email, password)
            if citizen_data:
                session['user_email'] = email
                session['user_name'] = citizen_data['name']  # Name speichern
                flash("Login erfolgreich!", "success")
                return redirect(url_for('main.dashboard'))
        except ValueError as e:
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
            return redirect(url_for('main.login'))
        except Exception as e:
            flash(f"Registrierung fehlgeschlagen: {e}", "danger")

    return render_template('register.html')

@main.route('/dashboard')
def dashboard():
    user_name = session.get('user_name', 'Gast')
    return render_template(
        'dashboard.html',
        user_name=user_name,
        abstimmungen=abstimmungen,
        teilgenommene_abstimmungen=teilgenommene_abstimmungen,
        ergebnisse=ergebnisse
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

@main.route("/profil")
def profil():
  return render_template("profil.html")

@main.route('/logout')
def logout():
    session.pop('user_email', None)
    flash("Sie wurden erfolgreich ausgeloggt.", "info")
    return redirect(url_for('login'))
