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
        cap.setCapability("deviceName", "iPhone 6s");
        cap.setCapability("platformName", "iOS");
        cap.setCapability("platformVersion", "9.1");
//        cap.setCapability("browserName", "safari");
        cap.setCapability("dd", "true");
        cap.setCapability("app", "/Users/bernie/Downloads/jdmobile.ipa");
//        cap.setCapability("uiid", "C4A9D8F3-C9B3-4B58-9508-E4961481BBBE");
        IOSDriver driver = new IOSDriver(new URL("http://127.0.0.1:4723/wd/hub"), cap);
//        driver.get("http://www.baidu.com");
    }
}
