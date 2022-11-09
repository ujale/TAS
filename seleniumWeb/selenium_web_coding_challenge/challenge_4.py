# Navigate to https://www.bbc.com/  and  print  out  the top 10 latest news from the home page.
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def top_news(driver):
    news_title = driver.find_elements(By.CLASS_NAME, 'media-list__item media-list__item--1')
    print("total news headlines on home page: ", news_title)
    #for news_headline in news_headlines:
    #    print("The news headlines are:", news_headline.text)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.bbc.com/")
    time.sleep(5)
    top_news(driver)


if __name__ == '__main__':
    main()


