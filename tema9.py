                        ##### Exercitii obligatorii #####

"""
Implementează o clasă Login care să moștenească unittest.TestCase
Gasește elementele în partea de sus folosind ce selectors dorești:
- setUp()
- Driver
https://the-internet.herokuapp.com/
Click pe Form Authentication
tearDown()
Quit browser
● Test 1
- Verifică dacă noul url e corect
● Test 2
- Verifică dacă page title e corect
● Test 3
- Verifică textul de pe elementul xpath=//h2 e corect
● Test 4
- Verifică dacă butonul de login este displayed
● Test 5
- Verifică dacă atributul href al linkului ‘Elemental Selenium’ e corect
● Test 6
- Lasă goale user și pass
- Click login
- Verifică dacă eroarea e displayed
● Test 7
- Completează cu user și pass invalide
- Click login
- Verifică dacă mesajul de pe eroare e corect
- Este și un x pus acolo extra așa că vom folosi soluția de mai jos:

expected = 'Your username is invalid!'
self.assertTrue(expected in actual, 'Error message text is incorrect')

● Test 8
- Lasă goale user și pass
- Click login
- Apasă x la eroare
- Verifică dacă eroarea a dispărut
● Test 9
- Ia ca o listă toate //label
- Verifică textul ca textul de pe ele să fie cel așteptat (Username și Password)
- Aici e ok să avem 2 asserturi
● Test 10
- Completează cu user și pass valide
- Click login
- Verifică ca noul url CONTINE /secure
- Folosește un explicit wait pentru elementul cu clasa ’flash succes’
- Verifică dacă elementul cu clasa=’flash succes’ este displayed
- Verifică dacă mesajul de pe acest element CONȚINE textul ‘secure area!’
● Test 11
- Completează cu user și pass valide
- Click login
- Click logout
- Verifică dacă ai ajuns pe https://the-internet.herokuapp.com/login
"""
import time
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class Login(TestCase):
    driver = None
    LINK = "https://the-internet.herokuapp.com/"
    BUTON_FORM = (By.LINK_TEXT, "Form Authentication")
    BUTTON_LOGIN = (By.CLASS_NAME, "fa-sign-in")
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SECURE_AREA = (By.XPATH, "//div[@class='flash success']")


    def setUp(self):
        print(f"\nIncepe setUp() pentru metoda {self._testMethodName}")
        self.driver = webdriver.Chrome()
        self.driver.get(self.LINK)
        self.driver.maximize_window()
        button_formular = self.driver.find_element(*self.BUTON_FORM)
        button_formular.click()
        self.driver.implicitly_wait(1)  # am pus implicitly wait pt ca, la testele ce urmeaza, e necesar sa astepte mereu o secunda

    def tearDown(self):
        print(f"Incepe tearDown() pentru metoda {self._testMethodName}")
        self.driver.quit()

    def asteapta(self, locator, timp):
        wait = WebDriverWait(self.driver, timp)
        return wait.until(EC.presence_of_element_located(locator))

    def logare(self):
        self.driver.find_element(*self.BUTTON_LOGIN).click()

# TEST 1 - Verifica daca noul URL este corect

    def test_url(self):
        print(f"A inceput testul {self._testMethodName}")
        expected_url = "https://the-internet.herokuapp.com/login"
        actual_url = self.driver.current_url
        self.assertEqual(expected_url, actual_url), f"Invalid URL, expected {expected_url}, but found {actual_url}"

# TEST 2 - Verifica daca page title e corect

    def test_title(self):
        print(f"A inceput testul {self._testMethodName}")
        expected_title = "The Internet"
        actual_title = self.driver.title
        self.assertEqual(expected_title, actual_title), f"Invalid page Title, expected {expected_title}, but found {actual_title}"

# TEST 3 - Verifica daca textul de pe elementul xpath=//h2 e corect

    def test_h2_text(self):
        print(f"A inceput testul {self._testMethodName}")
        text_h2 = self.driver.find_element(By.XPATH, "//h2").text
        expected_text = "Login Page"
        assert expected_text == text_h2, f"Invalid h2 text, expected {expected_text}, but found {text_h2}"
        # self.assertEqual(expected_text, text_h2), f"Invalid h2 text, expected {expected_text}, but found {text_h2}"
        # am observat ca, folosind assertion methods (assertEqual), nu se afiseaza corect mesajul de eroare

# TEST 4 - Verifica daca butonul de login este displayed

    def test_buton_login_display(self):
        print(f"A inceput testul {self._testMethodName}")
        login_button = self.driver.find_element(*self.BUTTON_LOGIN)
        assert login_button.is_displayed(), "Butonul de Login nu este afisat"

# TEST 5 - Verifică dacă atributul href al linkului ‘Elemental Selenium’ e corect

    def test_atribut_href(self):
        print(f"A inceput testul {self._testMethodName}")
        expected_href = "http://elementalselenium.com/"
        actual_href = self.driver.find_element(By.XPATH, "//a[text()='Elemental Selenium']").get_attribute("href") # luam atributul de tip "href" de pe acel element de tip a
        # assert expected_href == actual_href, f"Invalid href link, expected {expected_href}, but found {actual_href}"
        self.assertEqual(expected_href, actual_href), f"Invalid href link, expected {expected_href}, but found {actual_href}"

