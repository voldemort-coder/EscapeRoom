import pandas as pd


def procesare_csv(input_file, output_file):
    try:
        # 📥 Citirea fișierului CSV
        df = pd.read_csv(input_file)

        # 🧮 Calcularea valorii totale pentru fiecare comandă
        df["Total"] = df["Cantitate"] * df["Pret unitar"]

        # 💾 Salvarea rezultatelor într-un nou fișier CSV
        df.to_csv(output_file, index=False)

        print(f"✅ Fișierul procesat a fost salvat ca: {output_file}")

    except FileNotFoundError:
        print("❌ Fișierul specificat nu a fost găsit.")
    except Exception as e:
        print(f"⚠️ Eroare: {e}")


# 🔹 Utilizatorul introduce numele fișierului de intrare
input_file = input("📂 Introdu numele fișierului CSV de procesat (ex: comenzi.csv): ").strip()
output_file = "comenzi_procesate.csv"

# 🔄 Procesarea fișierului
procesare_csv(input_file, output_file)
