import math #biblioteca pentru a putea folosi functia sqrt

while True:
    try:
        print("\nVom calcula distanta dintre doua puncte (x1,y1), (x2, y2) :)")
        x1=float(input("Introdu coordonata x1: "))
        y1=float(input("Introdu coordonata y1:"))
        x2=float(input("Introdu coordonata x2:"))
        y2=float(input("Introdu coordonata y2:"))
        distanta = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        print(f"Distanța dintre punctele ({x1}, {y1}) și ({x2}, {y2}) este {distanta:.2f}")

    except ValueError:
        print("Te rog sa introduci doar numere, nu alte caractere sau litere.")


#.2f folosit pentru ca distanta sa fie afisata cu doua zecimale