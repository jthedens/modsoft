# modsoft
modul moderne softwareentwicklung

Was sind Branches?
Ein Branch (Zweig) in Git ist eine unabhängige Entwicklungsumgebung, die es ermöglicht, gleichzeitig an verschiedenen Features, Bugfixes oder Experimenten zu arbeiten, ohne die Hauptarbeit auf dem main-Branch zu beeinträchtigen.

Der main-Branch ist standardmäßig der Hauptzweig, in den normalerweise der fertige Code gemerged wird.
Entwickler erstellen für jede Aufgabe einen neuen Branch, um dort isoliert zu arbeiten. Zum Beispiel:
bash
Code kopieren
git checkout -b feature/neues-feature
2. Warum Branches nutzen?
Isolierte Entwicklung: Änderungen in einem Branch wirken sich nicht auf den Hauptcode aus, bis sie gemerged werden.
Paralleles Arbeiten: Mehrere Teammitglieder können gleichzeitig an unterschiedlichen Teilen eines Projekts arbeiten.
Rückverfolgbarkeit: Änderungen sind einfacher nachvollziehbar, da jeder Branch eine spezifische Aufgabe repräsentiert.
