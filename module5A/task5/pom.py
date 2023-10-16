import time

from TestAutomationSimplifiedPage import TasPage

from SwitchToSoftwareTestingPage import StstPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    tas_page = TasPage(driver)
    print(tas_page.success_stories_link.text, tas_page.title.text)
    tas_page.enroll_now_button.click()
    time.sleep(5)
    stst_page = StstPage(driver)
    stst_page.got_question_link.click()
    print(stst_page.enroll.text)
    time.sleep(5)


if __name__ == '__main__':
    main()
