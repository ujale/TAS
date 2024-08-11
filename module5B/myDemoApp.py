import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    desired_caps = {
        "deviceName": "sdk_gphone64_arm64",
        "automationName":  "UiAutomator2",
        "platformName": "Android",
        "platformVersion": "12",
        "app": "/Users/udemejalekun/Downloads/Android-MyDemoAppRN.1.1.0.build-226.apk",
        "appPackage": "com.saucelabs.mydemoapp.rn",
        "noSign": True
    }
    driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_caps)
    time.sleep(10)
    driver.quit()


if __name__ == '__main__':
    main()