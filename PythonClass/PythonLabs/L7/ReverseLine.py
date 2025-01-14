def reverse_lines(input_file, output_file):
    while True:
        try:
            # Deschidem fișierul de intrare pentru citire
            with open(input_file, 'r', encoding='utf-8') as infile:
                lines = infile.readlines()

            # Deschidem fișierul de ieșire pentru scriere
            with open(output_file, 'w', encoding='utf-8') as outfile:
                for line in lines:
                    outfile.write(line[::-1] + '\n')

            print(f"Fișierul '{output_file}' a fost creat cu succes!")
            break  # Ieșim din buclă dacă totul a funcționat bine
        except FileNotFoundError:
            print(f"Fișierul '{input_file}' nu a fost găsit.")
            input_file = input("Te rog să introduci o cale validă pentru fișierul de intrare: ")
        except Exception as e:
            print(f"A apărut o eroare: {e}")
            break


# Exemplu de utilizare
while True:
    try:
        input_file = input("Introdu calea către fișierul de intrare: ")
        output_file = input("Introdu calea pentru fișierul de ieșire: ")
        reverse_lines(input_file, output_file)
        break  # Ieșim din buclă dacă funcția s-a executat fără probleme
    except Exception as e:
        print(f"A apărut o eroare neașteptată: {e}")
