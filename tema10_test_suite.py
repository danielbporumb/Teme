##### Exercitii obligatorii #####

"""
1. Faceti o suita care sa contina testele voastre de la tema 9 + testele de la
intalnirea 10 (care au clasa). Generati raportul
"""
import unittest
import HtmlTestRunner

from Cursuri.curs10_test_01_alerts import TestAlerts
from Cursuri.curs10_test_02_authentication import TestFirefoxAuthentication
from Cursuri.curs10_test_03_context_menu import TestContextMenu
from Cursuri.curs10_test_04_keys import TestKeys
from Cursuri.curs10_test_05_dropdown import TestDropdown
from Teme.tema9 import Login


class TestSuiteTeme(unittest.TestCase):

    def test_suite(self):
        teste = unittest.TestSuite()
        teste.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Login),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestAlerts),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestFirefoxAuthentication),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestContextMenu),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestKeys),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestDropdown)
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title="Raport Tema 10",
            report_name="Raport Tema 9 si Curs 10"
        )

        runner.run(teste)