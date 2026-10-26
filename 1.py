liczba_punktów=int(input("Podaj liczbę punktów:"))

if liczba_punktów >= 80:
    print("Zaliczyłeś egzamin w terminie 0")
elif liczba_punktów < 80 and liczba_punktów > 50:
    print("Możesz poprawić swój wynik")
else:
    print("Musisz poprawić swój wynik")