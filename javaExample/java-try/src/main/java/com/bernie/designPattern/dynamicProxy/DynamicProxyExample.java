package com.bernie.designPattern.dynamicProxy;

import com.bernie.designPattern.staticPattern.Hello;
import com.bernie.designPattern.staticPattern.HelloImpl;

import java.lang.reflect.Proxy;

/**
 * Created by bida on 2016/7/8.
 */
public class DynamicProxyExample {
    public static void main(String[] args) {
        Hello hello = new HelloImpl();
        DynamicProxy dynamicProxy = new DynamicProxy(hello);

        Hello helloProxy = (Hello) Proxy.newProxyInstance(hello.getClass().getClassLoader(),
                hello.getClass().getInterfaces(), dynamicProxy);

        helloProxy.say("jack");
    }
}
