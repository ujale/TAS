import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    form = driver.find_element(By.TAG_NAME, "form")
    print("Form states: ", form.is_displayed(), form.is_enabled())
    if form.is_displayed():
        print("Clicking form")
        form.click()
    submit_button = driver.find_element(By.TAG_NAME, "button")
    print("Submit button states: ", submit_button.is_displayed(), submit_button.is_enabled())
    if submit_button.is_displayed():
        print("Clicking button")
        submit_button.click()
    time.sleep(5)


if __name__ == '__main__':
    main()
