def unique_pair_sum(numbers, target):
    pairs = set()
    for num in numbers:
        complement = target - num
        if complement in numbers:
            pairs.add((min(num, complement), max(num, complement)))
    return pairs
while True:
    try:
        numbers = list(map(int, input("Introdu o listă de numere separate prin spațiu: ").split()))
        target = int(input("Introdu valoarea țintă: "))
        print("Perechi unice:", unique_pair_sum(numbers, target))
    except ValueError:
        print("Te rog să introduci doar numere întregi.")

    cont = input("Vrei să continui? (da/nu): ").strip().lower()
    if cont != "da":
        print("La revedere!")
        break
