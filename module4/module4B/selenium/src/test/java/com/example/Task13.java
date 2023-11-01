package com.example;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.Select;

public class Task13 {
    public static void main(String[] args) {
        System.setProperty("webdriver.Firefox.driver","/Users/udemejalekun/Desktop/TAS/module4/module4B/selenium/src/geckodriver");
        WebDriver driver = new FirefoxDriver();
        driver.navigate().to("https://selenium08.blogspot.com/ ");
        driver.manage().window().maximize();
        driver.findElement(By.xpath("/html/body/div[1]/header/div/div/div[1]/div[2]/button/div[1]")).click();
        WebElement searchField = driver.findElement(By.xpath("/html/body/div[1]/header/div/div/div[1]/div[2]/div[1]/div/div/form/div/input"));
        searchField.sendKeys("Demo dropdown");
        searchField.sendKeys(Keys.RETURN);
        WebElement title = driver.findElement(By.linkText("Demo Dropdown List"));
        title.click();
        WebElement selectCountry = driver.findElement(By.xpath("//a[contains(text(),'Read more')]"));
        selectCountry.click();
        Select select = new Select(selectCountry);
        select.selectByValue("HW");
        WebElement selectMonth = driver.findElement(By.xpath("/html/body/div[1]/div[2]/div[1]/div/div/main/div/div[1]/div/article/div/div/div[3]/div[1]/div/div[3]/select"));
        Select select2 = new Select(selectMonth);
        select2.selectByIndex(1);
        select2.selectByValue("Feb");
        select2.selectByVisibleText("March");
    }
}
