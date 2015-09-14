package com.bernie;

import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.remote.DesiredCapabilities;

import java.net.MalformedURLException;

/**
 * Created by bida on 2015/9/14.
 */
public class SimpleDemo {
    public static void main(String args[]) throws MalformedURLException {
//        FirefoxDriver driver = new FirefoxDriver();
        System.setProperty("webdriver.chrome.driver","d:/tools/chromedriver.exe");
        DesiredCapabilities cap = DesiredCapabilities.chrome();
        ChromeDriver driver = new ChromeDriver(cap);

        driver.get("http://www.baidu.com");
    }
}
