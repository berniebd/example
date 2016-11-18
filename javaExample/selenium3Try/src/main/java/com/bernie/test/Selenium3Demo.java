package com.bernie.test;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.remote.DesiredCapabilities;

/**
 * Created by bida on 2016/11/18.
 */
public class Selenium3Demo {
    public static void main(String[] args) {
        DesiredCapabilities cap = DesiredCapabilities.firefox();
        cap.setCapability("marionette", true);
        WebDriver driver = new FirefoxDriver(cap);
        driver.get("http://www.baidu.com");

    }
}
