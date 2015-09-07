package com.bernie.selenium;

import org.openqa.selenium.phantomjs.PhantomJSDriver;
import org.openqa.selenium.phantomjs.PhantomJSDriverService;
import org.openqa.selenium.remote.DesiredCapabilities;

/**
 * Created by bida on 2015/8/12.
 */
public class PhantomJsTry {
    public static void main(String[] args){
        DesiredCapabilities cap = new DesiredCapabilities();
        cap.setCapability(PhantomJSDriverService.PHANTOMJS_EXECUTABLE_PATH_PROPERTY,
                "D:\\tools\\phantomjs-1.9.8-windows\\phantomjs.exe");
        PhantomJSDriver driver = new PhantomJSDriver(cap);
        driver.get("http://www.baidu.com");
        System.out.println(driver.getTitle());
        driver.close();
        driver.quit();
    }
}
