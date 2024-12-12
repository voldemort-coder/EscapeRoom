import random
numar_secret = random.randint(1, 100)      #random.randint() alege un număr întreg aleatoriu între 1 și 100 (inclusiv)
incercari = 0

print("Ghicește numărul secret (între 1 și 100).")

while True:
    try:
        ghicire = int(input("Introdu un numar care crezi ca e corect: "))
        if ghicire < 1 or ghicire > 100:
            print("Eroare: Numărul trebuie să fie între 1 și 100!")
            continue
        incercari += 1  #numărul de încercări

        if ghicire < numar_secret:
            print("Prea mic! Încearcă din nou.")
        elif ghicire > numar_secret:
            print("Prea mare! Încearcă din nou.")
        else:
            print(f"Corect! Ai ghicit numărul {numar_secret} în {incercari} încercări.")
            break  # Terminăm jocul
    except ValueError:
        print("Te rog introdu un număr valid!")

    if incercari == 10:
        print(f"Game Over! Nu ai ghicit :( numărul a fost {numar_secret}.")
        break


    '''Folosim while true pentru a forma o buclă continuă până la ghicirea corectă'''