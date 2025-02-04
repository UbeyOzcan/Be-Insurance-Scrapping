from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://react-select.com/home")
driver.maximize_window()
driver.implicitly_wait(20)
driver.find_element(By.XPATH, "//div[@class='select__value-container select__value-container--has-value  css-v68sna-control']").click()
driver.find_element("//*[text()='Green']").click()
time.sleep(3)
