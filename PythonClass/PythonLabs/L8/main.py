# main.py
import math_operations as mo


def main():
    while True:
        try:
            print("Operații matematice:")
            print("1. Adunare")
            print("2. Scădere")
            print("3. Înmulțire")
            print("4. Împărțire")
            print("0. Ieșire")

            choice = input("Alege o operație (1-4 sau 0 pentru ieșire): ").strip()

            if choice == "0":
                print("La revedere!")
                break

            if choice not in {"1", "2", "3", "4"}:
                print("Alegere invalidă. Încearcă din nou.")
                continue

            a = float(input("Introdu primul număr: "))
            b = float(input("Introdu al doilea număr: "))

            if choice == "1":
                print(f"Rezultat: {mo.add(a, b)}")
            elif choice == "2":
                print(f"Rezultat: {mo.subtract(a, b)}")
            elif choice == "3":
                print(f"Rezultat: {mo.multiply(a, b)}")
            elif choice == "4":
                print(f"Rezultat: {mo.divide(a, b)}")
        except ValueError as e:
            print("Eroare:", e)


main()
