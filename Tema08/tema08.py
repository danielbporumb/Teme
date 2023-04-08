                    ##### Exercitii obligatorii #####

"""
Alege-ți unuul sau mai multe din sugestiile de site-uri de mai jos
- https://www.phptravels.net/
- http://automationpractice.com/index.php
- https://formy-project.herokuapp.com/
- https://the-internet.herokuapp.com/
- https://www.techlistic.com/p/selenium-practice-form.html
- jules.app
Alege câte 3 elemente din fiecare tip de selector din următoarele categorii:
● Id
● Link text
● Parțial link text
● Name
● Tag*
● Class name*
● Css (1 după id, 1 după clasă, 1 după atribut=valoare_partiala)
observație:
- Probabil nu vei găsi un singur website care să cuprindă toate variantele de mai sus, astfel că îți recomandăm să 
folosești mai multe site-uri
- Opțional: La tag și class name vei folosi find elementS! - salvează în listă.
Interactionează cu un element la alegere din listă.
Pentru xpath identifică elemente după criteriile de mai jos:
● 3 după atribut valoare
● 3 după textul de pe element
● 1 după parțial text
● 1 cu SAU, folosind pipe |
● 1 cu *
● 1 în care le iei ca pe o listă de xpath și în python ajunge 1 element, deci
cu (xpath)[1]
● 1 în care să folosești parent::
● 1 în care să folosești fratele anterior sau de după (la alegere)
● 1 funcție ca și cea de la clasă prin care să pot alege eu prin parametru cu ce element vreau să interacționez.
"""


from selenium import webdriver
import time
from selenium.webdriver.common.by import By

LINK1 = "https://www.phptravels.net/"
LINK2 = "http://automationpractice.com/index.php"
LINK3 = "https://formy-project.herokuapp.com/"
LINK4 = "https://the-internet.herokuapp.com/"
LINK5 = "https://www.techlistic.com/p/selenium-practice-form.html"



###################### PARTIAL LINK TEXT ######################
driver4 = webdriver.Chrome()
driver4.get(LINK4)
driver4.maximize_window()
time.sleep(2)

element_by_PARTIAL_LINK_TEXT1 = driver4.find_element(By.PARTIAL_LINK_TEXT, "Drop").click()
time.sleep(1)
driver4.back()
time.sleep(1)
element_by_PARTIAL_LINK_TEXT2 = driver4.find_element(By.PARTIAL_LINK_TEXT, "Forgot").click()
time.sleep(1)
driver4.back()
time.sleep(1)
element_by_PARTIAL_LINK_TEXT3 = driver4.find_element(By.PARTIAL_LINK_TEXT, "Messages").click()
time.sleep(1)
driver4.back()
time.sleep(1)

###################### LINK TEXT ######################

element_by_LINK_TEXT1 = driver4.find_element(By.LINK_TEXT, "Dropdown").click()
time.sleep(1)
driver4.back()
time.sleep(1)
element_by_LINK_TEXT2 = driver4.find_element(By.LINK_TEXT, "Entry Ad").click()
time.sleep(1)
driver4.back()
time.sleep(1)
element_by_LINK_TEXT3 = driver4.find_element(By.LINK_TEXT, "Floating Menu").click()
time.sleep(1)
driver4.back()
time.sleep(1)

driver4.quit()

###################### ID ######################

driver3 = webdriver.Chrome()
driver3.get(LINK3)
driver3.maximize_window()
time.sleep(2)
driver3.find_element(By.LINK_TEXT, "Modal").click()
time.sleep(1)

element_by_ID1 = driver3.find_element(By.ID, "modal-button").click()
time.sleep(1)
element_by_ID2 = driver3.find_element(By.ID, "ok-button").click()
time.sleep(2)
element_by_ID3 = driver3.find_element(By.ID, "close-button").click()
time.sleep(2)

driver3.quit()

###################### NAME ######################

