# modsoft
modul moderne softwareentwicklung

# **Was ist Git und warum sollte es verwendet werden?**

1. Während andere Versionskontrollsystemen nur die Unterschiede in den Änderungen speichern, erstellt  Git häufig "Snapshots" der Dateien. Das bringt viele Vorteile, besonders jedoch hinsichtlich des Branchings.
   
2. Außerdem legt Git großen Wert auf die Sicherheit und Integrität der Daten. Jeder Commit erhält einen eindeutigen SHA-1-Hashwert, der sicherstellt, dass nachträgliche Änderungen oder Vertuschungen nicht möglich sind. Dies ermöglicht auch die Wiederherstellung von früheren Versionen.
   
3. Der Großteil der Arbeit mit Git erfolgt zudem lokal, was nützlich ist, wenn man unterwegs ist oder temporär keinen Internetzugang hat.

4. Git besitzt eine gewisse "Zeitmaschinen-Funktionalität" es ist möglich, mutige Änderungen zu testen und problemlos anzunehmen oder zu verwerfen. Git fördert somit eine dynamische und risikofreudige Arbeitsweise.
   
5. Des Weiteren fördert Git Branching, also das Erstellen von Verzweigungen (Branches), was eine flexible und parallele Entwicklung ermöglicht.
   
6. Git-Repositories können eine hierarchische Struktur bilden, bei der viele Klone für die Entwicklung verwendet werden und ein Master-Repository alle Änderungen sammelt.
   
 ![image](https://github.com/user-attachments/assets/00fb8d05-65da-49ac-b6d3-508fa29a7eb5)


# Git mit PyCharm benutzen - Local Repository und Remote Repository
 
Versionsverwaltungs-Tools wie Git lassen sich optimal in integrierte Entwicklungsumgebungen (IDEs) wie PyCharm einbinden. Dies erleichtert den Umgang mit Git für Entwickler deutlich. Git ermöglicht es, Änderungen an einem Projekt nachvollziehbar zu machen und PyCharm bietet eine Integration, um Git-Befehle direkt in der IDE auszuführen.
Um diese Konstellation zu nutzen, müssen sowohl Git als auch PyCharm auf dem Computer installiert sein. PyCharm bietet bereits eine direkte Integration von Git ohne zusätzliche Plugins.

<img align="right" width="200px" hspace="15" vspace="15" src="Git_Menue.png" alt="image" />

#### Git in PyCharm nutzen
PyCharm bietet zwei Hauptmöglichkeiten, um Git-Befehle auszuführen:
1. Über das Terminal: Git-Befehle können wie gewohnt direkt im Terminal eingegeben werden.
2. Über die GUI (Menüpunkte): PyCharm stellt über das Menü eine benutzerfreundliche Oberfläche bereit, um die wichtigsten Git-Befehle auszuführen.

#### Projekte mit Git-Repositories verknüpfen
Beim Anlegen eines neuen Projekts in PyCharm besteht die Möglichkeit, Git-Repositories mit kollaborativen Versionsverwaltungen wie GitHub zu verknüpfen. Dies erlaubt das Klonen eines bestehenden Remote-Repositories auf ein lokales Repository. Dazu muss die URL des Repositories in PyCharm angegeben werden. Dabei kann der Speicherort des lokalen Repositories individuell festgelegt werden.

#### Grundlegende Git-Operationen in PyCharm
Sobald die Versionskontrolle verknüpft ist (der Remote-Zugriff wird automatisch generiert), können grundlegende Operationen wie das Committen, Pullen oder Pushen von Änderungen über den Menüpunkt „Git “ ausgeführt werden:
- Änderungen hinzufügen und committen: Dateien können ausgewählt, gestaged und mit einer Commit-Nachricht versehen werden.  Mit Git > Commit (Strg + K) wird dieser Prozess angestoßen.
- Pushen von Änderungen: Commits können mit Git > Push (Strg + Shift + K) direkt an das verknüpfte Remote-Repository gesendet werden.
- Pullen von Änderungen: Um die neuesten Änderungen aus einem Remote-Repository zu beziehen, bietet PyCharm den Befehl Git > Pull.

Mit PyCharm können Tools wie das Anzeigen von Diff-Dateien (um Unterschiede zwischen verschiedenen Versionen eines Projekts darzustellen) genutzt werden, sowie die Möglichkeit, Branches zu erstellen und zu verwalten.

Weitere Informationen zu diesem Thema: https://www.jetbrains.com/help/pycharm/set-up-a-git-repository.html
