**Abgabe**: Text ()

## Aufgabe 1: Einfache Entscheidungen mit `if`-Statements (25 Punkte)

**Ziel:** Verstehen, wie Entscheidungen im Code in Arbeitsschritte übersetzt werden können.

Code-Beispiel:

```python
zahl = int(input("Gib eine Zahl ein: "))
if zahl > 10:
    print("Die Zahl ist größer als 10.")
else:
    print("Die Zahl ist 10 oder kleiner.")
```

- Schreibe die Arbeitsschritte auf.

    - Variable zahl definieren
    - Eingabe durch input() erfassen
    - mit int() in eine Ganzzahl umgewandeln
    - Bedingung prüfen:
        - Ja: Die Zahl ist größer als 10. wird ausgegeben
        - Nein: Die Zahl ist 10 oder kleiner. wird ausgegeben

---

## Aufgabe 2: Listen verstehen und mit Python erstellen (20 Punkte)

**Ziel:** Verstehen, wie Datenstrukturen wie Listen verwendet werden können.

Code-Beispiel:

```python
zahlen = [1, 2, 3, 4, 5]
print("Die erste Zahl ist:", zahlen[0])
print("Die letzte Zahl ist:", zahlen[-1])
```

- Schreibe die Arbeitsschritte auf.

    - Liste mit den Werten 1, 2, 3, 4, 5 erstellen
    - diese Liste zahl (Variable) zuweisen
    - Zugriff auf das erste Element: zahlen[0] gibt den Wert 1 zurück
        - Ausgabe: Die erste Zahl ist: 1
    - Zugriff auf das letzte Element: zahlen[-1] gibt den Wert 5 zurück
        - Ausgabe: Die letzte Zahl ist: 5

**Zusatzaufgabe:** Erstelle selbst eine Liste mit Wochentagen und schreibe die Arbeitsschritte auf.

```python
wochentage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
print(wochentage[0])
print(wochentage[-1])
```
- Liste mit den Werten Montag, Dienstag, Mittwoch, Donnerstag, Freitag, Samstag, Sonntag erstellen
- diese Liste wochentage (Variable) zuweisen
- Zugriff auf das erste Element: wochentage[0]
    - Ausgabe: Montag
- Zugriff auf das letzte Element: wochentage[-1]
     - Ausgabe: Sonntag

---

## Aufgabe 3: Entscheidungslogik erweitern (25 Punkte)

**Ziel:** Die Funktionsweise von mehreren Bedingungen in Python verstehen und in Arbeitsschritte übertragen.

Code-Beispiel:

```python
zahl = int(input("Gib eine Zahl ein: "))
if zahl > 0:
    print("Die Zahl ist positiv.")
elif zahl < 0:
    print("Die Zahl ist negativ.")
else:
    print("Die Zahl ist null.")
```

- Schreibe die Arbeitsschritte auf.

    - Variable zahl definieren
    - Eingabe durch input() erfassen
    - mit int() in eine Ganzzahl umgewandeln
    - Bedingung prüfen:
        - True: Die Zahl ist positiv. wird ausgegeben
        - False: Die Zahl ist negativ. wird ausgegeben
        - zahl = 0: Die Zahl ist null. wird ausgegeben

---

## Aufgabe 4: Funktionen verstehen (20 Punkte)

**Ziel:** Lernen, wie Funktionen in Python definiert werden und was in jedem Arbeitsschritt passiert.

Code-Beispiel:

```python
def ist_gerade(zahl):
    if zahl % 2 == 0:
        return True
    else:
        return False

zahl = int(input("Gib eine Zahl ein: "))
if ist_gerade(zahl):
    print("Die Zahl ist gerade.")
else:
    print("Die Zahl ist ungerade.")
```

- Schreibe die Arbeitsschritte auf.

    - Funktion ist_gerade definieren, mit Parameter zahl
        - Bedingung prüfen:
            - zahl % 2 == 0
    - Eingabe durch input() erfassen
    - mit int() in eine Ganzzahl umgewandeln
    - Bedingung prüfen:
        - True: Die Zahl ist gerade. wird ausgegeben
        - False: Die Zahl ist ungerade. wird ausgegeben

---

## Aufgabe 5: Benutzerinteraktion (10 Punkte)

**Ziel:** Die Struktur eines Programms mit Benutzereingaben und Ausgaben analysieren.

Code-Beispiel:

```python
name = input("Wie heißt du? ")
alter = int(input("Wie alt bist du? "))
print(f"Hallo {name}, in 10 Jahren wirst du {alter + 10} Jahre alt sein!")
```

- Schreibe die Arbeitsschritte auf.

    - Eingabe durch input() erfassen
    - mit int() in eine Ganzzahl umgewandeln
    - Alter in 10 Jahren berechen:
        - alter + 10
    - mit f-String formatierte Nachricht ausgeben
    
---