# Navigate any browser to https://weather.com/ get the current  temperature  and
# print  it  out  in  the  terminal.
# Then print out the temperature for Morning, Afternoon, Evening,and Overnight.
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://weather.com/")
    temp = driver.find_element(By.XPATH, '//*[@id="WxuCurrentConditions-main-b3094163-ef75-4558-8d9a-e35e6b9b1034"]/div/section/div/div[2]/div[1]/div[1]/span')
    print("Current Temperature: ", temp.text)
    morning = driver.find_element(By.XPATH, '//*[@id="WxuTodayWeatherCard-main-486ce56c-74e0-4152-bd76-7aea8e98520a"]/section/div/ul/li[1]/a/div[1]/span')
    print("Morning temperature is :", morning.text)
    afternoon = driver.find_element(By.CSS_SELECTOR, '#WxuTodayWeatherCard-main-486ce56c-74e0-4152-bd76-7aea8e98520a > section > div > ul > li.Column--column--1p659.Column--active--3vpgg > a > div.Column--temp--5hqI_ > span')
    print("Afternoon temperature is :", afternoon.text)
    evening = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/main/div[3]/section/div/ul/li[3]/a/div[1]/span')
    print("Evening temperature is :", evening.text)
    overnight = driver.find_element(By.XPATH, '//*[@id="WxuTodayWeatherCard-main-486ce56c-74e0-4152-bd76-7aea8e98520a"]/section/div/ul/li[3]/a/div[1]/span')
    print("Overnight temperature is :", overnight.text)
    time.sleep(10)


if __name__ == '__main__':
    main()
