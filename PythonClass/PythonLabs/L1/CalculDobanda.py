credit = float(input("Introdu valoarea creditului: "))
rata = float(input("Introdu rata dobânzii (în procente): "))
timp = float(input("Introdu timpul (în ani): "))

dobanda = (credit * rata * timp) / 100
print(f"Dobânda totală este: {dobanda:.2f} unități monetare.")

#Funcția input() în Python este folosită pentru a citi date de la utilizator sub formă de șiruri de caractere (string)."
# Orice lucru pe care utilizatorul îl introduce este, prin default, tratat ca un șir de caractere (de exemplu, "10" sau "3.14").

#float() este folosit pentru a converti acele șiruri de caractere într-un număr zecimal (tipul float),"
#astfel încât să putem efectua operații matematice cu ele.")
