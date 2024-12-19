import datetime

def aktuelles_datum_und_Uhrzeit():
    jetzt = datetime.datetime.now()
    print("Aktuelles Datum und Uhrzeit:", jetzt.strftime("%d.%m.%Y %H:%M:%S"))

def tage_bis_jahresende():
    heute = datetime.date.today()
    jahresende = datetime.date(heute.year, 12, 31)
    differenz = jahresende - heute
    print("Tage bis zum Jahresende:", differenz.days)

def tage_bis_datum():
    while True:
        try:
            datum_input = input("Gib ein Datum ein (TT.MM.JJJJ): ")
            tag, monat, jahr = map(int, datum_input.split("."))
            benutzer_datum = datetime.date(jahr, monat, tag)
            heute = datetime.date.today()
            differenz = benutzer_datum - heute
            print(f"Tage bis zum angegebenen Datum: {differenz.days}")
            break
        except ValueError:
            print("Ungültiges Datum")

def wochentag_berechnen():
    while True:
        try:
            datum_input = input("Gib ein Datum ein (TT.MM.JJJJ): ")
            tag, monat, jahr = map(int, datum_input.split("."))
            benutzer_datum = datetime.date(jahr, monat, tag)
            wochentag = benutzer_datum.strftime("%A")
            break
        except ValueError:
            print("Ungültiges Datum")

def zeit_in_zukunft():
    while True:
        try:
            zeit_input = input("Gib eine Zeitspanne ein (Minuten, Stunden, Tage): ")
            zeit, einheit = zeit_input.split()
            zeit = int(zeit)
            if einheit.lower() == "minuten":
                zukunft = datetime.datetime.now() + datetime.timedelta(minutes=zeit)
            elif einheit.lower() == "stunden":
                zukunft = datetime.datetime.now() + datetime.timedelta(hours=zeit)
            elif einheit.lower() == "tage":
                zukunft = datetime.datetime.now() + datetime.timedelta(days=zeit)
            else:
                print("Ungültige Einheit (Minuten, Stunden oder Tage bitte).")
                continue
            print(f"In {zeit} {einheit} wird der {zukunft.strftime('%d.%m.%Y %H:%M:%S')}")
            break
        except ValueError:
            print("Ungültiges Eingabe")

def main():

    aktuelles_datum_und_Uhrzeit()

    tage_bis_jahresende()

    wochentag_berechnen()

    zeit_in_zukunft()

if __name__ == "__main__":
    main()