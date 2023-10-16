package com.example;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

public class Task6 {
    public static void main(String[] args) throws InterruptedException {
        System.setProperty("webdriver.Firefox.driver","/Users/udemejalekun/Desktop/TAS/module4/module4B/selenium/src/geckodriver");
        WebDriver driver = new FirefoxDriver();
        driver.get("https://www.saucedemo.com/");
        driver.manage().window().maximize();
        driver.findElement(By.cssSelector("#user-name")).sendKeys("standard_user");
        driver.findElement(By.cssSelector("#password")).sendKeys("secret_sauce");
        driver.findElement(By.cssSelector("#login-button")).click();
        driver.findElement(By.cssSelector("#add-to-cart-sauce-labs-backpack")).click();
        driver.findElement(By.cssSelector("#shopping_cart_container > a")).click();
        driver.findElement(By.cssSelector("#checkout")).click();
        
    }
}
