package com.bernie.designPattern.staticPattern;

/**
 * Created by bida on 2016/7/8.
 */
public class StaticPatternExample {
    public static void main(String[] args) {
        Hello helloProxy = new HelloProxy();
        helloProxy.say("Jack");
    }
}
