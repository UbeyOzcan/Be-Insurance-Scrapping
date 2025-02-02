import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.web import Chrome

class Yuzzu:
    def __init__(self, url: str, license_year: str, birth_date: str, email: str, first_circulation: str, make:str):
        self.license_year = license_year
        self.birth_date = birth_date
        self.email = email
        self.url = url
        self.c = Chrome(self.url)
        self.first_circulation = first_circulation
        self.make = make

    def fill_homepage(self):
        browser = self.c.accept_cookies()
        time.sleep(2)
        license_year = browser.find_element(by=By.CLASS_NAME, value="mask-text")
        license_year.send_keys(self.license_year)
        time.sleep(2)
        birth_date = browser.find_elements(by=By.CLASS_NAME, value="mask-text")
        birth_date[1].send_keys(self.birth_date)
        time.sleep(2)
        email_input = browser.find_element(By.XPATH, '//input[@placeholder="Entrez votre adresse e-mail"]')
        email_input.send_keys(self.email)
        time.sleep(2)

        # Locate and click "Non"
        non_option = browser.find_element(By.XPATH, '//div[text()="Non"]')
        non_option.click()
        time.sleep(2)

        next_page = browser.find_element(By.ID, value='next_section_button')
        next_page.click()
        time.sleep(5)
        return browser

    def fill_vehicle_age_page(self, browser: object, first_owner: bool = True):
        if first_owner:
            first_owner_response = browser.find_element(By.XPATH, '//div[text()="Oui"]')
        else:
            first_owner_response = browser.find_element(By.XPATH, "//div[text()='Non, c'est un véhicule de seconde main']")

        time.sleep(3)
        first_circulation = browser.find_element(by=By.CLASS_NAME, value="mask-text")
        first_circulation.send_keys(self.first_circulation)
        time.sleep(3)
        next_page = browser.find_element(By.ID, value='next_section_button')
        next_page.click()
        time.sleep(3)
        return browser

    def fill_vehicle(self,browser:object):
        try:
            # Wait for the dropdown to be clickable
            dropdown = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "css-1hwfws3"))
            )

            # Click the dropdown to open the options
            dropdown.click()

            # Wait for the options to be visible
            option = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[text()='AUDI']"))
            )

            # Click the desired option
            option.click()
            time.sleep(5)
            print("Selection changed successfully!")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            # Close the browser
            browser.quit()