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