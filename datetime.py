import datetime

def aktuelles_datum_und_Uhrzeit():
    print("Aktuelles Datum und Uhrzeit:",datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

def tage_bis_jahresende():
    differenz = datetime.date(datetime.date.today().year, 12, 31) - datetime.datetime.now()
    print("Tage bis zum Jahresende:", differenz.days)

def berechne_differenz(ziel_datum=None):
    while True:
        try:
            if not ziel_datum:
                datum_input = input("Gib ein Datum ein (TT.MM.JJJJ): ")
            else:
                datum_input = ziel_datum
            tag, monat, jahr = map(int, datum_input.split("."))
            benutzer_datum = datetime.date(jahr, monat, tag)
            differenz = benutzer_datum - datetime.date.today()
            print(f"Tage bis zum angegebenen Datum: {differenz.days}")
            return benutzer_datum
        except ValueError:
            print("Ungültiges Datum (TT.MM.JJJJ bitte)")

def wochentag_berechnen():
    datum = berechne_differenz()
    print(f"Der eingegebene Wochentag ist {datum.strftime('%A')}")

def zeit_in_zukunft():
    while True:
        try:
            zeit_input = input("Gib eine Zeitspanne ein (Minuten, Stunden, Tage): ")
            zeit, einheit = zeit_input.split()
            zeit = int(zeit)
            delta = {"minuten": datetime.timedelta(minutes=zeit), "stunden": datetime.timedelta(hours=zeit), "tage": datetime.timedelta(days=zeit)}
            if einheit.lower() in delta:
                zukunft = datetime.date.today() + delta[einheit.lower()]
                print(f"In {zeit} {einheit} wird der {zukunft.strftime('%d.%m.%Y %H:%M:%S')}")
                break
            else:
                print("Ungültiges Eingabe (Minuten, Stunden oder Tage bitte).")

        except ValueError:
            print("Ungültiges Eingabe (Minuten, Stunden oder Tage bitte).")

def main():

    aktuelles_datum_und_Uhrzeit()
    tage_bis_jahresende()
    berechne_differenz ()
    wochentag_berechnen()
    zeit_in_zukunft()

if __name__ == "__main__":
    main()