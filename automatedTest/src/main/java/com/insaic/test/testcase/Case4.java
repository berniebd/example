package com.insaic.test.testcase;

import com.insaic.test.framework.common.NodeGenerator;
import org.openqa.selenium.support.events.EventFiringWebDriver;
import org.testng.Assert;
import org.testng.annotations.Parameters;
import org.testng.annotations.Test;

/**
 * Created by bernie on 5/14/16.
 */
public class Case4 {
    @Parameters({"expect", "actual"})
    @Test
    public void testOne(String expect, String actual) throws Exception {
        Assert.assertEquals(expect, actual);
        EventFiringWebDriver driver = NodeGenerator.getAvailableClient("firefox","46");
        Thread.sleep(15000);
        NodeGenerator.releaseClient(driver, "firefox", "46");
    }
}
