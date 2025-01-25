from flask import Flask
from flask_session import Session
import os


def create_app():
    app = Flask(__name__)

    # Secret Key setzen (verwende eine Umgebungsvariable oder einen festen Wert)
    app.secret_key = os.urandom(24)  # Zufällig generierter 24-Byte-Schlüssel

    # Flask-Session-Konfiguration
    app.config['SESSION_TYPE'] = 'filesystem'  # Speichert Sessions im Dateisystem
    app.config['SESSION_PERMANENT'] = False    # Optional: Sessions nur für die Browsersitzung
    app.config['SESSION_FILE_DIR'] = os.path.join(os.getcwd(), 'flask_session')  # Speichere Sessions in einem lokalen Ordner

    # Initialisiere die Flask-Session
    Session(app)

    # Weitere Konfigurationen (z. B. Datenbank, Blueprints etc.)
    from .routes import main
    app.register_blueprint(main)

    return app

