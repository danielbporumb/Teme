##### Exercitii obligatorii #####

"""
2. Ganditi voi o clasa de test din paginile sugerate in tema 8
- Scrieti cel putin 3 functii de test intr-o clasa (cum am facut la clasa)
Folositi firefox in loc de chrome (ce doriti voi, cate functii de test doriti,
freestyle ca sa incepeti sa ganditi si singuri niste scenarii de test).
"""
import time
from unittest import TestCase

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager



class testing(TestCase):
    driver = None
    LINK = "https://phptravels.net/"
    BUTTON_SEARCH = (By.ID, "flights-search")
    ROUND_TRIP = (By.ID, "round-trip")
    DROPDWON_LIST = (By.ID, "flight_type")
    PLECARE = (By.ID, "autocomplete")
    DESTINATIE = (By.ID, "autocomplete2")

    def setUp(self):
        self.service = Service(GeckoDriverManager().install())
        self.driver = webdriver.Firefox(service=self.service)
        self.driver.get(self.LINK)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    def test_url_title(self):
        expected_url = "https://phptravels.net/"
        actual_url = self.driver.current_url
        expected_title = "PHPTRAVELS | Travel Technology Partner - PHPTRAVELS"
        actual_title = self.driver.title
        self.assertEqual(expected_url, actual_url, "URL-ul nu coincide")
        self.assertEqual(expected_title, actual_title, "Titlul nu coincide")

    def test_empty_search(self):
        self.driver.find_element(*self.BUTTON_SEARCH).click()
        alert = self.driver.switch_to.alert
        alert.accept()
        round_trip = self.driver.find_element(*self.ROUND_TRIP)
        round_trip.click()
        self.assertTrue(round_trip.is_enabled() ,"Optiunea 'Round Trip' nu este selectata")

    def test_dropdown(self):
        options = self.driver.find_element(*self.DROPDWON_LIST)
        select = Select(options)
        select.select_by_visible_text("Business")
        time.sleep(1)
        optiune_selectata = select.first_selected_option.text
        time.sleep(1)
        self.assertEqual(optiune_selectata, "Business", "Nu a fost selectata optiunea 'Business'")



class TestSlider(TestCase):
    driver = None
    LINK = "https://the-internet.herokuapp.com/horizontal_slider"
    SLIDER = (By.XPATH, "//input[@type='range']")

    def setUp(self):
        self.service = Service(GeckoDriverManager().install())
        self.driver = webdriver.Firefox(service=self.service)
        self.driver.get(self.LINK)
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)

    def tearDown(self):
        self.driver.quit()

    def test_slider_value(self):
        slider = self.driver.find_element(*self.SLIDER)
        # print(slider.location)
        action = ActionChains(self.driver)
        action.click_and_hold(slider).move_by_offset(50, 0).release().perform()
        time.sleep(2)
        expected_value = "4"
        actual_value = self.driver.find_element(By.ID, "range")
        # print(actual_value.location)

        self.assertEqual(expected_value, actual_value.text, "Valorile nu corespund")

# nu gasesc ce teste sa mai fac pe site-urile astea, astfel incat sa nu repet ce am facut la cursuri sau teme anterioare..
# o sa mai completez ulterior cu ceva teste

    # def test_drag_and_drop(self):
    #     self.driver.find_element(By.LINK_TEXT, "Drag and Drop").click()
    #     patrat_A =  self.driver.find_element(By.ID, "column-a")
    #     text_A = patrat_A.text
    #     print(f"\nTextul initial de pe primul patrat este '{text_A}'")
    #     patrat_B =  self.driver.find_element(By.ID, "column-b")
    #     text_B = patrat_B.text
    #     print(f"Textul initial de pe al doilea patrat este '{text_B}'")
    #     actions = ActionChains(self.driver)
    #     actions.drag_and_drop(patrat_A, patrat_B).perform()
    #     time.sleep(1)
    #
    #     self.assertEqual(text_A, "B", "Nu s-a facut 'drag and drop', textul nu e cel asteptat")
    #     self.assertEqual(text_B, "A", "Nu s-a facut 'drag and drop', textul nu e cel asteptat")


# m-am tot chinuit o vreme cu o astfel de metoda de test, insa nu functioneaza nicicum drag_and_drop.. am incercat prin n variante