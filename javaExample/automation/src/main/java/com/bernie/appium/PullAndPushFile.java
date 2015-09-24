package com.bernie.appium;

import io.appium.java_client.android.AndroidDriver;
import org.openqa.selenium.remote.DesiredCapabilities;

import java.io.*;
import java.net.URL;

/**
 * Created by bida on 2015/9/14.
 */
public class PullAndPushFile {
    public static void main(String args[]) throws IOException {
        DesiredCapabilities cap = new DesiredCapabilities();
        cap.setCapability("deviceName", "huawei-plk_ul00-W8R0215813002079");

        AndroidDriver driver = new AndroidDriver(new URL("http://127.0.0.1:4723/wd/hub"), cap);

        byte[] content = driver.pullFile("/storage/emulated/0/log/log-popsdk-2015-09-13.log");
        String s = new String(content);
        System.out.println(s);
        FileOutputStream f = new FileOutputStream(new File("e:/pull.txt"));
        f.write(content);

        StringBuilder wrContent = new StringBuilder("");
        BufferedReader reader = new BufferedReader(new FileReader(new File("e:/pull.txt")));
        String tmp = "";
        while((tmp = reader.readLine()) != null){
            wrContent.append(tmp);
        }
        driver.pushFile("/storage/emulated/0/Download/push2.txt", wrContent.toString().getBytes());

        driver.quit();
    }
}
