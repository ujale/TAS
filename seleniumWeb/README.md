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
5. Css Selector: This is advisable for use when there is no ID or class name for the the element or where the ID or class name changes with each load i.e dynamic. 
6. XPath: This is advisable for use when there is no ID or class name for the the element or where the ID or class name changes with each load i.e dynamic. We can use either the Xpath or Full Xpath when rightclick and copy them from the website's dev tools element page
7. Link Text: These usually contain the 'a' tag in them and href i.e <a >. What we copy is the content of the link
8. Partial Link Text

# Lesson 14: Difference between Element Attribute & Element Property

Element attribute is static eg anchor tag, href of linked text etc, while element property refers to the computed property that can be dynamic eg checkbox (can be checked on unchecked), value, input fields etc.

Selenium uses the get_property() method to inspect the element property

# Lesson 15: Sending Key Event
This is done using the send_keys() method. In the lesson i wrote 2 ways of sending keys: directly or by using another method instead of main method

# Lesson 16: Sending mouse events
This is done using the click() method

# Lesson 17: Action Chains
These are used to automate low level interactions such as mouse movement, move button actions, key press, scrolling, highlighting text, right-click event, copy & paste event, element dragging etc.
To use action chains, first you import the package from selenium webdriver by including <from selenium.webdriver import ActionChains>
Next, initialize the actions object with the webdriver 
i.e actions = ActionChains(driver)

scroll by offset is used to similate trackpad option of scrollimg on mouse. it uses y delta values.A negative value for the delta y means to scroll up. 
scroll to element is similae to scroll by offset in function but uses an element locator instead of y delta value

The default xter limit in the highlighting is 15.

# Lesson 18: Element Visibility
This involves checking if the element is present on the web page or if it can recieve events from selenium. The following methods are used to get element visibility & state:
is_displayed
is_enabled
is_selected

# Lesson 19: Navigation
Events like moving forward, backward, refresh, maximize & minimize window
The commands are driver.maximize_window(), driver.refresh, driver.back, driver.forward

# Lesson 20: Synchronization
Explicit wait = This is a method in selenium that allows you wait until an element is visible or ready to recieve an event using WebDriverWait and ExpectedCondition class.
to use explicit wait, import both webdriverwait & expectedcondition:

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

The following are EC methods that can be used:
element_to_be_clicked
visibility_of_element_located
element_to_be_selected
element_attribute_to_include

Alternatively, you can use the time package in python to wait for X secs before performing an event = implicit wait
Its advised to refrain from use of time.sleep() (which is python's time package)
