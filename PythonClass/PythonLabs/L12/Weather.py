import requests


def get_weather(city):
    url = f"https://wttr.in/{city}?format=%C+|+%t+|+%w"
    try:
        response = requests.get(url, verify=False)  # Evităm erorile SSL
        response.raise_for_status()  # Verificăm dacă răspunsul a fost cu succes

        # Verificăm dacă orașul nu este valid
        if "Unknown location" in response.text:
            print(f"⚠️ Orasul '{city}' nu a fost gasit. Te rog să încerci din nou!")
            return

        # Extragem datele meteo
        conditii, temperatura, vant = response.text.split(" | ")

        # Afișăm datele într-un format prietenos
        print("\n🌍 Vremea pentru:", city.title())
        print(f"🌤️ Condiții: {conditii}")
        print(f"🌡️ Temperatura: {temperatura}")
        print(f"💨 Vânt: {vant}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Eroare la conectarea cu API-ul: {e}")


# 🔹 Cerem utilizatorului să introducă un oraș
oras = input("📝 Introdu numele orasului: ").strip()
get_weather(oras)
