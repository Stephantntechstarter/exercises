def miles_to_kilometers(miles):
    return miles / 0.621371

def kilometer_to_miles(kilometers):
    return kilometers * 0.621371

choice = input("Möchtest du Meilen in Kilometer oder Kilometer in Meilen umrechnen? (schreibe 'Meilen' oder 'Kilometer'):")

if choice == "Meilen":
    miles = float(input("Wie viele Meilen möchtest du umrechnen?"))
    kilometers = miles_to_kilometers(miles)
    print(f"{miles} Meilen sind {kilometers:.2f} Kilometer.")

elif choice == "Kilometer":
    kilometers = float(input("Wie viele Kilometer möchtest du umrechnen?"))
    miles = kilometer_to_miles(kilometers)
    print(f"{kilometers} Kilometer sind {miles:.2f} Meilen.")
    
else:
    print("Ungültige Eingabe. Bitte Meilen oder Kilometer eingeben.")