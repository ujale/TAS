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
    time.sleep(10)
    wiki_text = driver.find_element(By.XPATH, '/html/body/div[7]/div/div[11]/div[2]/div/div/div[2]/div/div[5]/div/div/div/div/div[1]/div/div/div/div/div/div/div[1]/div/div/div')
    print("Wikipedia text on python search: ", wiki_text.text)
    time.sleep(5)
    driver.close()


if __name__ == '__main__':
    main()
