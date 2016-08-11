package com.bernie.designPattern.dynamicProxy;

import com.bernie.designPattern.staticPattern.HelloImpl;

/**
 * Created by bida on 2016/7/8.
 */
public class CGLibProxyExample {
    public static void main(String[] args) {
        CGLibProxy cgLibProxy = new CGLibProxy();
        HelloImpl helloImple = cgLibProxy.getProxy(HelloImpl.class);
        helloImple.say("Jack");
    }
}
