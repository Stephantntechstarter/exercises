def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

choice = input("Möchtest du Celsius in Fahrenheit oder Fahrenheit in Celsius umrechnen? (Gib 'Celsius' oder 'Fahreinheit' ein):")

if choice == "Celsius":
    celsius = float(input("Wie viel Grad Celsius möchtest du umrechnen?"))
    fahrenheit = celsius_to_fahrenheit(c)
    print(f"{celsius} Grad Celsius sind {fahrenheit:.2f} Grad Fahreinheit.")

elif choice == "Fahrenheit":
    fahreinheit = float(input("Wie viel Grad Fahrenheit möchtest du umrechnen?"))
    celsius = fahrenheit_to_celsius(f)
    print(f"{fahrenheit} Grad Fahreinheit sind {celsius:.2f} Grad Celsius.")
    
else:
    print("Ungültige Eingabe. Bitte Celsius oder Fahreinheit eingeben.")