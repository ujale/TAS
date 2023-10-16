package com.example;

import java.util.Set;


import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

public class MultipleBrowserWindows {
    public static void main(String[] args) throws InterruptedException {
        System.setProperty("webdriver.Firefox.driver","/Users/udemejalekun/Desktop/TAS/module4/module4B/selenium/src/geckodriver");
        WebDriver driver = new FirefoxDriver();
        driver.get("https://www.dezlearn.com/multiple-browser-windows/"); //for alerts
        driver.manage().window().maximize();
        //String parentWIndow = driver.getWindowHandle();
        driver.findElement(By.cssSelector("#u_7_8")).click();
        // Alert alert = driver.switchTo().alert();
        // System.out.println(alert.getText());
        // driver.findElement(By.cssSelector("#p_alert3")).getText();
        // driver.findElement(By.cssSelector("#p_alert3")).click();
        // Thread.sleep(3000);
        // alert.sendKeys("Testing for alerts with inputs required");
        // Thread.sleep(3000);
        // alert.accept();

        Set<String> windows = driver.getWindowHandles();
        for(String window: windows){
            driver.switchTo().window(window);
            System.out.println(driver.getCurrentUrl());
            if (driver.getCurrentUrl().equalsIgnoreCase("https://www.facebook.com/")){
                String facebook = driver.findElement(By.xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/h2[1]")).getText();
                System.out.println(facebook);
            }
            driver.close();
        }

    }
}
