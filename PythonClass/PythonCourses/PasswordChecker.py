def verifica_parola(parola):
    # Criterii pentru parola puternică
    lungime_minima = len(parola) >= 8
    contine_majuscula = any(char.isupper() for char in parola)
    contine_minuscula = any(char.islower() for char in parola)
    contine_cifra = any(char.isdigit() for char in parola)
    contine_special = any(char in "!@#$%^&*()-_+=<>?" for char in parola)
    fara_spatii = " " not in parola
    # Verificăm dacă toate criteriile sunt îndeplinite
    este_puternica = (
        lungime_minima
        and contine_majuscula
        and contine_minuscula
        and contine_cifra
        and contine_special
        and fara_spatii
    )
    # Generăm feedback dacă parola este slabă
    feedback = []
    if not lungime_minima:
        feedback.append("Lungimea trebuie să fie de cel puțin 8 caractere.")
    if not contine_majuscula:
        feedback.append("Trebuie să conțină cel puțin o literă majusculă.")
    if not contine_minuscula:
        feedback.append("Trebuie să conțină cel puțin o literă minusculă.")
    if not contine_cifra:
        feedback.append("Trebuie să conțină cel puțin o cifră.")
    if not contine_special:
        feedback.append("Trebuie să conțină cel puțin un caracter special (!@#$%^&*()-_+=<>?).")
    if not fara_spatii:
        feedback.append("Nu trebuie să conțină spații.")

    return este_puternica, feedback

# Bucla principală
while True:
    # Solicităm parolele de la utilizator
    input_parole = input("Introduceți una sau mai multe parole separate prin virgulă: ")

    # Separăm parolele introduse
    parole = [parola.strip() for parola in input_parole.split(",")]

    # Verificăm fiecare parolă și afișăm rezultatele
    for parola in parole:
        este_puternica, feedback = verifica_parola(parola)
        if este_puternica:
            print(f"\nParola '{parola}' este puternică.")
        else:
            print(f"\nParola '{parola}' este slabă.")
            print("Feedback:")
            for criteriu in feedback:
                print(f"- {criteriu}")
    print()
