while True:
    try:
        numar=int(input("\nAlege un numar pentru care vrei sa generezi tabela de inmultire: "))
        limita=int(input("Alege pana la ce numar sa fie generata tabla: "))
        print(f"Tabelul de inmultire pentru {numar} este: ")
        for i in range (1, limita+1):
            print(f"{numar} x {i}= {numar*i}")

    except ValueError:
        print("Te rog sa introduci doar numere valide")
