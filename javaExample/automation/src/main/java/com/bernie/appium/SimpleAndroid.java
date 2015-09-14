package com.bernie.appium;

import io.appium.java_client.android.AndroidDriver;
import org.openqa.selenium.remote.DesiredCapabilities;

import java.net.MalformedURLException;
import java.net.URL;

/**
 * Created by bida on 2015/9/14.
 */
public class SimpleAndroid {
    public static void main(String args[]) throws MalformedURLException {
        DesiredCapabilities cap = new DesiredCapabilities();
        cap.setCapability("deviceName", "huawei-plk_ul00-W8R0215813002079");
        cap.setCapability("browserName", "Chrome");
//        cap.setCapability("platformVersion", "19");
        AndroidDriver driver = new AndroidDriver(new URL("http://127.0.0.1:4723/wd/hub"), cap);
        driver.get("http://www.baidu.com");
        driver.close();
    }
}
