package com.insaic.test.testcase;

import com.insaic.test.framework.common.NodeGenerator;
import org.openqa.selenium.support.events.EventFiringWebDriver;
import org.testng.annotations.Test;

/**
 * Created by bernie on 5/14/16.
 */
public class Case11 {
//    @Parameters({"expect", "actual"})
    @Test
    public void testOne() throws Exception {
//        Assert.assertEquals(expect, actual);
        EventFiringWebDriver driver = NodeGenerator.getAvailableClient("firefox","45");
        Thread.sleep(15000);
        NodeGenerator.releaseClient(driver, "firefox", "46");
    }
}
