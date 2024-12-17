#un tuple este un tip de structură de date din Python care:
#este imutabilă: Odată creat, nu poate fi modificat (nu poți adăuga, elimina sau schimba elemente).
#poate conține orice tip de date: Elementele unui tuple pot fi numere, string-uri, alte tuple, liste, etc.
#folosită adesea pentru a grupa și organiza date care nu trebuie modificate.

while True:
    try:
        user_input = input("\nIntroduceți elementele tuplăi separate prin spații: ").strip()

        my_tuple = tuple(user_input.split())

        cautari = input("Introduceți elementele pe care doriți să le căutați (separate prin spații): ").strip()
        cautari = [int(num) for num in cautari.split()]

        for cautare in cautari:
            if cautare in my_tuple:
                print(f"Elementul {cautare} există în tuplă.")
            else:
                print(f"Elementul {cautare} nu se găsește în tuplă.")

    except ValueError:
        print("Eroare!")
