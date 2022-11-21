# Using any browser navigate to any Youtube video of your choice,
# allow your script to wait for the comments to load then
# get the first two comments, and print them in the terminal.


import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


def comment_is_visible(driver):
    web_driver_wait = WebDriverWait(driver, 40)
    web_driver_wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'ytd-comment-renderer')))
    comments = driver.find_elements(By.TAG_NAME, "ytd-comment-renderer")
    index = 0
    for comment in comments:
        if index >= 2:
            break
        comment_info = comment.find_element(By.ID, 'content-text')
        print(comment_info.text)
        index += 1
    time.sleep(5)



def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.youtube.com/watch?v=l99fn9OdIvQ")
    comment_is_visible(driver)
    time.sleep(10)





if __name__ == '__main__':
    main()
