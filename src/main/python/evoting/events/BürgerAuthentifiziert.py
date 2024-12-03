from src.main.python.evoting.domain.entities.Buerger import Citizen
from src.main.python.evoting.infrastructure.services.AuthentifizierungsService import AuthentifizierungUser
from src.main.python.evoting.infrastructure.services.LoginService import UserLogin
from src.main.python.evoting.infrastructure.repositories.UserRepository import find_citizens


def main():
  user_mail, user_password = input("E-Mail: "), input("Passwort: ")
  data_citizen = find_citizens(user_mail, user_password)
  citizen = Citizen(
    citizen_id=data_citizen[0],
    name=data_citizen[1],
    email=data_citizen[2],
    password=data_citizen[3],
    role=data_citizen[4],
    authentifizierungsstatus=data_citizen[5],
    stimmberechtigung=data_citizen[6],
  )

  AuthentifizierungUser(citizen.stimmberechtigung, citizen.authentifizierungsstatus)


if __name__ == '__main__':
  main()
