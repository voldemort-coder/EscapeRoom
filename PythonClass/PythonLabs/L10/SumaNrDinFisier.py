def citeste_si_calculeaza_suma(nume_fisier):
    try:
        with open(nume_fisier, 'r') as fisier:
            suma = 0
            for linie in fisier:
                try:
                    numar = float(linie.strip())  # Convertim fiecare linie în număr
                    suma += numar
                except ValueError:
                    print(f"Eroare: '{linie.strip()}' nu este un număr valid și va fi ignorat.")
            return suma
    except FileNotFoundError:
        print("Eroare: Fișierul nu există.")
        return None
    except IOError:
        print("Eroare: A apărut o problemă la citirea fișierului.")
        return None


while True:
    nume_fisier = input("Introdu numele fișierului (sau calea către fișier): ")

    suma = citeste_si_calculeaza_suma(nume_fisier)
    if suma is not None:  # Dacă fișierul a fost citit cu succes
        print(f"Suma numerelor din fișier este: {suma}")
        break  # Ieșim din buclă dacă procesarea a fost reușită
    else:
        print("Te rugăm să introduci un fișier valid!")
