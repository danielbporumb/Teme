import unittest

from Teme.Tema14.app.dreptunghi import Dreptunghi
# from Teme.Tema06.tema06 import Dreptunghi # poate fi importata clasa si direct din Tema06


class TestDreptunghi(unittest.TestCase):

    def setUp(self):
        self.dreptunghi = Dreptunghi(7, 5, "verde")

    def tearDown(self):
        pass

    def test_descrie(self):
        self.dreptunghi.descrie()
        self.assertEquals(self.dreptunghi.lungime == 7, self.dreptunghi.latime == 5, self.dreptunghi.culoare == "verde")

    def test_aria(self):
        assert self.dreptunghi.aria() == 35

    def test_perimetrul(self):
        assert self.dreptunghi.perimetrul() == 24

    def test_schimba_culoarea(self):
        self.dreptunghi.schimba_culoarea("galben")
        assert self.dreptunghi.culoare == "galben"


