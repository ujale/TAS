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