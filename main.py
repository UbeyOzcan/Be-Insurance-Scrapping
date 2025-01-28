import random
import time
from selenium.webdriver.common.by import By
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

browser = webdriver.Chrome(chrome_options)
browser.maximize_window()
browser.get("https://www.yuzzu.be/fr/assurance-auto/simulation")
pop_up = browser.find_element(by= By.ID, value="cmpwelcomebtnyes")
pop_up.click()
print("cookies accepted ! ")
time.sleep(3)
# Page 1
license_year = browser.find_element(by= By.CLASS_NAME, value="mask-text")
license_year.send_keys("2013")
time.sleep(3)
birth_date = browser.find_elements(by= By.CLASS_NAME, value="mask-text")
birth_date[1].send_keys("17071995")
time.sleep(5)
email_input = browser.find_element(By.XPATH, '//input[@placeholder="Entrez votre adresse e-mail"]')
email_input.send_keys('test@example.com')
time.sleep(5)

# Locate and click "Non"
non_option = browser.find_element(By.XPATH, '//div[text()="Non"]')
non_option.click()
time.sleep(5)
exit()



