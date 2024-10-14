# modsoft
modul moderne softwareentwicklung

# Was sind Branches?
Ein Branch (Zweig) in Git ist eine unabhängige Entwicklungsumgebung, die es ermöglicht, gleichzeitig an verschiedenen Features, Bugfixes oder Experimenten zu arbeiten, ohne die Hauptarbeit auf dem main-Branch zu beeinträchtigen.

- Der main-Branch ist standardmäßig der Hauptzweig, in den normalerweise der fertige Code gemerged wird.
- Entwickler erstellen für jede Aufgabe einen neuen Branch, um dort isoliert zu arbeiten. Zum Beispiel:

``` git checkout -b feature/neues-feature ``

# Warum Branches nutzen?
- Isolierte Entwicklung: Änderungen in einem Branch wirken sich nicht auf den Hauptcode aus, bis sie gemerged werden.
- Paralleles Arbeiten: Mehrere Teammitglieder können gleichzeitig an unterschiedlichen Teilen eines Projekts arbeiten.
- Rückverfolgbarkeit: Änderungen sind einfacher nachvollziehbar, da jeder Branch eine spezifische Aufgabe repräsentiert.

# Branching-Strategien
- Feature Branches: Für jedes neue Feature oder jede neue Aufgabe wird ein eigener Branch erstellt und nach Fertigstellung in den Hauptbranch gemerged.
- Release Branches: Diese Branches dienen zur Vorbereitung einer neuen Version und sind von main abgezweigt, um letzte Anpassungen vorzunehmen.
- Hotfix Branches: Dienen zur schnellen Behebung von Fehlern im Produktionscode.

# Merge-Konflikte
Ein Merge-Konflikt tritt auf, wenn zwei Branches Änderungen an denselben Zeilen in einer Datei vorgenommen haben und Git nicht automatisch entscheiden kann, welche Änderung übernommen werden soll.

- Wie entstehen Merge-Konflikte? Ein häufiger Fall ist, wenn zwei Entwickler gleichzeitig an derselben Datei arbeiten und diese dann in den main-Branch zusammengeführt werden sollen.
- Lösen von Merge-Konflikten:
  1. Git teilt mit, in welchen Dateien ein Konflikt besteht, wenn der merge- oder pull-Befehl ausgeführt wird.
  2. Öffne die betroffenen Dateien. Git markiert die konfliktverursachenden Zeilen mit:
  <<<<<<< HEAD
// Dein aktueller Branch
=======
// Änderungen aus dem Branch, den du mergen möchtest
>>>>>>> branchname
3. Entscheide, welche Version der Änderungen übernommen werden soll (oder kombiniere beide).
4. Entferne die Konfliktmarkierungen und committe die Änderungen:
git add DateiName
git commit -m "Löse Merge-Konflikte"

# Branching in Zusammenarbeit mit anderen Tools
Wenn du mit einem Tool wie GitHub oder GitLab arbeitest, kannst du Pull Requests (PR) oder Merge Requests (MR) erstellen, um Branches zu reviewen und zu mergen.

Möchtest du eine Beispielgrafik zu Branches oder Merge-Konflikten einfügen, um das Handout visuell aufzuwerten? Das könnte die Inhalte verständlicher machen.
