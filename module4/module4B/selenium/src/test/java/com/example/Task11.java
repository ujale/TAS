package com.example;

/*Go to google.
search for "testify ltd"
Click on the search that result with www.testifyltd.com
sroll down the testify website and click on the linkedIn icon.
Get the description text on the userpage.(image; https://i.imgur.com/PmrWDXa.png )
*/

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;

public class Task11 {
    
    public static void main(String[] args) throws InterruptedException {
        System.setProperty("webdriver.Firefox.driver","/Users/udemejalekun/Desktop/TAS/module4/module4B/selenium/src/geckodriver");
        WebDriver driver = new FirefoxDriver();
        driver.navigate().to("https://www.google.com/");
        driver.manage().window().maximize();
        WebElement inputTestify = driver.findElement(By.cssSelector("#APjFqb"));
        inputTestify.sendKeys("testify ltd");
        inputTestify.sendKeys(Keys.RETURN);
        driver.findElement(By.xpath("/html/body/div[5]/div/div[10]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/div/span/a/div/div/div/cite")).click();
        
        JavascriptExecutor scrolling = (JavascriptExecutor) driver;
        scrolling.executeScript("window.scrollBy(500, 50)");
        String text = driver.findElement(By.xpath("//*[@id=\"__next\"]/main/section[1]/div/div[1]/div[1]/p")).getText();
        System.out.println(text);
        
    }

    
}
