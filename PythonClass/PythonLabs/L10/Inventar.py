inventar = {}


def adauga_produs(nume, cantitate):
    """
    Adaugă un produs nou în inventar sau actualizează cantitatea dacă produsul există deja.

    :param nume: Numele produsului (string).
    :param cantitate: Cantitatea produsului (int).
    """
    if nume in inventar:
        inventar[nume] += cantitate
    else:
        inventar[nume] = cantitate
    print(f"Produsul '{nume}' a fost adăugat/actualizat cu succes. Cantitate totală: {inventar[nume]}")


def cauta_produs(nume):
    """
    Caută un produs în inventar și returnează cantitatea.

    :param nume: Numele produsului (string).
    :return: Cantitatea produsului sau mesaj de eroare dacă nu există.
    """
    if nume in inventar:
        print(f"Produsul '{nume}' are o cantitate de: {inventar[nume]}")
    else:
        print(f"Eroare: Produsul '{nume}' nu există în inventar.")


def actualizeaza_cantitatea(nume, cantitate):
    """
    Actualizează cantitatea unui produs existent în inventar.

    :param nume: Numele produsului (string).
    :param cantitate: Noua cantitate a produsului (int).
    """
    if nume in inventar:
        inventar[nume] = cantitate
        print(f"Cantitatea produsului '{nume}' a fost actualizată la: {cantitate}")
    else:
        print(f"Eroare: Produsul '{nume}' nu există în inventar.")


def meniu():
    """
    Afișează meniul principal și gestionează interacțiunea cu utilizatorul.
    """
    while True:
        print("\nMeniu Inventar:")
        print("1. Adaugă produs")
        print("2. Caută produs")
        print("3. Actualizează cantitatea unui produs")
        print("4. Afișează toate produsele")
        print("5. Ieșire")

        try:
            optiune = int(input("Alege o opțiune (1-5): "))

            if optiune == 1:
                try:
                    nume = input("Introdu numele produsului: ").strip()
                    cantitate = int(input("Introdu cantitatea: "))
                    if cantitate < 0:
                        raise ValueError("Cantitatea nu poate fi negativă!")
                    adauga_produs(nume, cantitate)
                except ValueError as e:
                    print(f"Eroare: {e}")

            elif optiune == 2:
                nume = input("Introdu numele produsului pe care dorești să-l cauți: ").strip()
                cauta_produs(nume)

            elif optiune == 3:
                try:
                    nume = input("Introdu numele produsului: ").strip()
                    cantitate = int(input("Introdu noua cantitate: "))
                    if cantitate < 0:
                        raise ValueError("Cantitatea nu poate fi negativă!")
                    actualizeaza_cantitatea(nume, cantitate)
                except ValueError as e:
                    print(f"Eroare: {e}")

            elif optiune == 4:
                print("\nInventar curent:")
                if inventar:
                    for produs, cantitate in inventar.items():
                        print(f"- {produs}: {cantitate}")
                else:
                    print("Inventarul este gol.")

            elif optiune == 5:
                print("Ieșire din program. La revedere!")
                break

            else:
                print("Eroare: Opțiunea introdusă nu este validă. Alege o opțiune între 1 și 5.")

        except ValueError:
            print("Eroare: Te rugăm să introduci un număr valid pentru opțiune.")


# Pornirea programului
meniu()
