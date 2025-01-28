class BankAccount:
    def __init__(self):
        self._balance = 0  # Atribut privat pentru sold

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Depunere efectuată: {amount}")
        else:
            print("Suma de depus trebuie să fie pozitivă.")

    def withdraw(self, amount):
        if amount > self._balance:
            print("Fonduri insuficiente.")
        elif amount > 0:
            self._balance -= amount
            print(f"Retragere efectuată: {amount}")
        else:
            print("Suma de retras trebuie să fie pozitivă.")

    def get_balance(self):
        return self._balance

# Exemplu de utilizare
account = BankAccount()
account.deposit(1000)
account.withdraw(500)
print(f"Sold curent: {account.get_balance()}")  # Output: Sold curent: 500
