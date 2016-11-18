package com.bernie.appium;

import io.appium.java_client.android.AndroidDriver;
import org.openqa.selenium.remote.DesiredCapabilities;

import java.net.MalformedURLException;
import java.net.URL;

/**
 * Created by bida on 2015/9/15.
 */
public class InstallAndUninstallApp {
    public static void main(String args[]) throws MalformedURLException {
        DesiredCapabilities cap = new DesiredCapabilities();
        cap.setCapability("deviceName", "huawei-plk_ul00-W8R0215813002079");
        cap.setCapability("app", "e:/example.apk");
        AndroidDriver driver = new AndroidDriver(new URL("http://127.0.0.1:4723/wd/hub"), cap);

        driver.resetApp();
        driver.launchApp();
        driver.closeApp();
//        System.out.println(driver.isAppInstalled("com.wandoujia.phoenix2"));
//        if(driver.isAppInstalled("com.wandoujia.phoenix2")){
//            System.out.println("installed");
//            driver.removeApp("com.wandoujia.phoenix2");
//        }else{
//            System.out.println("not installed");
//        }
//        driver.installApp("e:/example.apk");

//        driver.runAppInBackground(10);
        driver.quit();
    }
}
