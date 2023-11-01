package com.example;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.interactions.Actions;

public class MouseActions {
    public static void main(String[] args) throws InterruptedException {
        System.setProperty("webdriver.Firefox.driver","/Users/udemejalekun/Desktop/TAS/module4/module4B/selenium/src/geckodriver");
        WebDriver driver = new FirefoxDriver();
        // driver.get("https://konga.com");
        // driver.manage().window().maximize();
        // WebElement compAcces = driver.findElement(By.xpath("//a[contains(text(),'Computers and Accessories')]"));  // Webelement variable
        // Actions mouse = new Actions(driver);  // Action class
        // mouse.moveToElement(compAcces).build().perform(); // for mouse hovering
        // Thread.sleep(3000);
        // driver.findElement(By.xpath("//body/div[@id='__next']/div[1]/section[1]/div[3]/div[1]/div[1]/div[1]/div[1]")).click();
        
        // // Right- click
        // driver.get("https://demo.guru99.com/test/simple_context_menu.html");
        // driver.manage().window().maximize();
        // WebElement rightClick = driver.findElement(By.xpath("//span[contains(text(),'right click me')]"));
        // Actions mouse = new Actions(driver);
        // mouse.contextClick(rightClick).build().perform(); // to right click
        // driver.findElement(By.cssSelector(".context-menu-icon-copy")).click();
        // Thread.sleep(3000);
        // driver.switchTo().alert().accept();

        // // Double click
        // driver.get("https://demo.guru99.com/test/simple_context_menu.html");
        // driver.manage().window().maximize();
        // WebElement doubleClick = driver.findElement(By.xpath("//button[contains(text(),'Double-Click Me To See Alert')]"));
        // Actions mouse = new Actions(driver);
        // mouse.doubleClick(doubleClick).perform(); // to double click
        // Thread.sleep(3000);
        // System.out.println(driver.switchTo().alert().getText());
        // Thread.sleep(3000);
        // driver.switchTo().alert().accept();
        // System.out.println("--Success--");
        
        // Drag an element
        // driver.get("https://jqueryui.com/draggable/");
        // driver.manage().window().maximize();
        // driver.switchTo().frame(0);
        // WebElement draggableBox = driver.findElement(By.xpath("//div[@id='draggable']"));
        // Actions drag = new Actions(driver);
        // drag.clickAndHold(draggableBox).moveByOffset(348, 180).build().perform();
        // Thread.sleep(3000);

        // // Drag & drop an element
        // driver.get("https://jqueryui.com/droppable/");
        // driver.manage().window().maximize();
        // driver.switchTo().frame(0);
        // WebElement dragBox = driver.findElement(By.xpath("//div[@id='draggable']"));
        // WebElement dropBox = driver.findElement(By.xpath("//div[@id='droppable']"));
        // Actions dragDrop = new Actions(driver);
        // dragDrop.clickAndHold(dragBox).moveToElement(dropBox).build().perform();

        // For Keyboard actions
        /*
         * You can either use the Keys.<> option 
         * Eg
         * inputTestify.sendKeys(Keys.RETURN);
         * OR 
         * use the Actions keyword
         *
         * Actions keys = new Actions(driver);
         * keys.sendKeys("").sendKeys(Keys.ENTER).build().perform()
         */

        // Keyboard actions: Copy all, cut & paste
        driver.get("https://google.com");
        driver.manage().window().maximize();
        Actions actions = new Actions(driver);
        actions.sendKeys("Testify ltd")
            .keyDown(Keys.COMMAND)
            .sendKeys("a").build().perform();
        Thread.sleep(3000);
        
            //cut
        actions.keyDown(Keys.COMMAND)
            .sendKeys("x").build().perform();
        Thread.sleep(3000);

        // paste
        actions.keyDown(Keys.COMMAND)
            .sendKeys("v").sendKeys(Keys.ENTER).build().perform();
        Thread.sleep(3000);
    }
}
