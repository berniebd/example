package com.bernie.designPattern.staticPattern;

/**
 * Created by bida on 2016/7/8.
 */
public class HelloImpl implements Hello {
    @Override
    public void say(String name) {
        System.out.println("Hello! " + name);
    }
}
