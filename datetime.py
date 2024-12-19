import datetime

# Gibt das aktuelle Datum und die Uhrzeit aus.
def aktuelles_datum_und_Uhrzeit():
    print("Aktuelles Datum und Uhrzeit:",datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

# Berechnet die verbleibenden Tage bis zum Jahresende und gibt diese aus.
def tage_bis_jahresende():
    differenz = datetime.date(datetime.date.today().year, 12, 31) - datetime.date.today()
    print("Tage bis zum Jahresende:", differenz.days)

# Berechnet die Differenz zwischen dem heutigen Datum und einem benutzerdefinierten Datum.
def berechne_differenz(ziel_datum=None):
    while True:                                                     # Schleife, die solange fortgesetzt wird, bis der Benutzer ein gültiges Datum eingibt
        try:
            if ziel_datum is None:                                  # Wenn kein Datum übergeben wurde, wird der Benutzer nach einem Datum gefragt
                datum_input = input("Gib ein Datum ein (TT.MM.JJJJ): ")
                if not datum_input.strip():                         # Prüfung, ob der Benutzer nichts eingibt
                    print("Das Datum darf nicht leer sein.")
                    continue                                        # Fortfahren zur nächsten Iteration der Schleife, sodass der Benutzer erneut nach dem Datum gefragt wird

            else:
                datum_input = ziel_datum
            tag, monat, jahr = map(int, datum_input.split("."))     # Splitten der Eingabe (TT.MM.JJJJ) in Tag, Monat, Jahr und Umwandlung in Integer
            benutzer_datum = datetime.date(jahr, monat, tag)        # Erstellen eines Datumsobjekts mit den eingegebenen Werten
            differenz = benutzer_datum - datetime.date.today()
            print(f"Tage bis zum angegebenen Datum: {differenz.days}")
            return benutzer_datum
        except ValueError:                                          # Wenn die Eingabe ungültig ist (z.B. falsches Format), wird dies abgefangen
            print("Ungültiges Datum. Bitte im Format TT.MM.JJJJ eingeben.")

# Berechnet den Wochentag für das eingegebene Datum.
def wochentag_berechnen():
    datum = berechne_differenz()                                    # Berechnet das benutzerdefinierte Datum und gibt es zurück
    print(f"Der eingegebene Wochentag ist {datum.strftime('%A')}")

# Berechnet das zukünftige Datum basierend auf der angegebenen Zeitspanne.
def zeit_in_zukunft():
    while True:                                                     # Endlos-Schleife, um den Benutzer so lange nach einer korrekten Eingabe zu fragen
        try:     
            zeit_input = input("Gib eine Zeitspanne ein (Minuten, Stunden, Tage): ")
            if not zeit_input.strip():                              # Prüfung, ob die Eingabe leer oder nur aus Leerzeichen besteht
                print("Das Datum darf nicht leer sein.")
                continue                                            # Fortfahren zur nächsten Iteration der Schleife, sodass der Benutzer erneut nach dem Datum gefragt wird

            zeit, einheit = zeit_input.split()                      # Aufteilen der Eingabe in Zeit und Einheit
            zeit = int(zeit)                                        # Umwandeln der Zeit in eine Ganzzahl

            delta = {                                               # Definition des Zeitdeltas für Minuten, Stunden und Tage als datetime.timedelta-Objekte
                "minuten": datetime.timedelta(minutes=zeit),
                "stunden": datetime.timedelta(hours=zeit),
                "tage": datetime.timedelta(days=zeit)
            }

            einheit = einheit.lower()                               # Umwandeln der Einheit in Kleinbuchstaben
            if  einheit in delta:                                   # Wenn die Einheit gültig ist, wird das zukünftige Datum berechnet
                zukunft = datetime.datetime.now() + delta[einheit]
                print(f"In {zeit} {einheit} wird es {zukunft.strftime('%d.%m.%Y %H:%M:%S')}")
                break                                               # Schleife verlassen, da die Eingabe korrekt war
            else:
                print("Ungültige Zeiteinheit. Verwende 'Minuten', 'Stunden' oder 'Tage'.")

        except ValueError:
            print("Ungültige Eingabe. Gib bitte eine gültige Zahl gefolgt von einer Zeiteinheit ein.")

# Hauptfunktion, die alle anderen Funktionen aufruft.
def main():

# Gibt das aktuelle Datum und die Uhrzeit aus
    aktuelles_datum_und_Uhrzeit()

# Berechnet und gibt die verbleibenden Tage bis zum Jahresende aus   
    tage_bis_jahresende()

# Berechnet die Differenz zwischen dem aktuellen Datum und einem benutzerdefinierten Datum  
    berechne_differenz ()

# Berechnet und gibt den Wochentag für das benutzerdefinierte Datum aus 
    wochentag_berechnen()

# Berechnet das zukünftige Datum basierend auf der angegebenen Zeitspanne und gibt es aus    
    zeit_in_zukunft()

# Frage, ob der Benutzer fortfahren möchte
   fortfahren = input("Möchtest du erneut eine Berechnung durchführen? (j/n): ")
        if fortfahren.lower() != 'j':
            break  

if __name__ == "__main__":
    main()