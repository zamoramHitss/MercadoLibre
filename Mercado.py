#Este código está realizado en Selenium Python, nunca había automatizado, es lo más que logré avanzar; 
#Para la locación no logré encontrar el identificador que me permitiera seleccionarlo, intenté con Link_text, pero no lo localiza.

#Las instrucciones para correrlo únicamente es que tengan chrome y se corra preferentemente en Visual Studio.


from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

url = "https://www.mercadolibre.com"
driver = webdriver.Chrome()
driver.get(url)
source = driver.page_source

elemento = driver.find_element (By.CLASS_NAME, "ml-site-mlm") #Selección país
elemento.click()

barra_busqueda = driver.find_element(By.CLASS_NAME, "nav-search-input") #Busqueda playStation 5
barra_busqueda.send_keys("playstation 5")
barra_busqueda.send_keys(Keys.RETURN)
sleep(3)

actions = ActionChains(driver)
actions.scroll_by_amount(0, 200).perform() 
sleep(3)

element = driver.find_element (By.XPATH, "(//span[@class='ui-search-filter-name'][normalize-space()='Nuevo'])[1]") #FiltroNuevo
element.click()


element = driver.find_element (By.CLASS_NAME, "andes-dropdown__trigger") #Filtro
element.click()

sleep(3)

element = driver.find_element (By.ID, ":R1b56ie:-menu-list-option-price_desc") #FiltroMayor
element.click()

sleep(5)


options = Options()
options.add_argument("detach")
