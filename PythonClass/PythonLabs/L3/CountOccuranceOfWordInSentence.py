while True:
    try:
        propozitie=input("\nIntrodu o propozitie: ")
        numar=input("Introdu cuvantul pe care vrei sa il numeri: ")

        if not propozitie.strip():  #verifica daca propozitia este goala
            print("Nu ai introdus nimic")
            continue

        if not numar.strip():
            print("Nu ai introdus cuvantul")
            continue

        propozitie=propozitie.lower()                   #ignora diferentele dintre literele mari si cele mici
        numar=numar.lower()
        aparitii=propozitie.split().count(numar)        #cu split() impartim propozitia in cuvinte si cu count() sa numere cuvantul specificat
        print(f"Cuvantul '{numar}' apare de {aparitii} ori în propozitie.")

    except Exception as e:
        print(f"A aparut o eroare: {e}")


#except exception as e:
#    -captureaza orice eroare
#    -variabila e stocheaza informatii despre eroare, precum tipul erorii si mesajul acesteia
#    -e poate fi utilizata pentru a afisa un mesaj depsre ce s-a intamplat, util pentru a rezolva problema

