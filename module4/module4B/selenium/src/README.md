## Lesson 1: Intro to selenium with Java
- Selenium webdriver is a web framework for executing cross browser tests and allows users choose any programming language of choice to write the test scripts. 
https://prnt.sc/QXxfmvXOJqaI
- Browser drivers are a standalone server used by selenium webdriver to control the browser. They are like the servants that are used to direct actions on browser

### Steps to setup driver for Chrome
1. Download the chrome driver for your corresponding OS
2. Unzip the downloaded file to extract the chromedriver.exe file and save this in a specific are
3. Copy the path of where the chromedriver.exe file is saved and set the system properties in environemnt variables


## Lesson2: Maven
- Maven is a  project management tool that is based on POM. For mac users with VS code, the maven extension is automatically added when the java extension pack is added as an extension. 
- I launched VS code as a new window and clicked on the Add Java project button, selected the maven option and chose the archetype for quickstart https://prnt.sc/IvphyJrFL_kU
- To add maven to your selenium project go to https://mvnrepository.com/artifact/org.seleniumhq.selenium/selenium-java/4.8.1, click on the stable version with more number of users and copy the artifact
- Go to the pom.xml file and paste the content in a new <dependency> tag.
- On your maven project, click on src-test-org.example and create a new file (java class) called googlenavigate

## Lesson3: DOM
- Document object model

## Lesson 4B: Locator strategy
<a></a> anchor tags contain a link & have a text associated with it that can be fetch by Linkedtext or partial link text locator

## Lesson 5: Xpath Selectors
1. For basic xpath, use the syntax: //TagName[@AttributeName, "AttributeValue"]
eg //input[@type='search']
2. Contains
eg //input[contains(@value, 'Lucky')]
3. Starts with: This is used when the element value is dynamic everytime th page is loaded but the first few letters of the element remains the same while its end changes. Eg facebook first name input field
//input[starts-with(@id, 'u_0_j')]
4. XPATH Axes method: used to find complex or dynamic elements. It appears as parent-child and ancestor-descendant relationships.
eg //Node1/child::*
//Node1/parent::*
//Node1/ancestor::*
//Node1/descedant::*

eg //div[@id='birthday_age']/descedant::div[2]

## Lesson7: Get Details
- Get Attribute: getAttribute("attr");
- Get Text: getText();
-Get Tag name: getTagName();
Get CSS value: getCssValue();

## Lesson 8: Element State
- is Enabled()
- isDisplayed()
- isSelected()

## Lesson 10: iframes
- Elements inside an iframe cannot be accessed directly. You need to switch to iframe to access it by using its name, id or index. 
- When inspected, elements with iframes reflect with an iframe flag on Chropath. The iframe element can be directly inspected by going to the html tag and then type iframe in the search box of chropath. This will show the number of iframes present on that webpage and you can search for he specific element of the iframe you want to drag.
- If the number of iframes present is 1, the index will be 0 and so on.

## Lesson 11: Alert & browser pop up
For Alerts: https://prnt.sc/ydc2kMhjdmi6
- Void dismiss(): used when the cancel button is clicked in the alert box
- Void accept(): used to click on the 'OK' button of the alert
- String getText(): used to capture alert message
- Void sendKeys(String stringToSend): used to send data to the alert box

For Pop-ups
- Driver.getWindowHandles(); // This is used when switching between windows on a browser. i.e multiple browser windows are open
- Driver.getWindowHandle();

## Lesson 13 Select class
- this is used for HTML select tags
EG selectByVisibleText
selectByIndex
selectByValue
deselectAll()

## Lesson 14 Test Synchronization
- 2 types of sync: 
1. unconditional: indicates timeout value & run continues after the period elapses. eg Thread.sleep()
2. conditional: you can specify timeout values & desired conditions eg  implicit & explicit wait
- implicit wait: wait until after a specified time before you throw an exception error
- Explicit wait: wait until specifi conditions are met or max time has elapsed

## Lesson 15: testNG assert
- developed within the lines of JUnit and NUnit
- TestNG covers all forms of tests: unit, functional, end to end, integration etc
- it requires JDK 5 and above
- Provides HTML report, supports parallel testing, helps in grouping//prioritization of tests, generate logs, contains annotations

How to Add testNG dependency?
- Navigate to the maven repository: https://mvnrepository.com/artifact/org.testng/testng 
https://prnt.sc/EEH7C-_D4cY9
https://prnt.sc/C__M32fQBO13
- Copy the testNG dependency and paste it in your project's POM XML
- Rebuild your project to import the necessary files: This is done by reloadng maven

## Lesson 16: testNg assert
2 types of assert: Hard assert and soft assert
- Hard assert: throws an AssetException immediately the assertion fails and the test suite continues with the next @Test
- Soft assert: collects the error in that @Test without throwing an exception error when an assertion fails. We need to create a method to use soft delete.
- If there is any exception and you want to throw it during a soft assert, use assertAll() as the last statement in the @Test

## Lesson 17: Running Test Suite
- TestNG.xml is a configuration file used in organizaing our tests and allows creation & handling of multiple test classes, define test suite, tests.
Steps:
1. Create a testng.xml file in your project folder with whatever name of choice but with the suffix .xml eg TestNg.xml
2. Paste this in the file
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE suite SYSTEM "http://testng.org/testng-1.0.dtd">
<suite name="">
    <test name="">
        <classes>
            <class name=""/>
        </classes>
    </test> <!-- Test -->
</suite> <!-- Suite -->
3. Give a name of choice for the test suite name, test name, while you add the names of the class(es) to be run. The class naming convention is packagename.classname