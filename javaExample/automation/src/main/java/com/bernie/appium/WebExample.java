package com.bernie.appium;

import io.appium.java_client.android.AndroidDriver;
import org.openqa.selenium.By;
import org.openqa.selenium.remote.CapabilityType;
import org.openqa.selenium.remote.DesiredCapabilities;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.concurrent.TimeUnit;

/**
 * Created by bernie on 4/5/16.
 */
public class WebExample {
    public static void main(String[] args) throws MalformedURLException {
        DesiredCapabilities cap = new DesiredCapabilities();
        cap.setCapability(CapabilityType.BROWSER_NAME, "chrome");
//        cap.setCapability("deviceName", "Nexus_5_API_21");
        cap.setCapability("deviceName", "huawei-plk_ul00-W8R0215813002079");



        AndroidDriver driver = new AndroidDriver(new URL("http://127.0.0.1:4723/wd/hub"), cap);
        driver.manage().timeouts().implicitlyWait(15, TimeUnit.SECONDS);
        driver.get("http://www.baidu.com");
        driver.findElement(By.id("index-kw")).sendKeys("上汽保险");
        driver.findElement(By.id("index-bn")).click();
    }
}
