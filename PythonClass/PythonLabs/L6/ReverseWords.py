def reverse_words():
    while True:
        try:
            sentence = input("Introdu propoziția: ").strip()
            if not sentence:
                raise ValueError("Propoziția nu poate fi goală.")

            words = sentence.split()  # Împărțim propoziția în cuvinte eliminând spațiile suplimentare
            reversed_sentence = " ".join(words[::-1])  # Inversăm ordinea cuvintelor
            print("Propoziția inversată:", reversed_sentence)
            break
        except ValueError as e:
            print("Eroare:", e)
        except Exception:
            print("A apărut o eroare necunoscută. Încearcă din nou.")


reverse_words()
