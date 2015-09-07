package com.bernie.hessiantry;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Created by bida on 2015/8/5.
 */
public class HelloHessianImpl implements HelloHessian {
    public String sayHello() {
        return "welcome to Hessian";
    }

    public MyCar getMyCar() {
        MyCar myCar = new MyCar();
        myCar.setCarName("阿斯顿.马丁");
        myCar.setCarModel("One-77");
        return myCar;
    }

    public List<String> myLoveFruit() {
        List<String> list = new ArrayList<String>();
        list.add("apple");
        list.add("kiwi");
        list.add("orange");
        return list;
    }

    public Map<String, String> myBabays() {
        Map<String, String> map = new HashMap<String, String>();
        map.put("son", "孙悟饭");
        map.put("daughter", "孙美美");
        return map;
    }
}
