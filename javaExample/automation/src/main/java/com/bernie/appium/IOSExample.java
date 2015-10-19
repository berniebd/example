package com.bernie.appium;

import io.appium.java_client.ios.IOSDriver;
import org.openqa.selenium.remote.DesiredCapabilities;

import java.net.MalformedURLException;
import java.net.URL;

/**
 * Created by bernie on 10/8/15.
 */
public class IOSExample {
    public static void main(String[] args) throws MalformedURLException {
        DesiredCapabilities cap = new DesiredCapabilities();
        IOSDriver driver = new IOSDriver(new URL(""), cap);
        driver.findElementByAccessibilityId("");
        driver.findElementByIosUIAutomation("");
    }
}
