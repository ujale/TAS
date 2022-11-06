# Lesson 4: Launching a browser
import time

from selenium import webdriver


def main():
    driver = webdriver.Safari(executable_path=r"/usr/bin/safaridriver")
    driver.get("https://www.testifyltd.com/contact")
    driver.maximize_window()
    time.sleep(10)
    driver.close()


main()