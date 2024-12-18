import random

def play_round():
    choices = ["Schere", "Stein", "Papier"]

user_choice = input("Wähle Schere, Stein oder Papier")

if user_choice not in choices:
    print("Ungültige Eingabe. Bitte wähle Schere, Stein oder Papier.")
    return None, None

computer_choice = random.choice(choices)

print(f"Du hast {user_choice} gewählt.")
print(f"Der Computer hat {computer_choice} gewählt.")

if user_choice == computer_choice:
    return "Unentschieden", computer_choice

elif (user_choice == "Schere" and computer_choice == "Papier") or \
    (user_choice == "Stein" and computer_choice == "Schere") or \
        (user_choice == "Papier" and computer_choice == "Stein"):
        return "Du hast gewonnen!", computer_choice

else:
    return "Du hast verloren!", computer_choice

def main():
    user_wins = 0
    computer_wins = 0
    draws = 0

    while True:
        result, computer_choice = play_round()

        if result is None:
            continue

        if result == "Du hast gewonnen!":
            user_wins += 1

        elif result == "Du hast verloren!":
            computer_wins += 1
        else:
            draws += 1
        
        print(result)
        print(f"Spielstand: Du hast {user_wins} - Computer {computer_wins} - Unentschieden {draws}")

        play_again = input("Möchtest du noch eine Runde spielen? (ja/nein):").lower()
        if play_again != "ja":
            print("Danke fürs Spielen!")
            break

if __name__ == "__main__":
    main()