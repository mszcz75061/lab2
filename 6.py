znak = input("Wprowadź pojedynczą literę: ")
if len(znak) == 1 and znak.isalpha():
    if znak.isupper():
        print(f"Litera '{znak}' jest duża.")
    elif znak.islower():
        print(f"Litera '{znak}' jest mała.")
else:
    print("Błąd: Musisz wprowadzić dokładnie jedną literę")
