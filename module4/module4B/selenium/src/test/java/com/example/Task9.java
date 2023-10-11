package com.example;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

public class Task9 {
    public static void main(String[] args) throws InterruptedException {
        System.setProperty("webdriver.Firefox.driver","/Users/udemejalekun/Desktop/TAS/module4/module4B/selenium/src/geckodriver");
        WebDriver driver = new FirefoxDriver();
        driver.navigate().to("https://www.saucedemo.com/");
        driver.manage().window().maximize();
        driver.findElement(By.cssSelector("#user-name")).sendKeys("standard_user");
        driver.findElement(By.cssSelector("#password")).sendKeys("secret_sauce");
        driver.findElement(By.cssSelector("#login-button")).click();
        driver.navigate().refresh();
        driver.navigate().back();
        String attrValue = driver.findElement(By.cssSelector("#login-button")).getAttribute("value");
        System.out.println("The value of the login attribute is" + attrValue);
        driver.navigate().forward();
    }
}
