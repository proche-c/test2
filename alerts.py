from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


PATH = "//Users/paula/Desktop/selenium/selenium/chromedriver"


serv_obj = Service(PATH)
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
driver.switch_to.window("snigel-cmp-framework")
driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div[3]/div[2]/div[2]]").click()
#primero cambiamos de frame:
driver.switch_to.frame("iframeResult")
driver.find_element(By.XPATH, "/html/body/button").click()
WebDriverWait(driver, 2)
#Cambiamos a la alerta y aceptamos
driver.switch_to.alert.accept()
WebDriverWait(driver, 2)
#Si queremos cancelar la alerta
#driver.switch_to.alert.dismiss()
#WebDriverWait(driver, 2)