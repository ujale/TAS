import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def send_keys_element(element, *keys):  # the asterick infront of keus means multiple keys can be passed
    element.send_keys(keys)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    first_name_input = driver.find_element(By.NAME, "firstname")  # option 1: find the element then pass keys
    first_name_input.send_keys("Ud")
    time.sleep(2)
    last_name_input = driver.find_element(By.NAME, "lastname")
    last_name_input.send_keys("Jale")
    email_input = driver.find_element(By.NAME, "email")
    email_input.send_keys("udeme@yopmail.")
    phone_input = driver.find_element(By.NAME, "phone")
    # phone_input.send_keys("090")
    time.sleep(5)

    # option 2: use a method def send_keys_element to pass the keys
    send_keys_element(driver.find_element(By.NAME, "firstname"), "eme")
    send_keys_element(driver.find_element(By.NAME, "lastname"), "kun")
    send_keys_element(driver.find_element(By.NAME, "email"), "com")
    # send_keys_element(driver.find_element(By.NAME, "phone"), "6")
    send_keys_element(driver.find_element(By.NAME, "phone"), Keys.CONTROL, "v")  # this represents control+v i.e paste
    time.sleep(10)


if __name__ == '__main__':
    main()
