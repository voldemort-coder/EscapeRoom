import math

# Clasa de bază Formă
class Forma:
    def aria(self):
        """Metodă abstractă care trebuie să fie implementată în subclase."""
        pass

    def __str__(self):
        """Reprezentare textuală generică pentru o formă geometrică."""
        return "Formă cu proprietăți necunoscute"

# Clasa Cerc care moștenește de la Forma
class Cerc(Forma):
    def __init__(self, raza):
        self.raza = raza

    def aria(self):
        """Calculăm aria cercului."""
        return math.pi * self.raza ** 2

    def __str__(self):
        """Reprezentarea textuală pentru un cerc."""
        return f"Cerc cu raza {self.raza} are aria {self.aria():.2f}"

# Clasa Dreptunghi care moștenește de la Forma
class Dreptunghi(Forma):
    def __init__(self, latime, inaltime):
        self.latime = latime
        self.inaltime = inaltime

    def aria(self):
        """Calculăm aria dreptunghiului."""
        return self.latime * self.inaltime

    def __str__(self):
        """Reprezentarea textuală pentru un dreptunghi."""
        return f"Dreptunghi cu lățimea {self.latime} și înălțimea {self.inaltime} are aria {self.aria()}"

# Funcția principală pentru testare
def main():
    # Cerem utilizatorului să introducă datele pentru cerc
    raza = float(input("Introdu raza cercului: "))
    cerc = Cerc(raza)  # Creăm instanța de Cerc

    # Cerem utilizatorului să introducă datele pentru dreptunghi
    latime = float(input("Introdu lățimea dreptunghiului: "))
    inaltime = float(input("Introdu înălțimea dreptunghiului: "))
    dreptunghi = Dreptunghi(latime, inaltime)  # Creăm instanța de Dreptunghi

    # Afișăm informațiile despre forme
    print("\nDetalii cerc:")
    print(cerc)  # Afișăm detaliile cercului

    print("\nDetalii dreptunghi:")
    print(dreptunghi)  # Afișăm detaliile dreptunghiului

if __name__ == "__main__":
    main()
