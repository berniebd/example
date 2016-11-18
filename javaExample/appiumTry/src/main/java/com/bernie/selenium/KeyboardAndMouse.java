package com.bernie.selenium;

import org.openqa.selenium.Keys;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.interactions.Actions;


/**
 * Created by bida on 2015/9/24.
 */
public class KeyboardAndMouse {
    public static void main(String[] args) {
        FirefoxDriver driver = new FirefoxDriver();
        Actions actions = new Actions(driver);
        actions.keyDown(Keys.ALT).keyDown(Keys.F4).keyUp(Keys.UP).keyUp(Keys.ALT).perform();
        actions.sendKeys();
    }
}
