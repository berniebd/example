package com.bernie.lambda;

import org.jdom.output.SAXOutputter;

/**
 * Created by bida on 2015/12/3.
 */
abstract  class Person{
    public abstract void eat();
}

class Child extends Person{
    @Override
    public void eat() {
        System.out.println("eat something");
    }
}

public class AnanymouseInnerClassDemo {
    public static void main(String[] args) {
//        Person p = new Child();
//        p.eat();
        Person p = new Person() {
            @Override
            public void eat() {
                System.out.println("eating something");
            }
        };
        p.eat();
        Runnable r = () -> System.out.println("hello world");
    }
}
