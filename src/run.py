import sys
import os

# Pfad zu `main` hinzufügen
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'main')))

from python.evoting.interface.app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
