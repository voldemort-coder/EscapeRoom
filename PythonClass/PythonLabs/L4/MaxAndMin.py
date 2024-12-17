while True:
    try:
        lista=input("\nIntroduceti numere separate prin spatii: ").strip()
        numere=[int(num) for num in lista.split()]                         #transforma intrarea intr-o lista de numere, dacă lista = "10 20 30", atunci numere va deveni [10, 20, 30]
        if not numere:
            print("Nu ati introdus niciun numar in lista. Incercati din nou.")
            continue
        if len(numere)==1:
            print("Ati introdus un singur numar.")
        else:
            print(f"Maximul este {max(numere)}, iar minimul este {min(numere)}")

    except ValueError:
        print("Eroare! Introduceti din nou numere separate prin spatii")
