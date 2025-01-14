def count_words_in_file(file_path):
    while True:
        try:
            # Deschidem fișierul
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            # Separăm conținutul în cuvinte și numărăm
            word_count = len(content.split())
            return word_count
        except FileNotFoundError:
            print("Fișierul nu a fost găsit. Te rog să introduci o cale validă.")
            # Cerem o cale nouă de la utilizator
            file_path = input("Introdu calea către fișier: ")
        except Exception as e:
            print(f"A apărut o eroare: {e}")
            break

# Exemplu de utilizare
file_path = input("Introdu calea către fișierul text: ")
numar_cuvinte = count_words_in_file(file_path)
if numar_cuvinte is not None:
    print(f"Fișierul conține {numar_cuvinte} cuvinte.")
