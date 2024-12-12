while True:
    try:
        numar=int(input("\nIntrodu un numar pentru care vrei sa afle factorialul: "))
        if numar<0:
            print("Nu putem calcula factorialul pentru numere negative")
            continue
        elif numar==0:
            print("Factorialul lui 0 este 1")
            continue
        else:
            factorial = 1
            for i in range(1, numar + 1):
                factorial *= i
            print(f"Factorialul lui {numar} este {factorial}.")

    except ValueError:
        print("Te rog să introduci un număr valid.")