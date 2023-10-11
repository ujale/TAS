package com.example;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

public class Task8 {
    public static void main(String[] args) throws InterruptedException {
        System.setProperty("webdriver.Firefox.driver","/Users/udemejalekun/Desktop/TAS/module4/module4B/selenium/src/geckodriver");
        WebDriver driver = new FirefoxDriver();
        driver.get("https://idorenyinankoh.github.io/loginPage/");
        driver.manage().window().maximize();
        driver.findElement(By.cssSelector("#create")).isEnabled();
        driver.findElement(By.cssSelector("#firstName")).sendKeys("Udems");
        driver.findElement(By.cssSelector("#lastName")).sendKeys("Tester");
        driver.findElement(By.cssSelector("#email")).sendKeys("udem@yopmail.com");
        driver.findElement(By.cssSelector("#female")).click();
        driver.findElement(By.cssSelector("#password")).sendKeys("P@ssw0rd");
        driver.findElement(By.cssSelector("#confirmPass")).sendKeys("P@ssw0rd");
        driver.findElement(By.cssSelector("#xpLevel")).sendKeys("I am a Tester");
        driver.findElement(By.cssSelector("#create")).isEnabled();
    }
}
