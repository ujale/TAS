package com.example;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.interactions.Actions;

public class Task12 {
    public static void main(String[] args) {
        System.setProperty("webdriver.Firefox.driver","/Users/udemejalekun/Desktop/TAS/module4/module4B/selenium/src/geckodriver");
        WebDriver driver = new FirefoxDriver();
        driver.get("https://jqueryui.com/resizable/");
        driver.manage().window().maximize();
        driver.switchTo().frame(0);
        WebElement resize = driver.findElement(By.xpath("/html/body/div/div[3]"));
        Actions resizing = new Actions(driver);
        resizing.clickAndHold(resize).moveByOffset(322, 190).build().perform();
    }
        
}
