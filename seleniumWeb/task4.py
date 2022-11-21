
# Task4
# Navigate to the website https://www.facebook.com/
# Find the email box and enter an email value
# Find the password box and enter a password value
# Find the Login button and click it
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.facebook.com/")
    email_input = driver.find_element(By.NAME, 'email')
    email_input.send_keys('ojo@QA.team')
    password_input = driver.find_element(By.NAME, 'pass')
    password_input.send_keys("1234ty")
    login_button = driver.find_element(By.NAME, 'login')
    login_button.click()
    time.sleep(20)
    driver.close()


if __name__ == '__main__':
    main()


