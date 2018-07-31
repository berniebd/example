package com.bernie.myself;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

@Component
public class StaticCfg implements Cloneable{
    @Value("bernie")
    public String name;

    @Value("1")
    public int age;

    @Value("true")
    public boolean isMale;

    @Value("99,98,97")
    public int[] scores;

    public void setName(String name){
        this.name = name;
    }

    @Override
    public Object clone() throws CloneNotSupportedException{
        return super.clone();
    }
}
