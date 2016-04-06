package com.bernie.appium;

import io.appium.java_client.android.AndroidDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.remote.DesiredCapabilities;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.concurrent.TimeUnit;

/**
 * Created by bida on 2015/9/21.
 */
public class SimpleExample {
    public static void main(String[] args) throws MalformedURLException {
        DesiredCapabilities cap = new DesiredCapabilities();
        cap.setCapability("platformName", "android");
//        cap.setCapability("app", "e:/example.apk");
        cap.setCapability("app", "/Users/bernie/Downloads/example.apk");
        cap.setCapability("unicodeKeyboard", "true");
        cap.setCapability("resetKeyboard", "true");
//        cap.setCapability("deviceName", "huawei-plk_ul00-W8R0215813002079");
        cap.setCapability("deviceName", "Nexus_5_API_21");
//        cap.setCapability("deviceName", "192.168.120.91:5555");

        AndroidDriver driver = new AndroidDriver(new URL("http://127.0.0.1:4723/wd/hub"), cap);
        driver.manage().timeouts().implicitlyWait(15, TimeUnit.SECONDS);
        driver.findElementByAndroidUIAutomator("new UiSelector().text(\"排行榜\")").click();

//        根据父元素获取同级元素
        driver.findElementByAndroidUIAutomator("new UiSelector().text(\"排行榜\")." +
                "fromParent(new UiSelector().text(\"应用\"))").click();

//        获取子元素
        driver.findElementByAndroidUIAutomator("new UiSelector().resourceId(\"com.wandoujia.phoenix2:id/tab_host\")" +
                ".childSelector(new UiSelector().className(\"android.widget.TextView\").text(\"游戏\"))").click();

        driver.findElementByAndroidUIAutomator("new UiSelector().resourceId(\"com.wandoujia.phoenix2:id/search_image\")").click();

        driver.navigate().back();

        driver.findElementByAndroidUIAutomator("new UiSelector().resourceId(\"com.wandoujia.phoenix2:id/search_text\")").click();


        driver.findElementByAndroidUIAutomator("new UiSelector().resourceId(\"com.wandoujia.phoenix2:id/search_box_edit\")")
                .sendKeys("腾讯新闻");
        driver.findElementByAndroidUIAutomator("new UiSelector().resourceId(\"com.wandoujia.phoenix2:id/search_button\")").click();
        WebElement ele = (WebElement) driver.findElementsByAndroidUIAutomator("new UiSelector()" +
                ".className(\"android.widget.TextView\").text(\"安装\")").get(0);
        ele.click();
        driver.openNotifications();
        driver.quit();
    }
}
