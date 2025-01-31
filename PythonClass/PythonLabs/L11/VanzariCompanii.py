import pandas as pd

# Încărcarea fișierului CSV
fisier_csv = "vanzari.csv"  # Asigură-te că fișierul este în același director cu scriptul
df = pd.read_csv(fisier_csv, parse_dates=["data_vanzarii"])

# 1️⃣ Care sunt cele mai vândute produse pe lună?
df["luna"] = df["data_vanzarii"].dt.to_period("M")
cele_mai_vandute = df.groupby(["luna", "produs"])["cantitate_vanduta"].sum().reset_index()
cele_mai_vandute = cele_mai_vandute.sort_values(["luna", "cantitate_vanduta"], ascending=[True, False])

# 2️⃣ Care a fost venitul total pe fiecare produs?
df["venit_total"] = df["cantitate_vanduta"] * df["pret"]
venit_pe_produs = df.groupby("produs")["venit_total"].sum().reset_index()

# 3️⃣ Filtrarea vânzărilor pentru un interval de timp
start_date = "2024-01-01"
end_date = "2024-03-31"
vanzari_filtrate = df[(df["data_vanzarii"] >= start_date) & (df["data_vanzarii"] <= end_date)]

# 4️⃣ Gruparea datelor după lună și an pentru a afla venitul mediu lunar
venit_mediu_lunar = df.groupby("luna")["venit_total"].mean().reset_index()

# 🔹 Afișarea rezultatelor
print("\n🔹 Cele mai vândute produse pe lună:")
print(cele_mai_vandute)

print("\n🔹 Venitul total pe fiecare produs:")
print(venit_pe_produs)

print("\n🔹 Vânzări filtrate între 01.01.2024 și 31.03.2024:")
print(vanzari_filtrate)

print("\n🔹 Venitul mediu lunar:")
print(venit_mediu_lunar)
