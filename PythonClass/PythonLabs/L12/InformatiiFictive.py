import requests
from tabulate import tabulate

# 🔹 Endpoint-ul API-ului
URL = "https://jsonplaceholder.typicode.com/users"

try:
    # 🔹 Trimitere cerere GET către API
    response = requests.get(URL)
    response.raise_for_status()  # Verificăm dacă cererea a fost cu succes

    # 🔹 Convertim răspunsul în format JSON
    users = response.json()

    # 🔹 Extragem și afișăm datele în format tabelar
    tabel_date = []
    for user in users:
        tabel_date.append([
            user["id"], user["name"], user["username"], user["email"],
            user["address"]["city"], user["company"]["name"],
            user["phone"], user["website"]
        ])

    # 🔹 Afișăm tabelul
    print("\n📌 Lista completă de utilizatori:")
    print(tabulate(tabel_date, headers=["ID", "Nume", "Username", "Email", "Oraș", "Companie", "Telefon", "Website"], tablefmt="grid"))

    # 🔹 Filtrare utilizatori după oraș
    oras_filtru = input("\n🔍 Introdu orașul pentru filtrare: ").strip()
    utilizatori_filtrati = [user for user in users if user["address"]["city"].lower() == oras_filtru.lower()]

    if utilizatori_filtrati:
        tabel_filtrat = [[
            user["id"], user["name"], user["username"], user["email"],
            user["address"]["city"], user["company"]["name"],
            user["phone"], user["website"]
        ] for user in utilizatori_filtrati]

        print(f"\n📌 Utilizatori din orașul {oras_filtru}:")
        print(tabulate(tabel_filtrat, headers=["ID", "Nume", "Username", "Email", "Oraș", "Companie", "Telefon", "Website"], tablefmt="grid"))
    else:
        print(f"\n⚠️ Nu există utilizatori în orașul {oras_filtru}.")

except requests.exceptions.RequestException as e:
    print(f"\n❌ Eroare la conectarea cu API-ul: {e}")
