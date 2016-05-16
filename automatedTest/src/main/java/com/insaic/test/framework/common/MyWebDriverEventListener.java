package com.insaic.test.framework.common;

import org.apache.commons.io.FileUtils;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.remote.RemoteWebDriver;
import org.openqa.selenium.support.events.AbstractWebDriverEventListener;
import java.io.File;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;

/**
 * Created by bernie on 5/14/16.
 */
public class MyWebDriverEventListener extends AbstractWebDriverEventListener {
    @Override
    public void onException(Throwable throwable, WebDriver driver) {
        SimpleDateFormat dateFormat = new SimpleDateFormat("yyyyMMdd_hhmmss");
        String dateStr = dateFormat.format(new Date());
        try {
            FileUtils.copyFile(((RemoteWebDriver)driver).getScreenshotAs(OutputType.FILE),
                    new File(String.format("/Users/bernie/%s%s%s_%s.png",
                            ((RemoteWebDriver)driver).getCapabilities().getPlatform(),
                            ((RemoteWebDriver)driver).getCapabilities().getBrowserName(),
                            ((RemoteWebDriver)driver).getCapabilities().getVersion(),
                            dateStr)));

        } catch (IOException e) {
            e.printStackTrace();
        }
        driver.quit();
//        NodeGenerator.releaseClient((RemoteWebDriver)driver);
    }
}
