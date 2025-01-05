from flask import Flask
import os


def create_app():
    app = Flask(__name__)

    # Secret Key setzen (verwende eine Umgebungsvariable oder einen festen Wert)
    app.secret_key = os.urandom(24)  # Zufällig generierter 24-Byte-Schlüssel

    # Weitere Konfigurationen (Datenbank, Blueprints etc.)

    # Beispiel für das Hinzufügen von Blueprints oder anderen Konfigurationen
    from .routes import main
    app.register_blueprint(main)

    return app