# TEST 6 - Lasă goale user și pass; - Click login; - Verifică dacă eroarea e displayed

    def test_blank_login(self):
        print(f"A inceput testul {self._testMethodName}")
        self.logare()
        eroare = self.driver.find_element(By.ID, "flash")
        assert eroare.is_displayed(), "Eroarea nu este afisata dupa logare fara Username/Password"

# TEST 7 - Completează cu user și pass invalide; - Click login; - Verifică dacă mesajul de pe eroare e corect;
# - Este și un x pus acolo extra așa că vom folosi soluția de mai jos
                        # expected = 'Your username is invalid!'
                        # self.assertTrue(expected in actual, 'Error message text is
                        # incorrect')

    def test_wrong_complete(self):
        print(f"A inceput testul {self._testMethodName}")
        username = self.driver.find_element(*self.USERNAME)
        username.send_keys("wrong_user")
        password = self.driver.find_element(*self.PASSWORD)
        password.send_keys("wrongpassword")
        self.logare()
        expected_message = "Your username is invalid!"
        actual_message = self.driver.find_element(By.ID, "flash").text # luam textul; am testat si ia inclusiv *
        self.assertTrue(expected_message in actual_message), "Error message text is incorrect"

# TEST 8 - Lasă goale user și pass;- Click login; - Apasă x la eroare;- Verifică dacă eroarea a dispărut

    def test_eroare_disparuta(self):
        print(f"A inceput testul {self._testMethodName}")
        self.logare()
        self.driver.find_element(By.CLASS_NAME, "close").click()
        eroare = self.driver.find_element(By.ID, "flash")
        self.assertTrue(eroare.is_displayed()), "Mesajul de eroare nu a disparut" # pica testul daca eroarea este inca afisata; daca nu faceam maximize window, dadea eroare, se suprapunea butonul 'x' cu link-ul catre GitHub

# TEST 9 - Ia ca o listă toate //label; - Verifică textul ca textul de pe ele să fie cel așteptat (Username și Password)
# - Aici e ok să avem 2 asserturi

    def test_text_asteptat(self):
        print(f"A inceput testul {self._testMethodName}")
        lista_label = self.driver.find_elements(By.XPATH, "//label")
        # print(lista_label)
        expected_label_text_1 = "Username"
        actual_label_text_1 = lista_label[0].text
        expected_label_text_2 = "Password"
        actual_label_text_2 = lista_label[1].text
        self.assertEqual(expected_label_text_1, actual_label_text_1), f"Textul {expected_label_text_1} nu se regaseste pe label {actual_label_text_1}"
        self.assertEqual(expected_label_text_2, actual_label_text_2), f"Textul {expected_label_text_2} nu se regaseste pe label {actual_label_text_2}"

# TEST 10 - Completează cu user și pass valide; - Click login; - Verifică ca noul url CONTINE /secure; - Folosește un explicit wait pentru elementul cu clasa ’flash succes’
# - Verifică dacă elementul cu clasa=’flash succes’ este displayed; - Verifică dacă mesajul de pe acest element CONȚINE textul ‘secure area!’

    def user_pass_valide(self):
        username = self.driver.find_element(*self.USERNAME)
        username.send_keys("tomsmith")
        password = self.driver.find_element(*self.PASSWORD)
        password.send_keys("SuperSecretPassword!")
        self.logare()

    def test_secure_area(self):
        print(f"A inceput testul {self._testMethodName}")
        self.user_pass_valide()
        actual_url = self.driver.current_url
        self.assertIn("/secure", actual_url), "Noul URL nu contine '/secure'"
        element_flash_success = self.asteapta(self.SECURE_AREA, 5) # ceva nu fac bine la implicitly si explicitly wait? nu functioneaza deloc (stiu ca aici nici nu ar trebui, pt ca il gaseste instant)
        assert element_flash_success.is_displayed(), "Elementul nu este afisat"
        mesaj = self.driver.find_element(*self.SECURE_AREA).text
        # self.assertIn("ion", mesaj), f"Mesajul {mesaj} nu contine textul 'secure area!'"
        self.assertIn("secure area", mesaj), f"Mesajul {mesaj} nu contine textul 'secure area!'"

# TEST 11 - Completează cu user și pass valide; - Click login; - Click logout; - Verifică dacă ai ajuns pe https://the-internet.herokuapp.com/login

    def test_logout(self):
        print(f"A inceput testul {self._testMethodName}")
        self.user_pass_valide()
        logout_button = self.driver.find_element(By.CLASS_NAME, "icon-signout")
        logout_button.click()
        expected_url = "https://the-internet.herokuapp.com/login"
        actual_url = self.driver.current_url
        assert expected_url == actual_url, f"Nu ai ajuns pe {expected_url}, esti pe {actual_url}"


# TEST 12

    def test_brute_force(self):
        element_h4 = self.driver.find_element(By.XPATH, "//h4").text
        potentiale_parole = element_h4.split(" ")
        # print(potentiale_parole)
        for parola in potentiale_parole:
            text_h2 = self.driver.find_element(By.XPATH, "//h2").text
            if text_h2 == 'Login Page':
                username = self.driver.find_element(*self.USERNAME)
                username.send_keys("tomsmith")
                password = self.driver.find_element(*self.PASSWORD)
                password.send_keys(str(parola))
                self.driver.find_element(*self.BUTTON_LOGIN).click()
                # time.sleep(2)
                print("Inca nu am gasit parola")
            # elif text_h2 == 'Secure Area':
            else:
                print(f"Parola secreta este {parola}")
                break

# nu imi afiseaza corect parola, o sa mai incerc..