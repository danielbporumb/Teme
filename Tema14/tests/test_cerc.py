import unittest

from Teme.Tema14.app.cerc import Cerc


class TestCerc(unittest.TestCase):

    def setUp(self):
        self.cerc = Cerc(4, "rosu")

    def tearDown(self):
        pass

    def test_descrie(self):
        self.cerc.descriere_cerc()
        self.assertEquals(self.cerc.raza == 4, self.cerc.culoare == "rosu")

    def test_aria(self):
        assert self.cerc.aria() == 50.24

    def test_diametru(self):
        assert self.cerc.diametru() == 8

    def test_circumferinta(self):
        assert self.cerc.circumferinta() == 25.12