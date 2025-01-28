def is_palindrome():
    while True:
        try:
            text = input("Introdu șirul de verificat: ").strip()
            if not text:
                raise ValueError("Șirul nu poate fi gol.")

            # Normalizăm șirul: eliminăm spațiile și transformăm în litere mici
            normalized_text = "".join(c.lower() for c in text if c.isalnum())
            if normalized_text == normalized_text[::-1]:  # Verificăm dacă este palindrom
                print("Rezultat: True (este un palindrom)")
            else:
                print("Rezultat: False (nu este un palindrom)")
            break
        except ValueError as e:
            print("Eroare:", e)
        except Exception:
            print("A apărut o eroare necunoscută. Încearcă din nou.")


is_palindrome()
