# Task2
# Visit the website https://academy.testifyltd.com/
# Locate the button with the text "Explore Courses" and print out the element
# Locate the element with the text "Subscribe to receive training updates from Testify" and print it.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def locate_explore_courses(driver):
    explore_course_link = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[1]/div/div/div[1]/div/button')
    print("The explore course button's link by Xpath: ", explore_course_link)


def locate_link_text(driver):
    subscribe_text_link = driver.find_element(By.CLASS_NAME, "react-reveal")
    print("The subscribe text link by class name: ", subscribe_text_link)


def locate_partial_link_text(driver):
    pass


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://academy.testifyltd.com/")
    locate_explore_courses(driver)
    locate_link_text(driver)
    driver.close()


if __name__ == '__main__':
    main()
