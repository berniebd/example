package com.bernie.codejson;

import link.jfire.codejson.JsonTool;
import link.jfire.codejson.strategy.WriteStrategy;

/**
 * Created by bida on 2015/12/16.
 */
public class CodejsonDemo {
    public static void main(String[] args) {
        Person person = new Person();
        person.setAge(12);
        person.setName("Jone");
        person.setBoy(false);
        Home home = new Home();
        home.setHeight(12.11f);
        home.setWeight(22.23f);
        home.setName("home name");
        home.setHost(person);
        String json = JsonTool.write(home);
        System.out.println(json);

        String str = "{\"height\":12.11,\"host\":{\"age\":12,\"name\":\"Jone\",\"boy\":false},\"name\":\"home name\",\"weight\":22.23}";

        Home home2 = JsonTool.read(Home.class, str);
        System.out.println(home2.getName());
        System.out.println(home2.getHost().getAge());

        WriteStrategy strategy = new WriteStrategy();
        strategy.addRenameField("Home.name", "halo");
        String json2 = strategy.write(home);
        System.out.println(json2);
    }
}
