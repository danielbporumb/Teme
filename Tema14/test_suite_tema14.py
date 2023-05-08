import unittest

import HtmlTestRunner

from Teme.Tema14.tests.test_angajat import TestAngajat
from Teme.Tema14.tests.test_cerc import TestCerc
from Teme.Tema14.tests.test_cont import TestCont
from Teme.Tema14.tests.test_dreptunghi import TestDreptunghi


class TestSuiteTema14(unittest.TestCase):

    def test_suite(self):
        teste = unittest.TestSuite()
        teste.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestDreptunghi),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestCerc),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestCont),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestAngajat)
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title="Raport Tema 14",
            report_name="Raport Tema 14"
        )

        runner.run(teste)