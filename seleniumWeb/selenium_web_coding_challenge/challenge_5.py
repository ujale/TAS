#Using any browser navigate to any Youtube video of your choice,
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
    web_driver_wait = WebDriverWait(driver, 20)
    web_driver_wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-comments/ytd-item-section-renderer')))
    first_comment = driver.find_element(By.XPATH, '//*[@id="main"]')
    first_comment_text = first_comment.find_element(By.XPATH, '//*[@id="comment-content"]')
    print("First comment", first_comment_text.text)
    time.sleep(5)


#def send_keys_element(element, keys):
#    element.send_keys(keys)

def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.youtube.com")
    driver.find_element(By.ID, "search-input").click()
    driver.find_element(By.XPATH, '//*[@id="video-title"]').click()
    #send_keys_element(driver.find_element(By.ID, "search-input"), "Adonai Nathaniel Bassey")
    comment_is_visible(driver)
    time.sleep(20)





if __name__ == '__main__':
    main()