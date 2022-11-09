#1.    Using    the    chrome    browser    navigate    to https://www.facebook.com/
# fill  in  the  email/phone  and password text box then click the Login Button.
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.facebook.com/")
    driver.find_element(By.ID, 'email').send_keys("timby@qa.team")
    driver.find_element(By.NAME, 'pass').send_keys("P@ssw0rd")
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button').click()
    time.sleep(10)


if __name__ == '__main__':
    main()
