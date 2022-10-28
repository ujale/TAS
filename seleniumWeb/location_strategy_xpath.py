from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


def locate_by_xpath(driver):
    form = driver.find_element(By.XPATH, "//form[1]")  # We start with // when indicating Xpath elements
    print("Form element by XPATH: ", form)
    form_by_xpath = driver.find_element(By.XPATH,
                                        '//*[@id="__next"]/main/section[1]/div/div[1]/div[2]/form/div[1]/div[1]/input')
    print("Form by copying Xpath: ", form_by_xpath)
    form_by_full_xpath = driver.find_element(By.XPATH, "/html/body/div/main/section[1]/div/div[1]/div[2]/form/div[1]/div[1]/input")
    print("Form by copying full Xpath: ", form_by_full_xpath)



def main():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    locate_by_xpath(driver)
    driver.close()


if __name__ == '__main__':
    main()
