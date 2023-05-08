class Cerc:
    raza = None
    culoare = None

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descriere_cerc(self):
        print(f"Descriere cerc:\n"
              f"Cercul are raza {self.raza}\n"
              f"Cercul are culoarea {self.culoare}")

    def aria(self):
        pi = 3.14
        aria = pi * self.raza**2
        return aria

    def diametru(self):
        d = 2 * self.raza
        return d

    def circumferinta(self):
        pi = 3.14
        c = 2 * pi * self.raza
        return c
