#introducerea in grade C de catre utilizator
#Funcția `float` transformă textul introdus într-un număr zecimal, pentru a putea face calculul.

celsius = float(input("Introdu temperatura în grade Celsius: "))
fahrenheit = celsius * 9 / 5 + 32 #convertirea in grade F
print(f"{celsius} grade Celsius sunt echivalente cu {fahrenheit} grade Fahrenheit.")

#Folosim `print` pentru a afișa rezultatul. Litera `f` dinaintea șirului de caractere
# permite includerea variabilelor direct în text (f-string) si stie sa iti ia valoarea cu acea zecimala
