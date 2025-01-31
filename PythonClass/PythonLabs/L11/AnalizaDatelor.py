import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Setăm numărul de zile pentru simulare
num_days = 60
np.random.seed(42)  # Pentru reproducibilitate

# Generăm datele
sales_data = []
for day in range(1, num_days + 1):
    num_products = np.random.randint(5, 16)  # 5-15 produse pe zi

    for _ in range(num_products):
        # Generăm datele aleatorii pentru un produs
        product_id = f"Produs_{np.random.randint(1, 101)}"  # ID produs
        price = max(0, np.random.normal(40, 8))  # Preț din distribuție normală
        quantity = np.random.randint(1, 11)  # Cantitate între 1 și 10

        # Simulăm promoțiile cu 30% probabilitate
        promotion = np.random.rand() < 0.3
        if promotion:
            price *= 0.8  # Reducere de 20%

        # Calculăm totalul vânzărilor și profitul
        total_sales = price * quantity
        profit = total_sales * 0.3  # Marja de profit este 30%

        # Adăugăm în dataset
        sales_data.append({
            "Zi": day,
            "Produs": product_id,
            "Pret unitar": round(price, 2),
            "Cantitate vanduta": quantity,
            "Total vanzari": round(total_sales, 2),
            "Profit": round(profit, 2),
            "Promotie activa": promotion
        })

# Creăm DataFrame
sales_df = pd.DataFrame(sales_data)

# Calculăm totaluri pe zi
daily_totals = sales_df.groupby("Zi").agg({
    "Total vanzari": "sum",
    "Profit": "sum"
}).reset_index()

# Vizualizare evoluție venituri și profituri pe zile
plt.figure(figsize=(12, 6))
plt.plot(daily_totals["Zi"], daily_totals["Total vanzari"], label="Venit Total", marker="o")
plt.plot(daily_totals["Zi"], daily_totals["Profit"], label="Profit Total", marker="s")
plt.title("Evoluția veniturilor și profitului pe zile")
plt.xlabel("Zi")
plt.ylabel("Valoare (RON)")
plt.legend()
plt.grid()
plt.show()

# Distribuția prețurilor
plt.figure(figsize=(12, 6))
plt.hist(sales_df["Pret unitar"], bins=20, color="blue", alpha=0.7, edgecolor="black")
plt.title("Distribuția prețurilor produselor")
plt.xlabel("Pret unitar (RON)")
plt.ylabel("Frecvență")
plt.grid()
plt.show()

# Distribuția cantităților
plt.figure(figsize=(12, 6))
plt.hist(sales_df["Cantitate vanduta"], bins=10, color="green", alpha=0.7, edgecolor="black")
plt.title("Distribuția cantităților vândute")
plt.xlabel("Cantitate vandută")
plt.ylabel("Frecvență")
plt.grid()
plt.show()

# Impactul promoțiilor
promotions_summary = sales_df.groupby("Promotie activa").agg({
    "Pret unitar": "mean",
    "Total vanzari": "mean"
}).rename(index={True: "Cu promoție", False: "Fără promoție"})

print("\nImpactul promoțiilor asupra prețurilor și veniturilor medii:")
print(promotions_summary)

# Vizualizare impact promoții
promotions_summary.plot(kind="bar", figsize=(10, 6), color=["orange", "purple"])
plt.title("Impactul promoțiilor asupra prețurilor și veniturilor medii")
plt.ylabel("Valoare medie (RON)")
plt.xlabel("Categorie")
plt.grid()
plt.show()

# Salvăm datasetul într-un fișier CSV
sales_df.to_csv("dataset_vanzari.csv", index=False)
print("\nDatasetul a fost salvat ca 'dataset_vanzari.csv'.")