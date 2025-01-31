class BankAccount:
    def __init__(self, initial_balance=0):
        """Inițializăm contul bancar cu un sold de start."""
        self._balance = initial_balance  # Atribut privat

    def deposit(self, amount):
        """Depune o sumă în cont."""
        if amount > 0:
            self._balance += amount
            print(f"Depunere reușită: {amount} RON")
        else:
            print("Suma de depunere trebuie să fie pozitivă.")

    def withdraw(self, amount):
        """Retrage o sumă din cont dacă există suficient sold."""
        if amount > 0:
            if self._balance >= amount:
                self._balance -= amount
                print(f"Retragere reușită: {amount} RON")
            else:
                print("Fonduri insuficiente!")
        else:
            print("Suma de retragere trebuie să fie pozitivă.")

    def get_balance(self):
        """Obține soldul curent al contului."""
        return self._balance


# Funcția principală pentru interacțiune cu utilizatorul
def main():
    print("Bine ai venit la gestionarea contului bancar!")

    # Solicită utilizatorului suma inițială pentru cont
    initial_balance = float(input("Introdu soldul inițial al contului: "))
    account = BankAccount(initial_balance)

    while True:
        print("\nOpțiuni disponibile:")
        print("1. Depunere")
        print("2. Retragere")
        print("3. Vizualizare sold")
        print("4. Ieșire")

        option = input("Alege o opțiune (1-4): ")

        if option == "1":
            deposit_amount = float(input("Introdu suma de depus: "))
            account.deposit(deposit_amount)
        elif option == "2":
            withdraw_amount = float(input("Introdu suma de retras: "))
            account.withdraw(withdraw_amount)
        elif option == "3":
            print(f"Soldul curent este: {account.get_balance()} RON")
        elif option == "4":
            print("Mulțumim că ai folosit serviciile noastre. La revedere!")
            break
        else:
            print("Opțiune invalidă! Te rog să alegi un număr între 1 și 4.")


if __name__ == "__main__":
    main()
