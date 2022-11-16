# Using    the    firefox    browser    navigate    to https://www.google.com/
# enter  the  text  Python  in  the search  box,  then  send  the  Enter  key.
# Get  the  text  from  the Wikipedia  brief  on  the  right  side  and  print  the  value  in  the console.
import time

from selenium import webdriver
from selenium.webdriver.common.by import (By)
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


def main():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get("https://www.google.com/")
    driver.maximize_window()
    search_field = driver.find_element(By.NAME, "q")
    search_field.send_keys("Python")
    search_field.submit()
    wiki_text = driver.find_element(By.CSS_SELECTOR, '.kno-rdesc > span:nth-child(2)')
    #print("Wikipedia text on python search: ", wiki_text.text)
    #right_pane = driver.find_element(By.XPATH, '//*[@id="rhs"]')
    print("Wikipedia text on python search: ", wiki_text.text)
    time.sleep(5)
    driver.quit()


if __name__ == '__main__':
    main()
