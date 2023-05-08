import unittest

from Teme.Tema14.app.angajat import Angajat


class TestAngajat(unittest.TestCase):

    def setUp(self):
        self.angajat = Angajat("Porumb", "Daniel", 2500)

    def tearDown(self):
        pass

    def test_descriere(self):
        self.angajat.descrie()
        self.assertEquals(self.angajat.nume == "Porumb", self.angajat.prenume == "Daniel")

    def test_nume_complet(self):
        assert self.angajat.nume_complet() == "Porumb Daniel"
        # assert self.angajat.nume_complet() == ("Porumb", "Daniel")

    def test_salariu_lunar(self):
        assert self.angajat.salariu_lunar() == 2500

    def test_salariu_anual(self):
        assert self.angajat.salariu_anual() == 30000

    def test_marire_salariu(self):
        self.angajat.marire_salariu(10)
        assert self.angajat.salariu == 2750