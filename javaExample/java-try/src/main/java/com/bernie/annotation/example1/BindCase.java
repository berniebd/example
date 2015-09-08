package com.bernie.annotation.example1;

/**
 * Created by bida on 2015/9/7.
 */
public class BindCase {
    @Bind(name = "case", time = 1)
    public void method(){
        System.out.println("method");
    }

    public void method1(){
        System.out.println("method1");
    }

    @Bind(name = "case2", time = 20)
    public void method2(){
        System.out.println("method2");
    }
}
