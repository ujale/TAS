from selenium import webdriver
from selenium.webdriver.common.by import (By)
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


def locate_by_link_text(driver):
    academy_link = driver.find_element(By.LINK_TEXT, "Academy")
    print("Academy link: ", academy_link)
    hire_link = driver.find_element(By.LINK_TEXT, "Hire")
    print("Hire link: ", hire_link)


def locate_by_partial_link_text(driver):
    academy_partial_link = driver.find_element(By.PARTIAL_LINK_TEXT, "adem")
    print("Academy partial link: ", academy_partial_link)
    test_links = driver.find_elements(By.PARTIAL_LINK_TEXT, "Test")
    print("Test link size: ", len(test_links))
    for test_link in test_links:
        print("learn_more_link: ", test_link)


def main():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    #locate_by_link_text(driver)
    locate_by_partial_link_text(driver)
    driver.close()


if __name__ == '__main__':
    main()
