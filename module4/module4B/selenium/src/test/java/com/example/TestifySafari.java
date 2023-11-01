package com.example;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.safari.SafariDriver;
import org.testng.annotations.Test;

public class TestifySafari {
    @Test
    public static void main(String[] args) {
        WebDriver driver = new SafariDriver();

        
        driver.navigate().to("https://www.google.com/");
        driver.manage().window().maximize();
        WebElement inputTestify = driver.findElement(By.cssSelector("body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div"));
        inputTestify.sendKeys("testify ltd");
        inputTestify.sendKeys(Keys.RETURN);
        //driver.navigate().refresh();
        driver.quit();
    }
}
