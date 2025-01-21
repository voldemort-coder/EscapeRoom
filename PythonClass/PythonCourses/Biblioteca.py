class Carte:
    def __init__(self, titlu, autor, isbn):
        self.titlu = titlu
        self.autor = autor
        self.isbn = isbn
        self.este_imprumutata = False

    def __str__(self):
        return f"{self.titlu} de {self.autor} (ISBN: {self.isbn}) {'[Împrumutată]' if self.este_imprumutata else '[Disponibilă]'}"

class MembruBiblioteca:
    def __init__(self, nume):
        self.nume = nume
        self.carti_imprumutate = []

    def imprumuta_carte(self, carte):
        if not carte.este_imprumutata:
            carte.este_imprumutata = True
            self.carti_imprumutate.append(carte)
            print(f"{self.nume} a împrumutat cartea '{carte.titlu}'.")
        else:
            print(f"Cartea '{carte.titlu}' este deja împrumutată.")

    def returneaza_carte(self, carte):
        if carte in self.carti_imprumutate:
            carte.este_imprumutata = False
            self.carti_imprumutate.remove(carte)
            print(f"{self.nume} a returnat cartea '{carte.titlu}'.")
        else:
            print(f"{self.nume} nu a împrumutat cartea '{carte.titlu}'.")

class Biblioteca:
    def __init__(self):
        self.carti = []

    def adauga_carte(self, carte):
        self.carti.append(carte)
        print(f"Cartea '{carte.titlu}' a fost adăugată în bibliotecă.")

    def sterge_carte(self, carte):
        if carte in self.carti:
            self.carti.remove(carte)
            print(f"Cartea '{carte.titlu}' a fost ștearsă din bibliotecă.")
        else:
            print(f"Cartea '{carte.titlu}' nu se găsește în bibliotecă.")

    def listeaza_carti_disponibile(self):
        disponibile = [carte for carte in self.carti if not carte.este_imprumutata]
        if disponibile:
            print("Cărți disponibile:")
            for carte in disponibile:
                print(f"  - {carte}")
        else:
            print("Nu există cărți disponibile.")

# Exemplu de inițializare a sistemului
def main():
    biblioteca = Biblioteca()

    # Adăugăm 5 cărți
    carti = [
        Carte("1984", "George Orwell", "12345"),
        Carte("Mândrie și Prejudecată", "Jane Austen", "23456"),
        Carte("Război și Pace", "Lev Tolstoi", "34567"),
        Carte("Crimă și Pedeapsă", "Fyodor Dostoevsky", "45678"),
        Carte("Micul Prinț", "Antoine de Saint-Exupéry", "56789")
    ]

    for carte in carti:
        biblioteca.adauga_carte(carte)

    # Creăm 3 membri
    membri = [
        MembruBiblioteca("Alice"),
        MembruBiblioteca("Bob"),
        MembruBiblioteca("Charlie")
    ]

    while True:
        print("\n--- Sistem Biblioteca ---")
        print("1. Listează cărțile disponibile")
        print("2. Împrumută o carte")
        print("3. Returnează o carte")
        print("4. Ieșire")

        optiune = input("Alege o opțiune: ")

        if optiune == "1":
            biblioteca.listeaza_carti_disponibile()

        elif optiune == "2":
            biblioteca.listeaza_carti_disponibile()
            titlu = input("Introdu titlul cărții pe care dorești să o împrumuți: ")
            carte_gasita = next((carte for carte in biblioteca.carti if carte.titlu == titlu), None)
            if carte_gasita:
                nume_membru = input("Introdu numele membrului: ")
                membru = next((m for m in membri if m.nume == nume_membru), None)
                if membru:
                    membru.imprumuta_carte(carte_gasita)
                else:
                    print("Membru neexistent.")
            else:
                print("Cartea nu a fost găsită.")

        elif optiune == "3":
            nume_membru = input("Introdu numele membrului care returnează o carte: ")
            membru = next((m for m in membri if m.nume == nume_membru), None)
            if membru:
                print("Cărți împrumutate:")
                for carte in membru.carti_imprumutate:
                    print(f"  - {carte}")
                titlu = input("Introdu titlul cărții pe care dorești să o returnezi: ")
                carte_gasita = next((carte for carte in membru.carti_imprumutate if carte.titlu == titlu), None)
                if carte_gasita:
                    membru.returneaza_carte(carte_gasita)
                else:
                    print("Cartea nu a fost găsită în lista de cărți împrumutate.")
            else:
                print("Membru neexistent.")

        elif optiune == "4":
            print("Ieșire din sistem.")
            break

        else:
            print("Opțiune invalidă. Încearcă din nou.")

if __name__ == "__main__":
    main()
