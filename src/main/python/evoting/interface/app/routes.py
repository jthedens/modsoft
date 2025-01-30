from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from src.main.python.evoting.application.dekoratoren.dekoratoren import log_method_call, handle_exceptions
from src.main.python.evoting.domain.entities import Abstimmung
from src.main.python.evoting.application.controller import abstimmung_controller, ergebnis_controller, buerger_controller, buerger_repository
from src.main.python.evoting.domain.entities.Buerger import Buerger
from datetime import datetime

main = Blueprint('main', __name__)



# Landingpage-Route
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
          # Benutzer authentifizieren
          buerger_daten = buerger_controller.finde_buerger(email, passwort)

          if "error" in buerger_daten:
              flash(buerger_daten["error"], "danger")
              return redirect(url_for('main.register'))

          session['user_email'] = email
          session['user_passwort'] = passwort
          session['user_name'] = buerger_daten['voller_name']
          session['user_id'] = buerger_daten['buergerid']
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
        vorname = request.form['vorname']
        nachname = request.form['nachname']
        geburtstag = request.form['geburtstag']
        adresse = request.form['adresse']
        plz = request.form['plz']
        email = request.form['email']
        passwort = request.form['password']


        try:
            # Benutzer zur Datenbank hinzufügen
            buerger_daten = buerger_controller.erstelle_buerger(vorname, nachname, geburtstag, adresse, plz, email, passwort)
            flash("Registrierung erfolgreich! Bitte melden Sie sich an.", "success")

            if buerger_daten:
                return redirect(url_for('main.login'))

            return redirect(url_for('register.html'))

        except Exception as e:
            flash(f"Registrierung fehlgeschlagen: {e}", "danger")

    return render_template('register.html')

@log_method_call
@main.route('/dashboard')
def dashboard():
    daten = abstimmung_controller.finde_abstimmungen_fuer_buerger(session['user_email'])
    teilgenommene_daten = abstimmung_controller.teilgenommen_abstimmung(session['user_id'])
    ergebnis_daten = ergebnis_controller.zeige_beendete_abstimmungen()

    if 'user_name' not in session:
      flash("Bitte loggen Sie sich ein.", "warning")
      return redirect(url_for('main.login'))

    return render_template(
        'dashboard.html',
        user_name=session['user_name'],
        abstimmungen=daten,
        teilgenommene_abstimmungen=teilgenommene_daten,
        ergebnisse=ergebnis_daten
    )

@log_method_call
@handle_exceptions
@main.route('/abstimmung', methods=['GET', 'POST'])
def abstimmung():
    abstimmung_id = request.args.get('id')  # Versucht, den Parameter 'id' zu holen
    abstimmung = abstimmung_controller.finde_abstimmung(abstimmung_id)
    buergerid = session.get('user_id')
    voted = abstimmung_controller.service.pruefe_buerger_hat_abgestimmt(abstimmung_id, buergerid)

    if not abstimmung:
        flash("Abstimmung nicht gefunden.", "error")
        return redirect(url_for('main.abstimmungen_uebersicht'))

    if request.method == 'POST':
        buergerid = session.get('user_id')
        stimme = request.form.get('vote')

        if not abstimmung_id or not buergerid:
            flash("Abstimmung oder Benutzerinformationen fehlen!", "error")
            return redirect(request.url)

        if stimme not in ["Ja", "Nein"]:
            flash("Ungültige Auswahl. Bitte wählen Sie 'Ja' oder 'Nein'.", "error")
            return redirect(request.url)

        try:
            if not voted:
              abstimmung_controller.abstimmen(abstimmung_id, buergerid, stimme)
            # session['voted'] = True
              print("Session voted (POST):", session.get('voted'))  # Debugging nach dem Setzen
              flash("Vielen Dank für Ihre Teilnahme! Ihre Stimme wurde gezählt.", "success")
        except Exception as e:
            flash(f"Fehler beim Speichern der Stimme: {e}", "error")
            return redirect(request.url)

        # Zur Abstimmungsseite zurückkehren
        return redirect(url_for('main.abstimmung', id=abstimmung_id))

    return render_template(
        'abstimmung.html',
        abstimmung=abstimmung,
        voted=voted,
        status_offen = abstimmung.get("status")  # Zugriff auf den Status im Dictionary
    )


#Übersicht über alle Abstimmungen, die für den Bürger zugänglich sind.
@log_method_call
@main.route('/abstimmungen')
def abstimmungen_uebersicht():
    daten = abstimmung_controller.finde_abstimmungen_fuer_buerger(session['user_email'])
    return render_template("abstimmungen.html", abstimmungen=daten)

@log_method_call
@main.route('/ergebnisse')
def ergebnis_übersicht():
    ergebnis_daten = ergebnis_controller.zeige_beendete_abstimmungen()
    return render_template('ergebnisse.html', ergebnisse=ergebnis_daten)

@log_method_call
@main.route('/profil')
def profil():
    if 'user_email' not in session:
        flash("Bitte loggen Sie sich zuerst ein.", "danger")
        return redirect(url_for('main.login'))

    # Benutzer aus der Datenbank anhand der gespeicherten E-Mail abrufen
    buerger_daten = buerger_repository.finde_buerger_nach_email(session['user_email'])

    if not buerger_daten:
        flash("Benutzerprofil konnte nicht gefunden werden.", "danger")
        return redirect(url_for('main.dashboard'))

    return render_template('profil.html', buerger=buerger_daten)

#Nutzenden ausloggen
@log_method_call
@main.route('/logout')
def logout():
    session.clear()
    flash("Sie wurden erfolgreich ausgeloggt.", "info")
    return redirect(url_for('main.login'))
