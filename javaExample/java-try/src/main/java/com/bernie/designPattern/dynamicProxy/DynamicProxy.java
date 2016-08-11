package com.bernie.designPattern.dynamicProxy;

import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;

/**
 * Created by bida on 2016/7/8.
 */
public class DynamicProxy implements InvocationHandler {
    private Object target;

    public DynamicProxy(Object target){
        this.target = target;
    }

    @Override
    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
        before();
        Object result = method.invoke(target, args);
        after();
        return result;
    }

    private void before(){
        System.out.println("Before");
    }

    private void after(){
        System.out.println("After");
    }
}
