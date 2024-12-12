def este_prim(numar):    #def se foloseste pentru a defini o functie
    if numar<=1:
        return False     #nr mai mici sau egale decat 1 nu sunt prime
    if numar ==2:
        return True      # 2 este numar prim
    if numar %2==0:
        return False     #numerele pare mai mari decat 2 nu sunt prime

    for i in range(3, int(numar ** 0.5) + 1, 2):
        if numar % i == 0:
            return False  # Dacă găsim un divizor, numărul nu este prim
    return True  # Dacă nu găsim divizori, numărul este prim

numar = int(input("Introdu un număr: "))
if este_prim(numar):
    print(f"{numar} este un număr prim.")
else:
    print(f"{numar} nu este un număr prim.")

#Folosim input() pentru a citi date de la utilizator (ca text) și
# int() pentru a le converti în numere întregi, astfel încât să putem face calcule cu ele.