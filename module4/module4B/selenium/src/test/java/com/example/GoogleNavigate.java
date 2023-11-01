package com.example;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;


public class GoogleNavigate {
    public static void main(String[] args) {
        System.setProperty("webdriver.chrome.driver","/Users/udemejalekun/Desktop/TAS/module4/module4B/selenium/src/chromedriver");
        WebDriver driver = new ChromeDriver();
        driver.get("https://www.google.com/");
        driver.manage().window().maximize();
        driver.findElement(By.id("input")).sendKeys("Baseball");

    }
}
