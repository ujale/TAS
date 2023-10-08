package com.example;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.safari.SafariDriver;

public class TestifySafari {
    public static void main(String[] args) {
        WebDriver driver = new SafariDriver();

        
        driver.get("https://www.testifyltd.com/contact");
        driver.manage().window().maximize();
        driver.findElement(By.id("input")).sendKeys("Baseball");
        //driver.close();
    }
}
