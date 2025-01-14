def citeste_filme(fisier):
    """Citește filmele din fișier și le returnează ca un dicționar."""
    filme = {}
    try:
        with open(fisier, "r") as f:
            for linie in f:
                titlu, evaluare = linie.strip().split(", ")
                filme[titlu] = int(evaluare)
    except FileNotFoundError:
        print(f"Fișierul {fisier} nu a fost găsit. Va fi creat unul nou.")
    return filme


def scrie_filme(fisier, filme):
    """Scrie filmele și evaluările lor în fișier."""
    with open(fisier, "w") as f:
        for titlu, evaluare in filme.items():
            f.write(f"{titlu}, {evaluare}\n")


def afiseaza_filme(filme):
    """Afișează filmele sortate după evaluare."""
    filme_sortate = sorted(filme.items(), key=lambda x: x[1], reverse=True)
    print("\nLista filmelor și evaluările acestora:")
    for titlu, evaluare in filme_sortate:
        print(f"{titlu}: {evaluare}")


def adauga_film(filme):
    """Adaugă un nou film cu evaluare în dicționar."""
    titlu = input("Introdu titlul filmului: ").strip()
    if titlu in filme:
        print("Filmul există deja. Poți actualiza evaluarea acestuia.")
        return
    while True:
        try:
            evaluare = int(input("Introdu evaluarea filmului (1-5): "))
            if 1 <= evaluare <= 5:
                break
            else:
                print("Te rog să introduci o evaluare între 1 și 5.")
        except ValueError:
            print("Te rog să introduci un număr valid.")
    filme[titlu] = evaluare


def actualizeaza_evaluare(filme):
    """Actualizează evaluarea unui film existent."""
    titlu = input("Introdu titlul filmului de actualizat: ").strip()
    if titlu not in filme:
        print("Filmul nu există în listă.")
        return
    while True:
        try:
            evaluare = int(input("Introdu noua evaluare (1-5): "))
            if 1 <= evaluare <= 5:
                break
            else:
                print("Te rog să introduci o evaluare între 1 și 5.")
        except ValueError:
            print("Te rog să introduci un număr valid.")
    filme[titlu] = evaluare


def sterge_film(filme):
    """Șterge un film din dicționar."""
    titlu = input("Introdu titlul filmului de șters: ").strip()
    if titlu in filme:
        del filme[titlu]
        print(f"Filmul '{titlu}' a fost șters.")
    else:
        print("Filmul nu există în listă.")


# Program principal
fisier = "movies.txt"
filme = citeste_filme(fisier)

while True:
    print("\nMeniu:")
    print("1. Vizualizează toate filmele")
    print("2. Adaugă un nou film")
    print("3. Actualizează evaluarea unui film")
    print("4. Șterge un film")
    print("5. Salvează și ieși")

    optiune = input("Alege o opțiune (1-5): ").strip()
    if optiune == "1":
        afiseaza_filme(filme)
    elif optiune == "2":
        adauga_film(filme)
    elif optiune == "3":
        actualizeaza_evaluare(filme)
    elif optiune == "4":
        sterge_film(filme)
    elif optiune == "5":
        scrie_filme(fisier, filme)
        print("Modificările au fost salvate. La revedere!")
        break
    else:
        print("Opțiune invalidă. Te rog să încerci din nou.")
