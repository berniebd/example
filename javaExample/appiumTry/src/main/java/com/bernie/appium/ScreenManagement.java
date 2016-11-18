package com.bernie.appium;

import io.appium.java_client.android.AndroidDriver;
import org.apache.commons.io.FileUtils;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.remote.DesiredCapabilities;

import java.io.File;
import java.io.IOException;
import java.net.URL;

/**
 * Created by bida on 2015/9/16.
 */
public class ScreenManagement {
    public static void main(String args[]) throws IOException {
        DesiredCapabilities cap = new DesiredCapabilities();
        cap.setCapability("deviceName", "huawei-plk_ul00-W8R0215813002079");
//        cap.setCapability("browserName", "chrome");
        cap.setCapability("app", "e:/example.apk");

        AndroidDriver driver = new AndroidDriver(new URL("http://127.0.0.1:4723/wd/hub"), cap);
//        System.out.println(driver.isLocked());
//        driver.lockScreen(10);
//        System.out.println(driver.isLocked());
        File  img = ((TakesScreenshot)driver).getScreenshotAs(OutputType.FILE);
        System.out.println(img.getName());
        System.out.println(img.getAbsolutePath());
        FileUtils.moveFile(img, new File("c:/" + img.getName()));
        driver.quit();
    }
}
