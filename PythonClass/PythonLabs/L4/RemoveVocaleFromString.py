while True:
    try:
        user_input = input("\nIntroduceți un text: ").strip()


        def remove_vowels(input_string):
            vowels = "aeiouAEIOUăĂîÎâÂ"  # Toate vocalele, inclusiv majuscule
            return "".join([char for char in input_string if char not in vowels])


        print("Text fără vocale:", remove_vowels(user_input))

    except Exception as e:
        print("Eroare! Vă rugăm să introduceți un text valid.")


#[char for char in input_string if char not in vowels]:
    #char este o variabilă care parcurge fiecare caracter din input_string (adică fiecare literă din string-ul dat de utilizator).
    #if char not in vowels verifică dacă caracterul curent char NU face parte din lista vocalelelor.
    #Dacă caracterul nu este o vocală, este inclus în lista.