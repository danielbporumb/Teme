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
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions as EC


class testing(TestCase):
    driver = None
    LINK = "https://phptravels.net/"
    BUTTON_SEARCH = (By.ID, "flights-search")
    ROUND_TRIP = (By.ID, "round-trip")
    DROPDWON_LIST = (By.ID, "flight_type")
    PLECARE = (By.ID, "autocomplete")
    DESTINATIE = (By.ID, "autocomplete2")
    FLIGHTS_TAB = (By.ID, "flights-tab")

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
        self.driver.find_element(*self.FLIGHTS_TAB).click()
        time.sleep(1)
        self.driver.find_element(*self.BUTTON_SEARCH).click()
        time.sleep(1)
        alert = self.driver.switch_to.alert
        alert.accept()
        round_trip = self.driver.find_element(*self.ROUND_TRIP)
        round_trip.click()
        self.assertTrue(round_trip.is_enabled() ,"Optiunea 'Round Trip' nu este selectata")

    def test_dropdown(self):
        self.driver.find_element(*self.FLIGHTS_TAB).click()
        time.sleep(1)
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


class DragAndDropTest(TestCase):
    driver = None
    LINK = "https://formy-project.herokuapp.com/"
    OBJECT_TO_DRAG = (By.ID, "image")
    LOCATION_TO_DROP = (By.ID, "box")

    def setUp(self):
        self.service = Service(GeckoDriverManager().install())
        self.driver = webdriver.Firefox(service=self.service)
        self.driver.get(self.LINK)
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)

    def tearDown(self):
        self.driver.quit()

    def test_drag_and_drop(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Drag").click()
        time.sleep(1)
        self.driver.refresh() # nu poti sa faci drag and drop decat dupa ce dai un refresh la pagina...
        time.sleep(1)
        action = ActionChains(self.driver)
        element = self.driver.find_element(*self.OBJECT_TO_DRAG)
        location_to_drop = self.driver.find_element(*self.LOCATION_TO_DROP)
        action.drag_and_drop(element, location_to_drop).perform()
        time.sleep(2)
        expected_box_text = "Dropped!"
        actual_box_text = self.driver.find_element(*self.LOCATION_TO_DROP).text

        self.assertEqual(expected_box_text, actual_box_text, "The element was not dropped here")


class Magazine(TestCase):
    driver = None
    LINK = "https://demo.nopcommerce.com/"
    ELECTRONICS_TAB = (By.LINK_TEXT, "Electronics")
    CELL_PHONES_TAB = (By.LINK_TEXT, "Cell phones")
    HTC_ONE_WISHLIST_BUTTON = (By.XPATH, "//a[text()='HTC One Mini Blue']/following::button[text()='Add to wishlist'][1]")
    # luam primul buton de wishlist de dupa link-text-ul HTC One Mini Blue
    WISHLIST_MESSAGE = (By.CLASS_NAME, "success")

    def setUp(self):
        self.service = Service(GeckoDriverManager().install())
        self.driver = webdriver.Firefox(service=self.service)
        self.driver.get(self.LINK)
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)

    def tearDown(self):
        self.driver.quit()

    def test_wishlist(self):
        electronics = self.driver.find_element(*self.ELECTRONICS_TAB)
        action = ActionChains(self.driver)
        action.move_to_element(electronics).perform()
        time.sleep(1)
        wait = WebDriverWait(self.driver, 5)
        cell_phones = wait.until(EC.presence_of_element_located(self.CELL_PHONES_TAB))
        cell_phones.click()
        time.sleep(1)
        self.driver.find_element(*self.HTC_ONE_WISHLIST_BUTTON).click()
        time.sleep(3)
        success_message = wait.until(EC.presence_of_element_located(self.WISHLIST_MESSAGE))
        expected_wishlist_message = "The product has been added to your wishlist"
        actual_wishlist_message = success_message.text

        self.assertEqual(expected_wishlist_message, actual_wishlist_message, "The is not on your wishlist")




