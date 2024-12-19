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
            else:
                datum_input = ziel_datum
            tag, monat, jahr = map(int, datum_input.split("."))     # Splitten der Eingabe (TT.MM.JJJJ) in Tag, Monat, Jahr und Umwandlung in Integer
            benutzer_datum = datetime.date(jahr, monat, tag)
            differenz = benutzer_datum - datetime.date.today()
            print(f"Tage bis zum angegebenen Datum: {differenz.days}")
            return benutzer_datum
        except ValueError:                                          # Wenn die Eingabe ungültig ist (z.B. falsches Format), wird dies abgefangen
            print("Ungültiges Datum (TT.MM.JJJJ bitte)")

# Berechnet den Wochentag für das eingegebene Datum.
def wochentag_berechnen():
    datum = berechne_differenz()
    print(f"Der eingegebene Wochentag ist {datum.strftime('%A')}")

# Berechnet das zukünftige Datum basierend auf der angegebenen Zeitspanne.
def zeit_in_zukunft():
    while True:     
        try:
            zeit_input = input("Gib eine Zeitspanne ein (Minuten, Stunden, Tage): ")
            zeit, einheit = zeit_input.split()
            zeit = int(zeit)

            delta = {                                                # Definition des Zeitdeltas für Minuten, Stunden und Tage als datetime.timedelta-Objekte
                "minuten": datetime.timedelta(minutes=zeit),
                "stunden": datetime.timedelta(hours=zeit),
                "tage": datetime.timedelta(days=zeit)
            }

            einheit = einheit.lower()
            if  einheit in delta:
                zukunft = datetime.datetime.now() + delta[einheit]
                print(f"In {zeit} {einheit} wird es {zukunft.strftime('%d.%m.%Y %H:%M:%S')}")
                break
            else:
                print("Ungültige Zeiteinheit. Verwende 'Minuten', 'Stunden' oder 'Tage'.")

        except ValueError:
            print("Ungültige Eingabe. Gib bitte eine gültige Zahl gefolgt von einer Zeiteinheit ein.")

# Hauptfunktion, die alle anderen Funktionen aufruft.
def main():

    aktuelles_datum_und_Uhrzeit()
    tage_bis_jahresende()
    berechne_differenz ()
    wochentag_berechnen()
    zeit_in_zukunft()

if __name__ == "__main__":
    main()