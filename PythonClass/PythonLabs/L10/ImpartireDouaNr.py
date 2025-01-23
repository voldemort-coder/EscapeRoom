def imparte_numerele(a,b):
    try:
        rezultat=a/b
        return rezultat
    except ZeroDivisionError:
        return None

while True:
    try:
        numar1=float(input("Introdu primul numar:"))
        numar2=float(input("Introdu al doilea numar:"))

        rezultat=imparte_numerele(numar1, numar2)
        if rezultat is not None:
            print(f"Rezultatul este: {rezultat}")
            break  # Ieșim din buclă după o împărțire reușită
        else:
            print("Eroare: Împărțirea la zero nu este permisă! Încearcă din nou.")
    except ValueError:
        print("Eroare: Introdu doar numere valide!")
