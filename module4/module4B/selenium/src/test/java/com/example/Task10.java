package com.example;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

public class Task10 {
    public static void main(String[] args) throws InterruptedException {
        System.setProperty("webdriver.Firefox.driver","/Users/udemejalekun/Desktop/TAS/module4/module4B/selenium/src/geckodriver");
        WebDriver driver = new FirefoxDriver();
        driver.navigate().to("https://jqueryui.com/");
        driver.manage().window().maximize();
        driver.findElement(By.xpath("//a[contains(text(),'Dialog')]")).click();
        driver.switchTo().frame(0);
        driver.findElement(By.xpath("//body/div[1]/div[1]/button[1]/span[1]")).click();

    }
}
