# Lesson 6: Locator Strategy

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com")
    #blue_element = driver.find_element(By.XPATH, "/html/body/div/main/section[1]/div/div[1]/div[1]/h1")
    #blue_element = driver.find_element(By.TAG_NAME, "h1")
    blue_element = driver.find_element(By.CLASS_NAME, "react-reveal")   # getting a single element
    print("Blue text on page: ", blue_element, blue_element.text)
    links = driver.find_elements(By.TAG_NAME, "a")  # getting multiple elements
    for link in links:
        print("Link element", link.text)


if __name__ == '__main__':
    main()