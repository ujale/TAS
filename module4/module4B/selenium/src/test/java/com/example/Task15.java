/*Structure your TestNG file to run Naviagte to google and search for testify. 
close the browser 
Naviagate to https://www.mcdonalds.com/us/en-us.html . print out the colour - code of the order now button. All test should be done in one class and utilize your knowldge of tesNG annotation)
 */

package com.example;

import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

public class Task15 {

    public static void main(String[] args) {
        
    }
    private static final TimeUnit MILLISECONDS = null;
    WebDriver driver = null;

    @BeforeMethod
    public void searchTestify() {
        System.setProperty("webdriver.Firefox.driver","/Users/udemejalekun/Desktop/TAS/module4/module4B/selenium/src/geckodriver");
        driver = new FirefoxDriver();
        driver.navigate().to("https://www.google.com/");
        driver.manage().window().maximize();
        WebElement inputTestify = driver.findElement(By.cssSelector("body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div"));
        inputTestify.sendKeys("testify ltd");
        inputTestify.sendKeys(Keys.RETURN);
        driver.manage().timeouts().implicitlyWait(5, MILLISECONDS);
        driver.quit();
    }

    @Test
    public void searchMcDonalds() throws InterruptedException{
        System.setProperty("webdriver.Firefox.driver","/Users/udemejalekun/Desktop/TAS/module4/module4B/selenium/src/geckodriver");
        driver = new FirefoxDriver();
        driver.navigate().to("https://www.mcdonalds.com/us/en-us.html/");
        driver.manage().window().maximize();
        // Get the 'Order Now' button color
        String buttonColor = driver.findElement(By.cssSelector("#button-ordernow")).getCssValue("background-color");
        System.out.println("The \"Order now\" Button color is: " + buttonColor);
        Thread.sleep(3000);
    }
}
