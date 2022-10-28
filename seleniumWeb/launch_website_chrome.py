# Lesson 4: Launching a browser
from selenium import webdriver


def main():
    driver = webdriver.Chrome(executable_path=r"/Users/udemejalekun/Downloads/chromedriver")
    driver.get("https://www.google.com")
    driver.close()


main()