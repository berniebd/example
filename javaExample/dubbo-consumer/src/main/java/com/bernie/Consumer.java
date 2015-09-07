package com.bernie;

import org.springframework.context.support.ClassPathXmlApplicationContext;

/**
 * Created by bernie on 9/3/15.
 */
public class Consumer {
    public static void main(String args[]){
        ClassPathXmlApplicationContext context = new ClassPathXmlApplicationContext(new String[]{"ApplicationConsumer.xml"});
        context.start();
        DemoService demoService = (DemoService)context.getBean("demoService");

        String name = "bernie";
        String hello = demoService.sayHello(name);
        System.out.println(hello);
        System.out.println(Thread.currentThread().getName() + " --> " + hello);
        context.close();
    }
}
