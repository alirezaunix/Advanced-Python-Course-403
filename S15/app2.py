from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait , Select
from selenium.webdriver.support import expected_conditions as EC
#. /html/body/div[2]/div[1]/fieldset/button

driver = webdriver.Firefox()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

btn_1 = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable(
                (By.XPATH,  '/html/body/div[2]/div[2]/fieldset/a'))
        )
btn_1.click()
