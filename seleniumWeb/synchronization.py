import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


def element_is_visible(driver):
    web_driver_wait = WebDriverWait(driver, 20)
    web_driver_wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "About us")))
    about_us_link = driver.find_element(By.LINK_TEXT, "About us")
    about_us_link.click()
    time.sleep(5)


def to_be_clickable(driver):
    web_driver_wait = WebDriverWait(driver, 20)
    web_driver_wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Academy")))
    academy_link = driver.find_element(By.LINK_TEXT, "Academy")
    academy_link.click()
    time.sleep(10)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    #to_be_clickable(driver)
    element_is_visible(driver)


if __name__ == '__main__':
    main()
