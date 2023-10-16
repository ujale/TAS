package com.example;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.interactions.Actions;

public class MouseActions {
    public static void main(String[] args) throws InterruptedException {
        System.setProperty("webdriver.Firefox.driver","/Users/udemejalekun/Desktop/TAS/module4/module4B/selenium/src/geckodriver");
        WebDriver driver = new FirefoxDriver();
        driver.get("https://konga.com");
        driver.manage().window().maximize();
        WebElement compAcces = driver.findElement(By.xpath("//a[contains(text(),'Computers and Accessories')]"));
        Actions mouse = new Actions(driver);
        mouse.moveToElement(compAcces).build().perform(); // for mousing over
        Thread.sleep(3000);
        driver.findElement(By.xpath("//body/div[@id='__next']/div[1]/section[1]/div[3]/div[1]/div[1]/div[1]/div[1]")).click();
    }
}
