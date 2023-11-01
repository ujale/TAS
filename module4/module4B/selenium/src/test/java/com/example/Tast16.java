package com.example;

/* Navigate to https://testifyltd.com/ .
Assert that the Our contact column at the footer of the homepeage has the follwing correct details, EMAIL: info@testifyltd.co.uk
LOCATION: Nigeria
PHONE: (+234)904-882-097
 */



import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.testng.Assert;
import org.testng.annotations.BeforeMethod;


public class Tast16 {
    WebDriver driver = null;

    @BeforeMethod
    public void searchTestify() {
        System.setProperty("webdriver.Firefox.driver","/Users/udemejalekun/Desktop/TAS/module4/module4B/selenium/src/geckodriver");
        driver = new FirefoxDriver();
        driver.navigate().to("https://testifyltd.com/");
        driver.manage().window().maximize();
    }

    @Test
    public void searchContact(){
        System.setProperty("webdriver.Firefox.driver","/Users/udemejalekun/Desktop/TAS/module4/module4B/selenium/src/geckodriver");
        driver = new FirefoxDriver();
        driver.navigate().to("https://testifyltd.com/");
        driver.manage().window().maximize();
        driver.findElement(By.xpath("//a[contains(text(),'Contact Us')]")).click();
    }

    @Test
    public void fetchContact(){

        System.setProperty("webdriver.Firefox.driver","/Users/udemejalekun/Desktop/TAS/module4/module4B/selenium/src/geckodriver");
        driver = new FirefoxDriver();
        driver.navigate().to("https://testifyltd.com/contact");
        driver.manage().window().maximize();
        driver.findElement(By.xpath("//body/div[@id='__next']/main[1]/section[1]/div[1]/div[1]/div[1]/ul[1]"));
        String contactEmail = "info@testifyltd.com";
        String contactPhone = "(+234)905-882-0971";
        String country = "Nigeria";
        Assert.assertEquals(country, "Nigeria");
        Assert.assertEquals(contactEmail, "info@testifyltd.com");
        Assert.assertEquals(contactPhone, "Nigeria");
    }
}
