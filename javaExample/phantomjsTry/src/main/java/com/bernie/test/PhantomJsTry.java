package com.bernie.test;

import org.apache.commons.io.FileUtils;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.phantomjs.PhantomJSDriver;
import org.openqa.selenium.phantomjs.PhantomJSDriverService;
import org.openqa.selenium.remote.DesiredCapabilities;

import java.io.File;
import java.io.IOException;

/**
 * Created by bida on 2016/11/18.
 */
public class PhantomJsTry {
    public static void main(String[] args) throws IOException {
        DesiredCapabilities cap = new DesiredCapabilities();
        cap.setCapability(PhantomJSDriverService.PHANTOMJS_EXECUTABLE_PATH_PROPERTY,
                "C:\\tools\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe");
        PhantomJSDriver driver = new PhantomJSDriver(cap);
        driver.get("http://www.baidu.com");
        System.out.println(driver.getTitle());
        FileUtils.copyFile(driver.getScreenshotAs(OutputType.FILE), new File("e:\\test.png"));
        driver.close();
        driver.quit();
    }
}
