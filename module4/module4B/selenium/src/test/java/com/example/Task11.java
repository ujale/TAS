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
        
        JavascriptExecutor scrolling = (JavascriptExecutor) driver;
        scrolling.executeScript("window.scrollBy(0, 500)");
        String text = driver.findElement(By.cssSelector("body.srp:nth-child(2) div.main:nth-child(11) div.e9EfHf div.GyAeWb:nth-child(14) div.s6JM6d div.eqAnXb:nth-child(3) div.v7W49e div.MjjYud:nth-child(3) div.g.Ww4FFb.vt6azd.tF2Cxc.asEBEc div.N54PNb.BToiNc.cvP2Ce div.kb0PBd.cvP2Ce.jGGQ5e:nth-child(1) div.yuRUbf a:nth-child(1) div.notranslate.TbwUpd.NJjxre.iUh30.ojE3Fb:nth-child(3) span.H9lube:nth-child(1) div.eqA2re.NjwKYd.Vwoesf > img.XNo5Ab")).getText();
        System.out.println(text);
        
    }

    
}
