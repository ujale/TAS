# Task
# Navigate to the website https://academy.testifyltd.com/
# Get the element with the text "© 2022 Testify Limited. All rights reserved."
# Print out the element text, and properties, and it attributes

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def print_element_text_attribute_property(element):
    print("Copyright Element attribute for text: ", element.text)
    print("Copyright Element attribute for ID:", element.get_attribute("id"))
    print("Copyright Element attribute for Class:", element.get_attribute("class"))
    print("Copyright Element attribute for Style:", element.get_attribute("style"))
    print("Copyright Element attribute for Inner Text:", element.get_attribute("innerText"))
    print("Copyright Element attribute for Inner HTML:", element.get_attribute("innerHtml"))
    #print("Copyright Element Value property: ", element.get_property("value`"))


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://academy.testifyltd.com/")
    copyright_element = driver.find_element(By.XPATH, '//*[@id="__next"]/section/div/div[2]/div[2]')
    print_element_text_attribute_property(copyright_element)


if __name__ == '__main__':
    main()
