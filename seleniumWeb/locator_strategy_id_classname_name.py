# Lesson 6: Locator Strategy (id, classname, name)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def locator_by_id(driver):
    email_element = driver.find_element(By.ID, "email")
    print("Id element for Email field: ", email_element)
    passw_element = driver.find_element(By.ID, "pass")
    print("Id element for Password field: ", passw_element)


def locator_by_class_name(driver):
    rr_first_element = driver.find_element(By.CLASS_NAME, "react-reveal")
    print("React reveal first element: ", rr_first_element)
    rr_elements = driver.find_elements(By.CLASS_NAME, "react-reveal")
    for rr_element in rr_elements:
        print("React reveal element: ", rr_element)



def locator_by_name(driver):
    first_name = driver.find_element(By.NAME, "firstname")
    print("Name element for first name field: ", first_name)
    last_name = driver.find_element(By.NAME, "lastname")
    print("Name element for last name field: ", last_name)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #driver.get("https://www.facebook.com")
    driver.get("https://www.testifyltd.com/contact")
    #locator_by_id(driver)
    locator_by_class_name(driver)
    locator_by_name(driver)


if __name__ == '__main__':
    main()