package com.bernie.appium;

import io.appium.java_client.ios.IOSDriver;
import org.openqa.selenium.By;
import org.openqa.selenium.remote.DesiredCapabilities;

import java.net.MalformedURLException;
import java.net.URL;

/**
 * Created by bida on 2015/10/9.
 */
public class IOSExample2 {
    public static void main(String[] args) throws MalformedURLException {
        DesiredCapabilities cap = new DesiredCapabilities();
        IOSDriver driver = new IOSDriver(new URL(""), cap);
        driver.findElement(By.tagName(""));
    }
}
