class Cont:
    iban = None
    titular_cont = None
    sold = None

    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f"Titularul '{self.titular_cont}' are in contul cu IBAN: {self.iban} suma de {self.sold} lei")

    def debitare_cont(self, suma):
        self.sold -= suma
        print(f"Ati retras suma de {suma} lei")

    def creditare_cont(self, suma):
        self.sold += suma
        print(f"Ati depus suma de {suma} lei")

