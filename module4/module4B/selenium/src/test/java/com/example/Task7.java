/* Navigate to https://worldweather.wmo.int/en/home.html. 
Search for your city in the search field. When the result loads, print the days and weather description for each of the days shown in a readable and understandable manner. */


package com.example;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;


public class Task7 {
    public static void main(String[] args) throws InterruptedException {
        System.setProperty("webdriver.Firefox.driver","/Users/udemejalekun/Desktop/TAS/module4/module4B/selenium/src/geckodriver");
        WebDriver driver = new FirefoxDriver();
        driver.get("https://worldweather.wmo.int/en/home.html");
        driver.manage().window().maximize();
        driver.findElement(By.cssSelector("#q_search")).sendKeys("Lagos");
        driver.wait(3000);
        //WebElement searchIcon = driver.findElement(By.cssSelector("#q_search"));
        //WebElement searchIcon = driver.findElement(By.xpath("//body/div[1]/div[5]/div[1]/div[2]/div[1]/form[1]/input[3]"));
        //searchIcon.sendKeys(Keys.RETURN);
        driver.findElement(By.xpath("//body/div[1]/div[5]/div[1]/div[2]/div[1]/form[1]/input[3]")).click();
    }
}
