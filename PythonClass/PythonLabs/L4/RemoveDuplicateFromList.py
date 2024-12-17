while True:
    try:
        user_input = input("Introduceți o listă de numere separate prin spații : ").strip()

        num_list = [int(num) for num in user_input.split()]

        unique_list = []
        for num in num_list:
            if num not in unique_list:
                unique_list.append(num)                       #append(num) este o metodă a listei în Python care adaugă un element la sfârșitul listei
        print("Lista fără duplicate:", unique_list)

    except ValueError:
        print("Eroare! Introduceți doar numere separate prin spații.")
