# src/main/python/evoting/application/controllers.py
from src.main.python.evoting.application.controllers.AbstimmungsController import AbstimmungController
from src.main.python.evoting.application.controllers.BürgerController import BuergerController
from src.main.python.evoting.application.controllers.ErgebnisController import ErgebnisController
from src.main.python.evoting.infrastructure.repositories.UserRepository import BuergerRepository

# Globale Controller-Instanzen
abstimmung_controller = AbstimmungController()
buerger_controller = BuergerController()
ergebnis_controller = ErgebnisController()
buerger_repository = BuergerRepository()
