import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 🔹 Creăm un DataFrame gol pentru a stoca vânzările
df = pd.DataFrame(columns=["data_vanzarii", "produs", "cantitate_vanduta", "pret", "promotie"])

# 🔹 Cerem utilizatorului să introducă numărul de înregistrări
nr_vanzari = int(input("Câte vânzări dorești să introduci? "))

for i in range(nr_vanzari):
    print(f"\n🔹 Introdu detaliile pentru vânzarea {i + 1}:")
    data = input("Data vânzării (YYYY-MM-DD): ")
    produs = input("Produsul vândut: ")
    cantitate = int(input("Cantitate vândută: "))
    pret = float(input("Preț per bucată: "))
    promotie = input("A fost promoție? (da/nu): ").strip().lower()
    promotie = 1 if promotie == "da" else 0

    # Adăugăm înregistrarea în DataFrame
    df = df.append({"data_vanzarii": data, "produs": produs, "cantitate_vanduta": cantitate,
                    "pret": pret, "promotie": promotie}, ignore_index=True)

# 🔹 Convertim coloana data_vanzarii în format de dată
df["data_vanzarii"] = pd.to_datetime(df["data_vanzarii"])

# 🔹 Calculăm venitul total și profitul
df["venit_total"] = df["cantitate_vanduta"] * df["pret"]
df["profit"] = df["venit_total"] * 0.2  # Presupunem un profit fix de 20%

# 🔹 Evoluția veniturilor și profitului pe zile
evolutie_vanzari = df.groupby("data_vanzarii")[["venit_total", "profit"]].sum()

plt.figure(figsize=(12, 5))
plt.plot(evolutie_vanzari.index, evolutie_vanzari["venit_total"], label="Venit Total", marker="o")
plt.plot(evolutie_vanzari.index, evolutie_vanzari["profit"], label="Profit Total", marker="s", linestyle="dashed")
plt.xlabel("Data")
plt.ylabel("Sume (Lei)")
plt.title("Evoluția veniturilor și profitului zilnic")
plt.legend()
plt.grid()
plt.xticks(rotation=45)
plt.show()

# 🔹 Distribuția prețurilor și cantităților vândute
plt.figure(figsize=(12, 5))
sns.histplot(df["pret"], bins=10, kde=True, color="blue", label="Prețuri")
sns.histplot(df["cantitate_vanduta"], bins=10, kde=True, color="red", label="Cantități", alpha=0.6)
plt.xlabel("Valoare")
plt.ylabel("Frecvență")
plt.title("Distribuția prețurilor și cantităților vândute")
plt.legend()
plt.show()

# 🔹 Analiza impactului promoțiilor
impact_promotii = df.groupby("promotie")["venit_total"].sum()
print("\n🔹 Impactul promoțiilor asupra veniturilor:")
print(f"Venit fără promoții: {impact_promotii.get(0, 0)} Lei")
print(f"Venit cu promoții: {impact_promotii.get(1, 0)} Lei")
