from src.main.python.evoting.domain.entities.Buerger import Citizens
from src.main.python.evoting.infrastructure.services.AuthentifizierungsService import AuthentifizierungUser
from src.main.python.evoting.infrastructure.services.LoginService import UserLogin
from src.main.python.evoting.infrastructure.repositories.UserRepository import findCitizens

if __name__ == '__main__':
    userMail, userPassword = UserLogin()
    dataCitizens = findCitizens(userMail, userPassword)
    citizens = Citizens(dataCitizens[0], dataCitizens[1], dataCitizens[2], dataCitizens[3], dataCitizens[4],
                         dataCitizens[5], dataCitizens[6])

    AuthentifizierungUser(citizens.stimmberechtigung, citizens.authentifizierungsstatus)
