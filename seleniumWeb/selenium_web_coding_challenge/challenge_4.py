# Navigate to https://www.bbc.com/  and  print  out  the top 10 latest news from the home page.
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def top_news(driver):
    news_headline = driver.find_elements(By.CLASS_NAME, 'media__link')
    #for news in news_headline:
    #    print("This prints all the news headlines are:", news.text)
    index = 0
    while index < 10:
        print(news_headline[index].text)
        index += 1





def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.bbc.com/")
    time.sleep(5)
    top_news(driver)


if __name__ == '__main__':
    main()


