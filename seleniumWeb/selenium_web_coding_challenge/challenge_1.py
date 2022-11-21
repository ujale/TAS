#1. Using    the    chrome    browser    navigate    to https://www.facebook.com/
# fill  in  the  email/phone  and password text box then click the Login Button.
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def facebook_login(driver):
    driver.get("https://www.facebook.com/")
    driver.find_element(By.ID, 'email').send_keys("timby@qa.team")
    driver.find_element(By.NAME, 'pass').send_keys("P@ssw0rd")
    driver.find_element(By.XPATH,
                        '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button').click()
    time.sleep(30)
    assert driver.find_element(By.ID, "email").text == "timby@qa.team"
    #form_element = driver.find_element(By.XPATH, '//form[@data-testid="royal_login_form"]')
    #print(form_element)


def main():
    chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    gecko_driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    facebook_login(chrome_driver)
    facebook_login(gecko_driver)



if __name__ == '__main__':
    main()
