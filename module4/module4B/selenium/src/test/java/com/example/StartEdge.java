package com.example;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.edge.EdgeDriver;

public class StartEdge {
    public static void main(String[] args) {
        System.setProperty("webdriver.Edge.driver", "/Users/udemejalekun/Desktop/TAS/module4/module4B/selenium/src/msedgedriver");
        WebDriver driver = new EdgeDriver();
        driver.get("https://www.konga.com/");
    }
}
