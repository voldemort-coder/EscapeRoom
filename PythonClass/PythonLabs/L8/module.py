import math


def math_operations():
    while True:
        try:
            num = float(input("Introdu un număr pentru rădăcina pătrată și factorial: "))
            angle = float(input("Introdu un unghi (în grade) pentru calculul sinusului: "))

            # Calculăm rădăcina pătrată
            sqrt_result = math.sqrt(num)
            print(f"Rădăcina pătrată a {num} este {sqrt_result}")

            # Calculăm factorialul (doar pentru numere întregi)
            if num.is_integer() and num >= 0:
                factorial_result = math.factorial(int(num))
                print(f"Factorialul lui {int(num)} este {factorial_result}")
            else:
                print(f"Nu se poate calcula factorialul pentru {num} (număr neîntreg sau negativ).")

            # Calculăm sinusul
            radians = math.radians(angle)  # Convertim gradele în radiani
            sin_result = math.sin(radians)
            print(f"Sinusul unghiului de {angle} grade este {sin_result}")
            break
        except ValueError:
            print("Te rog să introduci valori numerice valide.")


math_operations()
