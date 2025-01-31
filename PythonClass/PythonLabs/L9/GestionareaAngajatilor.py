class Employee:
    def __init__(self, name, salary):
        """Inițializăm un angajat cu nume și salariu."""
        self.name = name
        self.salary = salary

    def get_details(self):
        """Returnează detaliile despre angajat."""
        return f"Employee: {self.name}, Salary: {self.salary}"


class Manager(Employee):
    def __init__(self, name, salary, department):
        """Inițializăm un manager cu nume, salariu și departament."""
        super().__init__(name, salary)  # Apelăm constructorul clasei de bază
        self.department = department

    def get_details(self):
        """Suprascriem metoda pentru a include și departamentul."""
        return f"Manager: {self.name}, Salary: {self.salary}, Department: {self.department}"


def main():
    print("Introducerea detaliilor angajatului:")
    # Cerem utilizatorului să introducă datele pentru angajat
    name = input("Numele angajatului: ")
    salary = float(input("Salariul angajatului: "))

    # Creăm instanța de Employee
    emp = Employee(name, salary)

    print("\nIntroducerea detaliilor managerului:")
    # Cerem utilizatorului să introducă datele pentru manager
    manager_name = input("Numele managerului: ")
    manager_salary = float(input("Salariul managerului: "))
    department = input("Departamentul managerului: ")

    # Creăm instanța de Manager
    mgr = Manager(manager_name, manager_salary, department)

    # Afișăm detaliile angajatului și managerului
    print("\nDetalii angajat:")
    print(emp.get_details())

    print("\nDetalii manager:")
    print(mgr.get_details())


if __name__ == "__main__":
    main()
