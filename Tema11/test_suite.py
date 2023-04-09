import unittest
import HtmlTestRunner

from Teme.Tema11.tests.test_login_page import TestLoginPage
from Teme.Tema11.tests.test_secure_page import TestSecurePage


class TestSuite(unittest.TestCase):

    def test_suite(self):

        teste_de_rulat = unittest.TestSuite()

        teste_de_rulat.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestLoginPage),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestSecurePage),
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title="Raport Tema 11",
            report_name="Raport Tema 11"
        )

        runner.run(teste_de_rulat)