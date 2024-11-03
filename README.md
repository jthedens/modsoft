# Modul Moderne Softwareentwicklung (Gruppe 8 - eVote)

## Übung 1 (Git)

---

## Was ist Git und warum sollte es verwendet werden?

1. Während andere Versionskontrollsystemen nur die Unterschiede in den Änderungen speichern, erstellt  Git häufig "Snapshots" der Dateien. Das bringt viele Vorteile, besonders jedoch hinsichtlich des Branchings.
   
2. Außerdem legt Git großen Wert auf die Sicherheit und Integrität der Daten. Jeder Commit erhält einen eindeutigen SHA-1-Hashwert, der sicherstellt, dass nachträgliche Änderungen oder Vertuschungen nicht möglich sind. Dies ermöglicht auch die Wiederherstellung von früheren Versionen.
   
3. Der Großteil der Arbeit mit Git erfolgt zudem lokal, was nützlich ist, wenn man unterwegs ist oder temporär keinen Internetzugang hat.

4. Git besitzt eine gewisse "Zeitmaschinen-Funktionalität" es ist möglich, mutige Änderungen zu testen und problemlos anzunehmen oder zu verwerfen. Git fördert somit eine dynamische und risikofreudige Arbeitsweise.
   
5. Des Weiteren fördert Git Branching, also das Erstellen von Verzweigungen (Branches), was eine flexible und parallele Entwicklung ermöglicht.
   
