from geometry import circle_area, circumference, rectangle_area, perimeter


def main():
    while True:
        try:
            # Calcul pentru cerc
            radius = float(input("Introdu raza cercului: "))
            print(f"Aria cercului: {circle_area(radius)}")
            print(f"Circumferința cercului: {circumference(radius)}")

            # Calcul pentru dreptunghi
            length = float(input("Introdu lungimea dreptunghiului: "))
            width = float(input("Introdu lățimea dreptunghiului: "))
            print(f"Aria dreptunghiului: {rectangle_area(length, width)}")
            print(f"Perimetrul dreptunghiului: {perimeter(length, width)}")
            break
        except ValueError:
            print("Te rog să introduci valori numerice valide.")


main()
