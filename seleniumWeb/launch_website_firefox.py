# Lesson 4: Launching a browser
from selenium import webdriver


def main():
    driver = webdriver.Firefox(executable_path=r"/Users/udemejalekun/Downloads/geckodriver")
    driver.get("https://www.google.com")
    driver.close()


main()