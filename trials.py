
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

PATH = "//Users/paula/Desktop/selenium/selenium/chromedriver"


serv_obj = Service(PATH)
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://profile.intra.42.fr")
attr = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/div/div[1]/img").tag_name
res = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/div/div[1]/img").rect
driver.find_element(By.ID, "user_login").send_keys("proche-c")
value = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/div/div[3]/form/div[1]/div[1]/input").get_attribute("value")
text = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/div/div[3]/a[1]").text
print("*******")
print("attr is:", attr)
print("*******")
print("res is:", res)
print("*******")
print("value is:", value)
print("*******")
print("text is:", text)
driver.quit()