driver1 = webdriver.Chrome()
driver1.get(LINK1)
driver1.maximize_window()
time.sleep(2)
driver1.find_element(By.XPATH, "//span[text()='flights']").click()
time.sleep(1)

element_by_NAME1 = driver1.find_element(By.NAME, "trip").click() # sunt doua elemente cu name-ul 'trip', in acest caz da click pe primul
time.sleep(2)
element_by_NAME2 = driver1.find_element(By.NAME, "from").send_keys("Cluj-Napoca")
time.sleep(1)
driver1.find_element(By.CLASS_NAME, "autocomplete-location").click() # dam click si pe sugestia aparuta din formular
time.sleep(2)
element_by_NAME3 = driver1.find_element(By.NAME, "to").send_keys("Timisoara")
time.sleep(1)
driver1.find_element(By.CLASS_NAME, "autocomplete-location").click() # dam click si pe sugestia aparuta din formular
time.sleep(2)

driver1.quit()

###################### TAG ######################

driver3 = webdriver.Chrome()
driver3.get(LINK3)
driver3.maximize_window()
time.sleep(2)

driver3.find_element(By.LINK_TEXT, "Buttons").click()
time.sleep(1)
lista_butoane = list()
butoane = driver3.find_elements(By.TAG_NAME, "button")
for buton in butoane:
    lista_butoane.append(buton)
print(f"Lista cu ({len(lista_butoane)}) butoane : {str(lista_butoane)}")

driver3.back()
time.sleep(1)

driver3.find_element(By.LINK_TEXT, "Checkbox").click()
time.sleep(1)
lista_checkbox = list()
checkbox = driver3.find_elements(By.TAG_NAME, "input")
for bifa in checkbox:
    lista_checkbox.append(bifa)
    bifa.click() # le si bifam
    time.sleep(1)
# lista_checkbox[1].click()  # sau putem bifa doar unul din ele
# time.sleep(1)
print(f"Lista cu ({len(lista_checkbox)}) checkbox-uri : {lista_checkbox})")

driver3.back()
time.sleep(1)

driver3.find_element(By.LINK_TEXT, "Dropdown").click()
time.sleep(1)
driver3.find_element(By.ID, "dropdownMenuButton").click()
time.sleep(1)
lista_dropdown = list()
elemente = driver3.find_elements(By.TAG_NAME, "a")
for element in elemente:
    lista_dropdown.append(element)
print(f"Lista cu ({len(lista_dropdown)}) elemente dropdown : {lista_dropdown})")
# o sa fie 32 de elemente, deoarece pe acea pagina sunt 2 liste dropdown a cate 15 elemente fiecare + inca o lista dropdown cu 2 elemente

driver3.quit()

###################### CLASS NAME ######################

driver5 = webdriver.Chrome()
driver5.get(LINK5)
driver5.maximize_window()
time.sleep(2)

elemente_by_CLASS_NAME1 = driver5.find_elements(By.CLASS_NAME, "control-group")
print(f"Lista 1 cu ({len(elemente_by_CLASS_NAME1)}) elemente cu clasa 'control-group': {elemente_by_CLASS_NAME1}")
time.sleep(2)

driver5.quit()

driver3 = webdriver.Chrome()
driver3.get(LINK3)
driver3.maximize_window()
time.sleep(2)

driver3.find_element(By.PARTIAL_LINK_TEXT, "Radio").click()
time.sleep(1)
elemente_by_CLASS_NAME2 = driver3.find_elements(By.CLASS_NAME, 'form-check')
print(f"Lista 2 cu ({len(elemente_by_CLASS_NAME2)}) elemente cu clasa 'form-check-input' : {elemente_by_CLASS_NAME2}")
time.sleep(2)

###################### CSS dupa ID ######################

