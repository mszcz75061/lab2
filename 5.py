plik = open("notowania giełdowe.txt", "r")
print(plik.read())
with open("notowania giełdowe.txt", "a") as plik:
    plik.write("ALR, 113\n")
with open('notowania giełdowe.txt', 'r') as plik:
    print(plik.read())




