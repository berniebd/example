package com.bernie.hessiantry;

import com.caucho.hessian.client.HessianProxyFactory;

import java.net.MalformedURLException;
import java.util.Iterator;
import java.util.Map;

/**
 * Created by bida on 2015/8/5.
 */
public class HessianClientTest {
    public static void main(String[] args) throws MalformedURLException {
        String url = "http://localhost:8080/HessianService";

        HessianProxyFactory factory = new HessianProxyFactory();
        HelloHessian hello = (HelloHessian)factory.create(HelloHessian.class, url);

        MyCar myCar = hello.getMyCar();
        System.out.println(myCar.toString());

        System.out.println(hello.sayHello());

        for(Map.Entry<String, String> entry : hello.myBabays().entrySet()){
            System.out.println(entry.getKey() + " " + entry.getValue());
        }

        Iterator<String> items = hello.myLoveFruit().iterator();
        while (items.hasNext()){
            System.out.println(items.next());
        }
    }
}