driver3.back()
time.sleep(1)
driver3.find_element(By.PARTIAL_LINK_TEXT, "disabled").click()
time.sleep(1)
element_CSS_by_ID = driver3.find_element(By.CSS_SELECTOR, "input#input").send_keys("Salut")
time.sleep(1)

###################### CSS dupa CLASA ######################
driver3.back()
time.sleep(1)
driver3.find_element(By.PARTIAL_LINK_TEXT, "Mouse").click()
time.sleep(1)
element_CSS_by_CLASS = driver3.find_element(By.CSS_SELECTOR, "input.form-control").send_keys("Danel Porumb")
time.sleep(1)

###################### CSS dupa atribut=valoare_partiala ######################

driver3.back()
time.sleep(1)
driver3.find_element(By.LINK_TEXT, "Autocomplete").click()
time.sleep(1)
element_CSS_atribut_valoare_partiala = driver3.find_element(By.CSS_SELECTOR, "input[placeholder*='code']")
element_CSS_atribut_valoare_partiala.send_keys("455200")
time.sleep(1)


###################### XPATH ######################

element_XPATH_atribut_valoare1 = driver3.find_element(By.XPATH, "//input[@id='street_number']").send_keys("Taietura Turcului")
time.sleep(1)
element_XPATH_atribut_valoare2 = driver3.find_element(By.XPATH, "//input[@id='route']").send_keys("47/11")
time.sleep(1)
element_XPATH_atribut_valoare3 = driver3.find_element(By.XPATH, "//input[@type='text' and @id='locality']").send_keys("Cluj-Napoca")
time.sleep(1)

element_XPATH_text_element1 = driver3.find_element(By.XPATH, "//input[@placeholder='State']").send_keys("Cluj")
time.sleep(1)
element_CSS_atribut_valoare_partiala.clear() # il sterg pt ca deja l-am completat mai sus cu CSS
time.sleep(1)
element_XPATH_text_element2 = driver3.find_element(By.XPATH, "//input[@placeholder='Zip code']").send_keys("400221")
time.sleep(1)
element_XPATH_text_element3 = driver3.find_element(By.XPATH, "//input[@placeholder='Country']").send_keys("Romania")
time.sleep(1)

element_XPATH_partial_text = driver3.find_element(By.XPATH, "//input[contains(@class,'pac')]").send_keys("Adresa completa")
time.sleep(1)

driver3.back()
time.sleep(1)
driver3.find_element(By.LINK_TEXT, "Complete Web Form").click()
time.sleep(1)
element_XPATH_cu_pipe = driver3.find_element(By.XPATH, "//input[@id='first-name'] | //input[@placeholder='Enter first name']").send_keys("Porumb")
time.sleep(1)
element_XPATH_unic = driver3.find_element(By.XPATH, "//*[@id='last-name']").send_keys("Daniel")
time.sleep(1)
element_XPATH_lista = driver3.find_element(By.XPATH, "//div[3]/input[1][@class='form-control']").send_keys("Inginer")
time.sleep(1)
element_XPATH_frate_anterior = driver3.find_element(By.XPATH, "//input[@id='radio-button-1']/following::input[@id='radio-button-2']").click() # fratele butonului 1
time.sleep(1)
element_XPATH_parent = driver3.find_element(By.XPATH, "//option[@value='0']/parent::*")
element_XPATH_parent.click() # dam doar click pe acel form-control
time.sleep(1)


def selecteaza_experienta(ani_experienta):
    if 0 <= ani_experienta <= 1:
        element_XPATH_parent.find_element(By.XPATH, "//option[@value='1']").click()
    elif 2 <= ani_experienta <= 4:
        element_XPATH_parent.find_element(By.XPATH, "//option[@value='2']").click()
    elif 5 <= ani_experienta <= 9:
        element_XPATH_parent.find_element(By.XPATH, "//option[@value='3']").click()
    else:
        element_XPATH_parent.find_element(By.XPATH, "//option[@value='4']").click()

selecteaza_experienta(4)
time.sleep(3)