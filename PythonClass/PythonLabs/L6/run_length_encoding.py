def run_length_encoding():
    while True:
        try:
            text = input("Introdu șirul de caractere: ").strip()
            if not text:
                raise ValueError("Șirul nu poate fi gol.")

            encoded = []  # Listă pentru a stoca codificarea
            i = 0

            while i < len(text):
                count = 1
                while i + 1 < len(text) and text[i] == text[i + 1]:  # Contorizăm caracterele consecutive
                    count += 1
                    i += 1
                encoded.append(f"{text[i]}{count}")  # Adăugăm caracterul și numărul de apariții
                i += 1

            print("Codificare RLE:", "".join(encoded))
            break
        except ValueError as e:
            print("Eroare:", e)
        except Exception:
            print("A apărut o eroare necunoscută. Încearcă din nou.")


run_length_encoding()
