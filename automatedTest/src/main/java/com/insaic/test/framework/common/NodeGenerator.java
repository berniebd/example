package com.insaic.test.framework.common;

import org.javatuples.Pair;
import org.openqa.selenium.Capabilities;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.remote.RemoteWebDriver;
import org.openqa.selenium.support.events.EventFiringWebDriver;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.HashMap;

/**
 * Created by bernie on 5/14/16.
 */
public class NodeGenerator {
//    private static NodeGenerator nodeGenerator;
    private static HashMap<Pair<String, String>,Integer> clients = new HashMap<Pair<String, String >, Integer>();
//
//    private NodeGenerator(){}
//
//    public static NodeGenerator getNodeGenerator(){
//        NodeGenerator nodeGenerator = null;
//        if(nodeGenerator == null){
//            synchronized (NodeGenerator.class){
//                if(nodeGenerator == null){
//                    nodeGenerator = new NodeGenerator();
//                }
//            }
//        }
//        return nodeGenerator;
//    }

    private static Capabilities getCapabilities(String browserName) throws Exception {
        Capabilities capabilities = null;
        switch (browserName.toUpperCase()){
            case "FIREFOX":
                capabilities = DesiredCapabilities.firefox();
                break;
            case "IE":
                capabilities =  DesiredCapabilities.internetExplorer();
                break;
            default:
                throw new Exception("请指定正确的浏览器....");
        }
        return capabilities;
    }

    private static void addClient(String browserName, String version){
        System.out.println("begin add clients:" + clients);
        String browser = browserName.toUpperCase();
        if(!clients.containsKey(Pair.with(browser, version))){
            clients.put(Pair.with(browser, version), 1);
        }else{
            clients.put(Pair.with(browser, version), clients.get(Pair.with(browser, version)) + 1);
        }
        System.out.println("after add clients:" + clients);
    }

    private static void reduceClient(String browserName, String version){
        System.out.println("begin reduce client:" + clients);
        String browser = browserName.toUpperCase();
        if(!clients.containsKey(Pair.with(browser, version))){
            return;
        }else if(clients.get(Pair.with(browser, version)) == 1){
            clients.put(Pair.with(browser, version), 0);
        }else{
            clients.put(Pair.with(browser, version), clients.get(Pair.with(browser, version)) - 1);
        }
        System.out.println("after reduce cilents:" + clients);
    }

    public static void releaseClient(EventFiringWebDriver driver, String browserName, String version){
//        String browserName = driver.getCapabilities().getBrowserName();
//        String version = driver.getCapabilities().getVersion();
        driver.quit();
        reduceClient(browserName, version);
    }

    private static EventFiringWebDriver generateClient(String browserName, String version) throws Exception {
        EventFiringWebDriver eventFiringWebDriver = null;
        try {
            WebDriver driver = new RemoteWebDriver(new URL(String.format("http://localhost:5555/wd/hub")), getCapabilities(browserName));
            eventFiringWebDriver = new EventFiringWebDriver(driver);
            eventFiringWebDriver.register(new MyWebDriverEventListener());
        } catch (MalformedURLException e) {
            e.printStackTrace();
        }
        return eventFiringWebDriver;
    }

    public static synchronized EventFiringWebDriver getAvailableClient(String browserName, String version) throws Exception {
        String browser = browserName.toUpperCase();
        EventFiringWebDriver driver = null;
        if(!clients.containsKey(Pair.with(browser, version))) {
            addClient(browserName, version);
            driver = generateClient(browser, version);
        }else if(clients.get(Pair.with(browser, version)) < 4){
            addClient(browserName, version);
            driver = generateClient(browser, version);
        }else if(clients.get(Pair.with(browser, version)) >=4){
            do{
                System.out.println("Wait 10 seconds for available node...:" + clients);
                Thread.sleep(10 * 1000);
            }while(clients.get(Pair.with(browser, version)) >= 3);
            addClient(browserName, version);
            driver = generateClient(browser, version);
        }
        return driver;
    }
}
