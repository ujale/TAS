package com.example;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
//import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

public class Task4 {
    public static void main(String[] args) throws InterruptedException {
        System.setProperty("webdriver.Firefox.driver","/Users/udemejalekun/Desktop/TAS/module4/module4B/selenium/src/geckodriver");
        WebDriver driver = new FirefoxDriver();
        // System.setProperty("webdriver.chrome.driver","/Users/udemejalekun/Desktop/TAS/module4/module4B/selenium/src/chromedriver");
        // WebDriver driver = new ChromeDriver();
        driver.get("http://demo.guru99.com/");
        driver.manage().window().maximize();
        driver.findElement(By.linkText("Security Project")).click();
        Thread.sleep(3000); // remove popup
        driver.findElement(By.xpath("/html/body/form/table/tbody/tr[1]/td[2]/input")).sendKeys("Poppie");
        driver.findElement(By.xpath("/html/body/form/table/tbody/tr[2]/td[2]/input")).sendKeys("Passw0rd");
        
    }
}
