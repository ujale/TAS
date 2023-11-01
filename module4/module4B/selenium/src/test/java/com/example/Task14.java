package com.example;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

public class Task14 {
    public static void main(String[] args) {
        System.setProperty("webdriver.Firefox.driver","/Users/udemejalekun/Desktop/TAS/module4/module4B/selenium/src/geckodriver");
        WebDriver driver = new FirefoxDriver();
        driver.navigate().to("https://www.toolsqa.com/ ");
        driver.manage().window().maximize();
        driver.findElement(By.xpath("//a[contains(text(),'Tutorials')]")).click();
    }
}
