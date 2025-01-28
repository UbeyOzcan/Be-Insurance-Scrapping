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
exit()
#filling in the form
first_name = browser.find_element(By.ID, "input-firstname")
first_name.send_keys("FirstName")
last_name = browser.find_element(By.ID, "input-lastname")
last_name.send_keys("LastName")
random_email = str(random.randint(0,99999)) + "@example.com"
email = browser.find_element(By.ID, "input-email")
email.send_keys("your-email8@example.com")


telephone = browser.find_element(By.ID, "input-telephone")
telephone.send_keys("+351999888777")
password = browser.find_element(By.ID, "input-password")
password.send_keys("123456")
password_confirm = browser.find_element(By.ID, "input-confirm")
password_confirm.send_keys("123456")
newsletter = browser.find_element(By.XPATH, value="//label[@for='input-newsletter-yes']")
newsletter.click()
terms = browser.find_element(By.XPATH, value="//label[@for='input-agree']")
terms.click()
continue_button = browser.find_element(By.XPATH, value="//input[@value='Continue']")
continue_button.click()
time.sleep(5)
#asserting that the browser title is correct
assert browser.title == "Your Account Has Been Created!"
time.sleep(5)
#closing the browser
browser.quit()