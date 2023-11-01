package com.example;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.testng.asserts.SoftAssert;

public class Assertions {

    public void hardAssert(){
        String name = "Ben";
        Assert.assertEquals(name, "Benny");
        System.out.println("Code reached here");
    }

    @Test
    public void softAssert(){
        String name = "Ben";
        SoftAssert sa = new SoftAssert(); // Create a method
        sa.assertEquals(name, "Benny");
        System.out.println("Code reached here again");
        sa.assertAll();
    }
}
