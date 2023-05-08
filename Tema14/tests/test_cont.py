import unittest

from Teme.Tema14.app.cont import Cont


class TestCont(unittest.TestCase):

    def setUp(self):
        self.cont = Cont(12344321, "Daniel Porumb", 200)

    def tearDown(self):
        pass

    def test_afisare_sold(self):
        self.cont.afisare_sold()
        self.assertEquals(self.cont.iban == 12344321, self.cont.titular_cont == "Daniel Porumb", self.cont.sold == 200)

    def test_debitare_cont(self):
        self.cont.debitare_cont(50)
        assert self.cont.sold == 150

    def test_creditare_cont(self):
        self.cont.creditare_cont(100)
        assert self.cont.sold == 300