6. Git-Repositories können eine hierarchische Struktur bilden, bei der viele Klone für die Entwicklung verwendet werden und ein Master-Repository alle Änderungen sammelt.
   
 ![image](https://github.com/user-attachments/assets/00fb8d05-65da-49ac-b6d3-508fa29a7eb5)

## Grundlegende Git-Befehle

### git status
git status gibt an, welche Dateien geändert wurden und in welchem Zustand diese sich befinden (getrackt oder nicht getrackt)

![image](https://github.com/user-attachments/assets/2b797420-4c41-4ac5-abee-71b8a083f539)

### git add
Das Kommando git add wird verwendet, um Dateien oder Verzeichnisbäume unter die Versionskontrolle von Git zu stellen. Es kann sowohl neue als auch geänderte Dateien zum Staging-Bereich hinzufügen. Mit diesem Befehl bereitet Git alles für den nächsten Commit vor, indem es den Snapshot bzw. das Index-Update aktualisiert.

![image](https://github.com/user-attachments/assets/c20f5259-ba5e-487a-91e8-80643508635c)

git add README.md         # Nur eine Datei hinzufügen

git add *.java            # Alle Java-Dateien hinzufügen

git add SecretFolder      # Einen Ordner rekursiv hinzufügen

git add .                 # Alle Änderungen hinzufügen

Die letzte Option (git add .) ist zwar die einfachste, aber es kann zu unerwarteten Nebenwirkungen kommen, wenn ungewollte Änderungen mit gestaged werden. Daher sollte man vorsichtig sein und im Zweifel explizit Dateien auswählen, um Überraschungen zu vermeiden.
Hinweis: Kein Commit ohne ein vorheriges git add! Wenn Änderungen nicht gestaged und committed werden, sind sie nicht sichtbar, auch nicht auf GitHub.
Wichtig: Man kann auch mit git commit -a -m "Nachricht" alles in einem Schritt erledigen, aber es wird empfohlen, git add explizit zu verwenden, um bessere Kontrolle über die Änderungen zu behalten.

## git diff
git diff ist ein UNIX-Befehl und listet alle Änderungen im Detail auf. Das heißt, dass wenn in einer Zeile etwas geändert wurde, alt und neu in rot (= verschwunden) und grün (neu hinzugefügt) erscheinen. Es werden stets die Unterschiede zwischen dem Arbeitsverzeichnis und dem Staging-Bereich angezeigt. Wenn eine Datei geändert wurde, aber noch nicht gestaged ist, zeigt git diff diese Änderungen an. Wichtig ist, dass git diff immer den Vergleich zur letzten committeten Version macht.

![image](https://github.com/user-attachments/assets/b5da56ec-25a4-433a-8831-31e0df5c6e19)

## git commit
Mit git commit werden alle gestagten Änderungen in das Repository übernommen und dauerhaft gespeichert. Der Staging-Bereich wird nach dem Commit geleert, und die Änderungen sind nun Teil der Git-Historie.

![image](https://github.com/user-attachments/assets/efc39d97-11b9-4cd2-8465-c2d17b9011a1)

Wichtige Optionen:

-a: Fügt alle geänderten Dateien hinzu (falls vergessen) und committet sie in einem Schritt.

-m: Erlaubt es, eine Commit-Nachricht direkt in der Kommandozeile zu schreiben, ohne einen Editor zu öffnen.

Man kann außerdem Dateien oder Dateimuster angeben, um nur spezifische Dateien zu committen.
Falls ein Commit falsch war, kann man mit der Option --amend den letzten Commit nachträglich ändern. Das ist besonders hilfreich, um Fehler zu korrigieren, ohne einen neuen Commit erstellen zu müssen.

## git push 
Mit dem Befehl git push werden alle lokalen Commits mit dem Remote-Server synchronisiert. Man überträgt damit die Änderungen, die lokal vorgenommen wurden, in das zentrale Repository. Normalerweise ist das Remote-Repository in der .git/config gespeichert, sodass man meist nur git push ausführen muss, ohne das Repository explizit anzugeben.

Wichtig: Beim Arbeiten im Team sollte man daran denken, frühzeitig git pull auszuführen, um sicherzustellen, dass man über die Änderungen informiert ist, die andere Teammitglieder bereits mit git push an den Server gesendet haben.
Falls man über das HTTPS-Protokoll pusht, kann es hilfreich sein, das Passwort zu cachen, um es nicht bei jeder Push-Operation erneut eingeben zu müssen.

## git pull / git fetch
Mit git pull und git fetch vergleicht man die Änderungen auf dem Remote-Server mit dem lokalen Branch. Diese Befehle helfen dabei, die lokalen Änderungen mit denen im zentralen Repository abzugleichen.

git pull: Dieser Befehl lädt die Änderungen vom Remote-Repository und führt anschließend einen Merge mit dem lokalen Branch durch.

git fetch: Hierbei werden nur die Änderungen vom Remote-Repository heruntergeladen, ohne dass sie direkt in den lokalen Branch integriert werden. Man kann später manuell mergen.

Wichtig: Der Unterschied zwischen den beiden Befehlen ist, dass git pull direkt einen Merge durchführt, während git fetch nur die Änderungen abruft, ohne sie zu mergen.
Normalerweise wird die Adresse des Remote-Repositorys aus der Konfigurationsdatei .git/config gelesen.

## git rm und git mv
Mit dem Befehl git rm werden Dateien aus dem Git-Repository entfernt. Dieser Vorgang erfolgt in zwei Schritten: Zuerst muss die Datei physisch gelöscht werden (z. B. mit DEL oder rm file), bevor die Änderungen mit git commit festgeschrieben werden. Zum Entfernen einer Datei verwendet man den Befehl:

$ git rm <dateiname>

Falls eine Datei nur aus dem Index entfernt werden soll, aber nicht physisch gelöscht werden muss, kann die Option --cached verwendet werden:

$ git rm --cached <dateiname>

Der Befehl git mv wird verwendet, um Dateien umzubenennen oder zu verschieben. Dies geschieht ebenfalls durch eine Kombination aus rm und add, was bedeutet, dass Git intern diese beiden Schritte zusammenführt:

$ git mv <alter_dateiname> <neuer_dateiname>

Dieser Befehl vereinfacht den Prozess, indem er die Datei verschiebt oder umbenennt und die Änderungen sofort für den nächsten Commit vorbereitet.

--- 

## Was sind Branches?
Ein Branch (Zweig) in Git ist eine unabhängige Entwicklungsumgebung, die es ermöglicht, gleichzeitig an verschiedenen Features, Bugfixes oder Experimenten zu arbeiten, ohne die Hauptarbeit auf dem main-Branch zu beeinträchtigen.

- Der main-Branch ist standardmäßig der Hauptzweig, in den normalerweise der fertige Code gemerged wird.
- Entwickler erstellen für jede Aufgabe einen neuen Branch, um dort isoliert zu arbeiten. Zum Beispiel:

`git checkout -b feature/neues-feature`

### Warum Branches nutzen?
- **Isolierte Entwicklung**: Änderungen in einem Branch wirken sich nicht auf den Hauptcode aus, bis sie gemerged werden.
- **Paralleles Arbeiten**: Mehrere Teammitglieder können gleichzeitig an unterschiedlichen Teilen eines Projekts arbeiten.
- **Rückverfolgbarkeit**: Änderungen sind einfacher nachvollziehbar, da jeder Branch eine spezifische Aufgabe repräsentiert.

### Branching-Strategien
- **Feature Branches**: Für jedes neue Feature oder jede neue Aufgabe wird ein eigener Branch erstellt und nach Fertigstellung in den Hauptbranch gemerged.
- **Release Branches**: Diese Branches dienen zur Vorbereitung einer neuen Version und sind von `main abgezweigt, um letzte Anpassungen vorzunehmen.
- **Hotfix Branches**: Dienen zur schnellen Behebung von Fehlern im Produktionscode.

### Merge-Konflikte
Ein Merge-Konflikt tritt auf, wenn zwei Branches Änderungen an denselben Zeilen in einer Datei vorgenommen haben und Git nicht automatisch entscheiden kann, welche Änderung übernommen werden soll.

- Wie entstehen Merge-Konflikte? Ein häufiger Fall ist, wenn zwei Entwickler gleichzeitig an derselben Datei arbeiten und diese dann in den main-Branch zusammengeführt werden sollen.
- Lösen von Merge-Konflikten:
  1. Git teilt mit, in welchen Dateien ein Konflikt besteht, wenn der merge- oder pull-Befehl ausgeführt wird.
  2. Öffne die betroffenen Dateien. Git markiert die konfliktverursachenden Zeilen mit:
  ```bash
    <<<<<<< HEAD
    // Dein aktueller Branch
    =======
    // Änderungen aus dem Branch, den du mergen möchtest
    >>>>>>> branchname
  ```

3. Entscheide, welche Version der Änderungen übernommen werden soll (oder kombiniere beide).
4. Entferne die Konfliktmarkierungen und committe die Änderungen:
  ```bash
  git add DateiName
  git commit -m "Löse Merge-Konflikte"
  ```

### Branching in Zusammenarbeit mit anderen Tools
Mit dem Tool  GitHub oder GitLab können Pull Requests (PR) oder Merge Requests (MR) erstellt werden, um Branches zu reviewen und zu mergen.


---

## Git mit PyCharm benutzen - Local Repository und Remote Repository
 
Versionsverwaltungs-Tools wie Git lassen sich optimal in integrierte Entwicklungsumgebungen (IDEs) wie PyCharm einbinden. Dies erleichtert den Umgang mit Git für Entwickler deutlich. Git ermöglicht es, Änderungen an einem Projekt nachvollziehbar zu machen und PyCharm bietet eine Integration, um Git-Befehle direkt in der IDE auszuführen.
Um diese Konstellation zu nutzen, müssen sowohl Git als auch PyCharm auf dem Computer installiert sein. PyCharm bietet bereits eine direkte Integration von Git ohne zusätzliche Plugins.

<img align="right" width="200px" hspace="15" vspace="15" src="Git_Menue.png" alt="image" />

### Git in PyCharm nutzen
PyCharm bietet zwei Hauptmöglichkeiten, um Git-Befehle auszuführen:
1. Über das Terminal: Git-Befehle können wie gewohnt direkt im Terminal eingegeben werden.
2. Über die GUI (Menüpunkte): PyCharm stellt über das Menü eine benutzerfreundliche Oberfläche bereit, um die wichtigsten Git-Befehle auszuführen.

### Projekte mit Git-Repositories verknüpfen
Beim Anlegen eines neuen Projekts in PyCharm besteht die Möglichkeit, Git-Repositories mit kollaborativen Versionsverwaltungen wie GitHub zu verknüpfen. Dies erlaubt das Klonen eines bestehenden Remote-Repositories auf ein lokales Repository. Dazu muss die URL des Repositories in PyCharm angegeben werden. Dabei kann der Speicherort des lokalen Repositories individuell festgelegt werden.

### Grundlegende Git-Operationen in PyCharm
Sobald die Versionskontrolle verknüpft ist (der Remote-Zugriff wird automatisch generiert), können grundlegende Operationen wie das Committen, Pullen oder Pushen von Änderungen über den Menüpunkt „Git “ ausgeführt werden:
- Änderungen hinzufügen und committen: Dateien können ausgewählt, gestaged und mit einer Commit-Nachricht versehen werden.  Mit Git > Commit (Strg + K) wird dieser Prozess angestoßen.
- Pushen von Änderungen: Commits können mit Git > Push (Strg + Shift + K) direkt an das verknüpfte Remote-Repository gesendet werden.
- Pullen von Änderungen: Um die neuesten Änderungen aus einem Remote-Repository zu beziehen, bietet PyCharm den Befehl Git > Pull.

Mit PyCharm können Tools wie das Anzeigen von Diff-Dateien (um Unterschiede zwischen verschiedenen Versionen eines Projekts darzustellen) genutzt werden, sowie die Möglichkeit, Branches zu erstellen und zu verwalten.

Weitere Informationen zu diesem Thema: https://www.jetbrains.com/help/pycharm/set-up-a-git-repository.html

---

## Nützliche Tools und Plattformen

GitHub: Eine der bekanntesten Plattformen für die Versionskontrolle, die es Entwicklern ermöglicht, Projekte zu hosten, zusammenzuarbeiten und Issues zu verwalten.	Features: Pull-Requests, Code-Reviews, Actions für CI/CD, GitHub Pages.

GitLab:	Eine integrierte Plattform für DevOps, die Git-Repositories, CI/CD und Projektmanagement bietet. Features:	Automatisierte Deployments, Issue-Tracking, Wiki-Funktion.

Bitbucket:	Eine Plattform für die Versionskontrolle, die eng mit Atlassian-Tools wie Jira und Trello verbunden ist. Features:	Pull-Requests, Pipelines für CI/CD, Integration mit anderen Atlassian-Produkten.

SourceForge:	Eine Plattform für Open-Source-Projekte, die Hosting und Versionskontrolle bietet. Features:	Projektverwaltung, Bug-Tracking, Download-Statistiken.

GitKraken:	Ein visueller Git-Client, der die Arbeit mit Git-Repositories erleichtert. Features: Drag-and-Drop-Interface, integriertes Issue-Tracking, Team-Kollaboration.

---

## Dokumentation der Zusammenarbeit (Übung 1)
- Was ist Git und warum sollte es verwendet werden? *- bearbeitet von Vera Kammerer*
- Grundlegende Git-Befehle *- bearbeitet von Vera Kammerer*
- Branches und ihre Nutzung, Umgang mit Merge-Konflikten *- bearbeitet von Josefine Theden-Schow*
- Git mit IntelliJ/PyCharm benutzen: Local Repository und Remote Repository *- bearbeitet von Niklas Wehl*
- Nützliche Git-Tools und Plabormen (z. B. GitHub) *- bearbeitet von Jan Eberlein*



---

---


## Übung 2 (CI/CD)

---

### Was ist CI/CD? Was sind die Vorteile?

CI/CD steht für **Continuous Integration (CI)** und **Continuous Deployment (CD)**. 

Continuous Integration (CI):
Continuous Integration ist ein Konzept, bei dem der Code automatisch, regelmäßig und fortlaufend zusammengeführt wird. Mit diesem Verfahren können Fehler im Code frühzeitig erkannt und die Effizienz in der Entwicklung gesteigert werden. Automatisierte Tests, die bei jeder Codeänderung durchlaufen werden, helfen, Unstimmigkeiten frühzeitig zu erkennen. Diese Automatisierung kann den gesamten Prozess von der Änderung bis zur Auslieferung der Software umfassen. Der Umfang dieser Tests lässt sich individuell an die Anforderungen des Projekts anpassen

Continuous Deployment (CD):
Continuous Deployment (CD) ist eine Methode in der Softwareentwicklung, bei der Änderungen im Code automatisch und fortlaufend in die Produktionsumgebung übertragen werden, sobald alle Tests erfolgreich bestanden sind. Es erweitert das Konzept des Continuous Delivery und ermöglicht es, jede geprüfte Codeänderung ohne manuelle Freigabe direkt den Nutzern bereitzustellen.


### Wie können wir CI/CD in unser Projekt integrieren?

Erstes Ziel: Eine einfach gehaltene CI-Pipeline, die primär zur Fehlererkennung dient und den Code auf Integrität und Stabilität überprüft.
Späteres Ziel: Erweiterung der Pipeline um automatisierte Deployment-Schritte, sobald die grundlegende CI-Konfiguration stabil läuft.
Die Pipeline soll im Verlauf der Entwicklung schrittweise und gemeinsam mit dem Team angepasst und optimiert werden.

Für ein Python-Projekt sind GitHub Actions und GitLab CI/CD gängige und gut unterstützte Optionen, die eine gute Integration in bestehende Git-Repositories bieten.

Sobald die grundlegende CI-Pipeline zuverlässig läuft und Fehler effektiv erkannt werden, kann die Pipeline um CD-Funktionen erweitert werden. Dabei wird zunächst ein automatisiertes Deployment in eine Staging-Umgebung eingerichtet, um das Deployment zu testen und mögliche Fehler frühzeitig zu erkennen. 
Sobald die Staging-Deployments stabil laufen, kann das automatische Deployment hinzugefügt werden, idealerweise mit einem manueller Freigabeschritt.

Die Pipeline sollte kontinuierlich auf Basis von Team-Feedback und Projektanforderungen weiterentwickelt werden.

Zu den möglichen Erweiterungen könnten gehören: Testabdeckung erweitern, Parallelisierung der Tests, Performance-Tests, …


### Begründung für die Wahl von GitHub Actions:

Um eine CI/CD-Pipeline in unser Projekt zu integrieren, haben wir uns für die Plattform GitHub Actions entschieden. Ein Hauptargument für diese Wahl ist die nahtlose Integration in bestehende Git-Repositories. Da Workflows direkt auf der Plattform eingerichtet werden können, auf der das Projekt gehostet wird, wird die Verwaltung der Workflows erheblich vereinfacht.

Zusätzlich bietet GitHub Actions eine große Auswahl an vordefinierten Actions, die flexibel anpassbar sind. Die YAML-Dateien zur Workflow-Konfiguration lassen sich unkompliziert im Repository anpassen, was das Maß an Flexibilität im Entwicklungsprozess erhöht.

Weitere Vorteile von GitHub Actions:

- Umfangreiche Bibliothek an Workflows und Actions
- Automatisierung durch ereignisbasierte Trigger (z. B. beim Push oder Pull-Request)
- Kostenfreie Nutzung für öffentliche Repositories und einfache Aktivierung ohne zusätzliche Registrierung

---

### Einrichtung der CI/CD-Pipeline

```bash
name: Python CI Pipeline

on:
  push:
    branches:
      - main
  pull_request:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Check out code
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

      - name: Run tests (skip if no tests yet)
        run: |
          echo "No tests to run at this stage."

```
---

### Tests hinzufügen



---








---

## Übung 3 (UML & DDD)

Ergebnisse aus unserem Miro-Board: https://miro.com/app/board/uXjVLO2HW6A=/?share_link_id=761067200081

___

### Event Storming

#### Nutzerregistrierung und Authentifizierung

BürgerInnen:
- Fordert Registrierung an
- Bestätigt Link in E-Mail.


System:
- Wahlberechtigungprüfen
- Bestätigungs-E-Mail gesendet
- Bürgerregristrierung erfolgreich abgeschlossen


#### Abstimmungsübersicht

BürgerInnen:
- Fordert Abstimmungsübersicht an


System:
- Liste der verfügbaren Abstimmungen wird angezeigt

#### Abstimmungsmechanismus

BürgerInnen:
- Wählt Abstimmung aus
- Gibt Stimme ab


System:
- Abstimmung eröffnet

#### Abstimmungssicherheit

System:
- System prüft, ob Stimme zum ersten Mal abgegeben
- Stimme wird gezählt > Zugang zur Abstimmung gesperrt
- ODER: Stimme wird verworfen

#### Ergebnisübersicht

BürgerInnen:
- Fordert Ergebnisübersicht an

System:
- Abstimmungsergebnisse werden angezeigt




---

### Domänenmodell

<img align="center" width="500px" hspace="15" vspace="15" src="U3 Abb 2.png" alt="Abbildung 2" />

**Bürger**: Eine Person, die sich im System registriert und an Abstimmungen teilnimmt.
- Bürger-ID: string
- Name: string
- E-Mail: string
- Authentifizierungsstatus: boolean
- Stimmberechtigung.: boolean

**Organisation**
- Organisations-ID: string
- Name: string
- Kontakt: string
- Authentifizierungsstatus: boolean

**Abstimmung**: Eine Abstimmung zu einem bestimmten städtischen Thema oder Projekt.
- Abstimmungs-ID: string
- Titel: string
- Beschreibung: string
- Organisations-ID: string
- Frist: date
- Abstimmungsstatus: boolean
- verfügbare Optionen.: string

**Stimme**: Die von einem Bürger abgegebene Wahlentscheidung.
- Bürger-ID: string
- Abstimmungs-ID: string
- Wahloption: string

---

### Bounded Contexts

#### Inhaltsmanagment
- Erstellung der Abstimmung und bestimmen der Rahmenbedingungen (Zu welcher Sache wird abgestimmt und der Gruppe von Usern darf abstimmen ...)

#### Registrierungsverwaltung
- Koordiniert die Registrierung der Bürger:innen und überprüft in diesem Zusammenhang die Wahlberechtigung. (Erfassen von personenbezogenen Daten, Zuweisung einer Rolle, …).

#### Abstimmungsverwaltung
- Stellt die Abstimmung/Themen zur Verfügung über die die Bürger:innen abstimmen können
- Erfasst die abgegebenen Stimmen
- Überwacht die Korrektheit der Abstimmung (Abstimmungssicherheit/-sicherheit)

#### Ergebnisauswertung
- Erstellt nach Abgabe der Stimme eine Ergebnisübersicht
- Schließt die Abstimmung nach Abgabe aller Stimmen

<img align="center" width="500px" hspace="15" vspace="15" src="U3 Abb 3.png" alt="Abbildung 3" />


---

### Entitäten und Aggregate

#### Inhaltsmanagment
Entität: Organisation \
Aggregate: Organisation

- Erstellen der Inhalte der Abstimmungen (Texte und Informationen)
- Rahmenbedingen der jeweiligen Abstimmung (Anzahl der Stimmen, Bürger-Gruppe, Rollenberechtigungen, ...)

#### Registrierungsverwaltung
Entität: Bürger \
Aggregate: Bürger

- Erfassen der Daten: Name, E-Mail, Geburtsdatum, Adresse, ...
- Registrierung bestätigen oder ablehnen
- Erstellen einer eindeutigen ID/Kennung
- Zuweisen einer Rolle (Bürger/Organisator/Gast, ...)

#### Abstimmungsverwaltung
Entität: Abstimmung \
Aggregate: Abstimmung

- Bietet eine Übersicht mit allen Abstimmungen
- Beinhaltet Informationstexte und eine Option zum Abstimmen
- Bestätigen der Stimme mit abschließen des Prozesses
- Erfassen der Stimme
- Überwacht die Korrektheit der Abstimmung

#### Ergebnisauswertung
Entität: Ergebnis \
Aggregate: Ergebnis

- Beinhaltet alle Stimmen
- Bereitet das Ergebnis aller Stimmen auf
- Sperrt die Abstimmung

---

### Domain Services und Repositories

#### Domain Services

**a. AbstimmungsService** 
- **Beschreibung:** Verwaltet die Logik rund um den Abstimmungsprozess und die Verwaltung der Abstimmungen.
- **Methoden:**
  - erstelleAbstimmung(titel: string, beschreibung: string, frist: date, optionen: string[]): Abstimmung
    - Erstellt eine neue Abstimmung mit den angegebenen Details.
  - aktualisiereAbstimmung(abstimmungsID: string, neueDaten: Abstimmungsdaten): Abstimmung
    - Aktualisiert die Daten einer bestehenden Abstimmung.
  - sperreAbstimmung(abstimmungsID: string): boolean
    - Sperrt eine Abstimmung, sodass keine weiteren Stimmen mehr abgegeben werden können.


**b. StimmService**
- **Beschreibung:** Verwaltet die Logik rund um die Abgabe und Verwaltung von Stimmen.
- **Methoden:**
  - stimmeAbgeben(buergerID: string, abstimmungsID: string, wahloption: string): Stimme
    - Fügt eine Stimme zu einer Abstimmung hinzu.
  - überprüfeStimmberechtigung(buergerID: string, abstimmungsID: string): boolean
    - Prüft, ob der Bürger für die Abstimmung stimmberechtigt ist.

**c. ErgebnisService**
- **Beschreibung:** Verwaltet die Berechnung und Verwaltung von Ergebnissen, die separat von der Abstimmung existieren.
- **Methoden:**
  - berechneErgebnis(abstimmungsID: string): Ergebnis
    - Berechnet das Ergebnis einer Abstimmung, indem alle abgegebenen Stimmen berücksichtigt werden.
  - speichereErgebnis(ergebnis: Ergebnis): void
    - Speichert das berechnete Ergebnis für eine Abstimmung.
  - zeigeErgebnis(abstimmungsID: string): Ergebnis
    - Gibt das berechnete Ergebnis zurück, falls die Abstimmung abgeschlossen und gesperrt ist.


#### Repositories


**a. AbstimmungRepository**
- **Beschreibung:** Verwaltet die Persistenz der Abstimmungs-Entitäten.
- **Methoden:**
  - speichereAbstimmung(abstimmung: Abstimmung): void
    - Speichert eine neue Abstimmung.
  - findeAbstimmung(abstimmungsID: string): Abstimmung
    - Sucht eine Abstimmung basierend auf ihrer ID.
  - aktualisiereAbstimmung(abstimmung: Abstimmung): void
    - Aktualisiert eine bestehende Abstimmung in der Datenbank.
  - loescheAbstimmung(abstimmungsID: string): void
    - Löscht eine Abstimmung basierend auf ihrer ID.

**b. StimmeRepository**
- **Beschreibung:** Verwaltet die Persistenz der Stimme-Entitäten.
- **Methoden:**
  - speichereStimme(stimme: Stimme): void
    - Speichert eine abgegebene Stimme.
  - findeStimmenNachAbstimmung(abstimmungsID: string): List<Stimme>
    - Gibt alle Stimmen für eine bestimmte Abstimmung zurück.

**c. ErgebnisRepository**
- **Beschreibung:** Verwaltet die Persistenz der Ergebnis-Entitäten, die separat von der Abstimmung gespeichert werden.
- **Methoden:**
  - speichereErgebnis(ergebnis: Ergebnis): void
    - Speichert ein berechnetes Ergebnis.
  - findeErgebnisNachAbstimmung(abstimmungsID: string): Ergebnis
    - Sucht das Ergebnis einer bestimmten Abstimmung.
  - aktualisiereErgebnis(ergebnis: Ergebnis): void
    - Aktualisiert das Ergebnis einer Abstimmung, falls Anpassungen notwendig sind.
  - loescheErgebnis(ergebnisID: string): void
    - Löscht ein Ergebnis basierend auf seiner ID.

---

### Strategie zur Implementierung des DDD-Modells in Code

Die vorliegende Strategie beschreibt einen strukturierten Ansatz zur Implementierung von Domain-Driven Design (DDD) Modellen in Code, wobei die Aspekte Testbarkeit und Modularität berücksichtigt werden.

**1. Domänenverständnis**

Zunächst muss eine „gemeinsame Sprache“ (**Ubiquitous Language**)
bzw. ein gemeinsames Verständnis entwickelt werden, die bei der Implementierung im Team verwendet wird, um Missverständnisse zu vermeiden. Zudem wurden die verschiedenen „**Bounded Contexts**“ innerhalb der Domäne/des Modells identifiziert, sowie die Grenzen und Schnittstellen zwischen Ihnen definiert.

**2. Architektur**

a) Schichtenarchitektur
- **Domain Layer**: Enthält Entitäten, Value Objects, Aggregate und Domain Services.
- **Application Layer** beinhaltet Use Cases, die die Geschäftslogik orchestrieren.
- **Infrastructure Layer**: Umfasst technische Implementierungen wie Datenzugriffe und externe Schnittstellen.
- **Presentation Layer**: Stellt die Benutzeroberfläche bereit.
b) Modularisierung
- Organisation des Codes in Modulen, die klar definierte Verantwortlichkeiten haben.
- Namenskonventionen und Ordnerstrukturen zur besseren Übersichtlichkeit.

**3. Implementierung des Domänenmodells**

**Entitäten** haben eine eindeutige Identität, und **Value Objects** sind unveränderlich und beschreiben Attribute. **Aggregate** mit einer **Wurzelentität** müssen definiert werden, und es wird sichergestellt, dass alle Änderungen über die Wurzel erfolgen.

**4. Testbarkeit**

Über die Unit Tests wird die **Domänenlogik** sichergestellt, und über die Integrationstests überprüft, ob die Interaktion zwischen Modulen und Schichten korrekt funktionieren.

**5. Modularität und Flexibilität**

Durch die Implementierung von **Dependency Injection**, können die Abhängigkeiten verwaltet und die Testbarkeit erhöht werden.
Durch die Verwendung von **Event Sourcing und CQRS** kann zusätzliche Modularität erreicht werden-

**6. Beispiel eines Domain Models**

Nebenan ist ein Beispiel des Domain Models zum E-Vote System

**7. Ausblick**

Im nächsten Schritt wird mit der Implementierung der grundlegenden Entitäten und Value Objects begonnen. Zudem werden die ersten Unit Tests parallel zur Domainimplementierung durchgeführt.



### Beispiel: Domain Model in Python

```bash

from datetime import datetime
from typing import List


class Bürger:
 def __init__(self, bürger_id: str, name: str, email: str, authentifizierungsstatus: bool, stimmberechtigung: bool):
        self.bürger_id = bürger_id
        self.name = name
        self.email = email
        self.authentifizierungsstatus = authentifizierungsstatus
        self.stimmberechtigung = stimmberechtigung

    def ist_stimmberechtigt(self) -> bool:
        return self.stimmberechtigung


class Stimme:
    def __init__(self, bürger_id: str, abstimmungs_id: str, wahloption: str):
        self.bürger_id = bürger_id
        self.abstimmungs_id = abstimmungs_id
        self.wahloption = wahloption


class Abstimmung:
    def __init__(self, abstimmungs_id: str, titel: str, beschreibung: str, organisations_id: str, frist: datetime, abstimmungsstatus: bool):
        self.abstimmungs_id = abstimmungs_id
        self.titel = titel
        self.beschreibung = beschreibung
        self.organisations_id = organisations_id
        self.frist = frist
        self.abstimmungsstatus = abstimmungsstatus
        self.verfügbare_optionen: List[str] = []

    def add_option(self, option: str):
        self.verfügbare_optionen.append(option)

    def ist_aktiv(self) -> bool:
        return self.abstimmungsstatus and datetime.now() <= self.frist


class Organisation:
    def __init__(self, organisations_id: str, name: str, kontakt: str, authentifizierungsstatus: bool):
        self.organisations_id = organisations_id
        self.name = name
        self.kontakt = kontakt
        self.authentifizierungsstatus = authentifizierungsstatus


# Beispiel für die Nutzung des Domain Models
if __name__ == "__main__":
    # Erstellen von Bürgern
    bürger1 = Bürger(bürger_id="B1", name="Max Mustermann", email="max@example.com", authentifizierungsstatus=True, stimmberechtigung=True)
    bürger2 = Bürger(bürger_id="B2", name="Erika Mustermann", email="erika@example.com", authentifizierungsstatus=True, stimmberechtigung=False)

    # Erstellen einer Organisation
    organisation = Organisation(organisations_id="O1", name="Wahlorganisation", kontakt="kontakt@organisation.com", authentifizierungsstatus=True)

    # Erstellen einer Abstimmung
    abstimmung = Abstimmung(
        abstimmungs_id="A1",
        titel="Wahl 2024",
        beschreibung="Wählen Sie Ihren bevorzugten Kandidaten.",
        organisations_id=organisation.organisations_id,
        frist=datetime(2024, 12, 31),
        abstimmungsstatus=True,
    )

    # Optionen zur Abstimmung hinzufügen
    abstimmung.add_option("Kandidat A")
    abstimmung.add_option("Kandidat B")

    # Stimmen abgeben
    if bürger1.ist_stimmberechtigt():
        stimme1 = Stimme(bürger_id=bürger1.bürger_id, abstimmungs_id=abstimmung.abstimmungs_id, wahloption="Kandidat A")
        print(f"{bürger1.name} hat für {stimme1.wahloption} gestimmt.")
    else:
        print(f"{bürger1.name} ist nicht stimmberechtigt.")

    if bürger2.ist_stimmberechtigt():
        stimme2 = Stimme(bürger_id=bürger2.bürger_id, abstimmungs_id=abstimmung.abstimmungs_id, wahloption="Kandidat B")
        print(f"{bürger2.name} hat für {stimme2.wahloption} gestimmt.")
    else:
        print(f"{bürger2.name} ist nicht stimmberechtigt.")

```


---

## Dokumentation der Zusammenarbeit (Übung 3)

- Event Storming *- bearbeitet von allen Gruppenmitgliedern*
- Domänenmodell *- bearbeitet von Josefine Theden-Schow*
- Bounded Contexts und Entitäten und Aggregate *- bearbeitet von Niklas Wehl*
- Domain Services und Repositories *- bearbeitet von Vera Kammerer*
- Strategie zur Implementierung des DDD-Modells in Code *- bearbeitet von Jan Eberlein*

---

---









