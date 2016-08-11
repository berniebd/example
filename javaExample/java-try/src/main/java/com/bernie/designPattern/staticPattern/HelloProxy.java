package com.bernie.designPattern.staticPattern;

/**
 * Created by bida on 2016/7/8.
 */
public class HelloProxy implements Hello {
    private HelloImpl helloImpl;
    public HelloProxy(){
        helloImpl = new HelloImpl();
    }

    @Override
    public void say(String name) {
        before();
        helloImpl.say(name);
        after();
    }

    private void before(){
        System.out.println("Before");
    }

    private void after(){
        System.out.println("After");
    }
}
