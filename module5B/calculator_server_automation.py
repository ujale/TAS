import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    desired_caps = {
        "deviceName": "Android Emulator",
        "automationName": "UiAutomator2",
        "platformName": "Android",
        "platformVersion": "12",
        "app": "http://127.0.0.1:9009/Calculator_8.4%20%28503542421%29_Apkpure.apk",
        "noSign": True
    }
    driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_caps)
    time.sleep(5)
    driver.quit()


if __name__ == '__main__':
    main()
