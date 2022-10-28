# Lesson 1: Browser Automation
Examples of browser automation tools:
Selenium, Puppeteer, Cypress, Axiom, Node Crawler, Requests, Capybara

## Setting up selenium in your python project
- Open terminal and enter the following command: 
pip install selenium or pip3 install selenium

# Lessons 2 & 3: Selenium and webdrivers
Selenium is an open source project with libraries & tools for web automation. It is available in almost all PL: nodejs(Javascript), groovy, python, PHP, C#, Java, perl, scala, ruby and it supports almost all OS: windows, linux, macos

A webdriver is an interface that allows the user to execute commands and test over browser. Each browser has its own webdriver, firefox- gecko driver, chrome- chrome driver etc
Ensure you download the webdriver that corresponds to the version of your browser

- For Chrome: https://chromedriver.chromium.org/downloads
- For Firefox: https://github.com/mozilla/geckodriver/releases
- For Edge: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
- For Safari: follow the instructions here https://webkit.org/blog/6900/

Alternatively, you can install chrome webdriver from the python library using the command:
pip install chromedriver-autoinstaller

Once the above command is complete you can import the library in your python project by using:
import chromedriver_autoinstaller

# Lesson 4: Launching browser from python using selenium
- Have a webdriver installed on your system
- Import selenium library into my python code
- Set executable path of the driver

Create a py test file eg launch_website on your IDE and enter the following:

from selenium import webdriver

def main():
    driver = webdriver.Chrome(executable_path=r"<path of the chrome driver on your machine>")
    driver.get("https://www.google.com")
    driver.close()


main()

Repeat same for other browser, changing Chrome in the above to Firefox or Edge

# Lesson 5: Auto setting webdrivers

The problem of having to download webdrivers for different browsers on different OS and calling their respective path is what auto setting webdrivers using webdriver manager solves.
With the lastest version of selenium, browser drivers can be managed by users. This is done using the command to install the webdriver manager package. This feature means we no longer have to download webdrivers on our system as the webdriver manager is responsible for downloading it at the first time the test is run.

This is the command to install webdriver manager in terminal
- pip3 install webdriver-manager 

- syntax for test using auto set webdrivers is given below:

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.google.com")


if __name__ == '__main__':
    main()

# Lesson 6: Locator Strategy

Types of locators are:
1. Name
2. Id
3. Class
4. Tag Name
5. Css Selector
6. XPath
7. Link Text
8. Partial Link Text
