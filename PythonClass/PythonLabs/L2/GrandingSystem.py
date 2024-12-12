while True:
    try:
        procentaj=int(input("\nIntrodu procentajul intre 1 si 100: "))
        if procentaj <= 0 or procentaj > 100:
            print("Eroare: Procentajul trebuie să fie între 1 și 100.")
        else:
            if procentaj >=90:
                nota= "A"
            elif procentaj>=80:
                nota= "B"
            elif procentaj >=70:
                nota= "C"
            elif procentaj>=60:
                nota= "D"
            else:
                nota= "F"
            print(f"\nNota ta este: {nota}")

    except ValueError:
        print("Eroare: Te rog introdu un număr valid!")