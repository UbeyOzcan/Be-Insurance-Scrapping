from selenium.webdriver.common.by import By
from selenium import webdriver
import time


class Chrome:
    def __init__(self, url: str) -> None:
        self.url = url

    def open(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        browser = webdriver.Chrome(chrome_options)
        browser.maximize_window()
        browser.get(self.url)
        return browser

    def accept_cookies(self):
        browser = self.open()
        pop_up = browser.find_element(by=By.ID, value="cmpwelcomebtnyes")
        pop_up.click()
        return browser


