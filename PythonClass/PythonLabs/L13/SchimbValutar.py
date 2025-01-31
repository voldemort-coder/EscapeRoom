import requests


def obtine_curs_valutar(moneda_provenienta):
    url = f"https://api.exchangerate-api.com/v4/latest/{moneda_provenienta}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Aruncă o eroare dacă API-ul nu răspunde corect
        data = response.json()
        return data["rates"]  # Returnează toate ratele disponibile
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Eroare la conectarea la API: {e}")
        return None


def converteste_suma(moneda_provenienta, moneda_destinatie, suma):
    rates = obtine_curs_valutar(moneda_provenienta)

    if rates and moneda_destinatie in rates:
        curs = rates[moneda_destinatie]
        suma_convertita = suma * curs
        print(f"\n✅ {suma} {moneda_provenienta} = {round(suma_convertita, 2)} {moneda_destinatie}")
        print(f"💱 Curs de schimb: 1 {moneda_provenienta} = {curs} {moneda_destinatie}")
    else:
        print("❌ Moneda de destinație nu este disponibilă.")


def main():
    moneda_provenienta = input("Introduceți moneda de proveniență (ex: USD, EUR, RON): ").upper()
    moneda_destinatie = input("Introduceți moneda de destinație (ex: USD, EUR, RON): ").upper()

    try:
        suma = float(input("Introduceți suma pe care doriți să o convertiți: "))
        converteste_suma(moneda_provenienta, moneda_destinatie, suma)
    except ValueError:
        print("❌ Te rog să introduci o sumă validă!")


if __name__ == "__main__":
    main()
