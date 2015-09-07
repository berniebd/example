package com.bernie;

/**
 * Created by bernie on 9/3/15.
 */
public class DemoServiceImpl implements DemoService{
    public String sayHello(String name) {
        System.out.println("name is " + name);
        return "hello --->>>" + name;
    }
}
