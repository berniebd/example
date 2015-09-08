package com.bernie.annotation.example1;


import org.apache.log4j.Logger;

import java.lang.reflect.Method;

/**
 * Created by bida on 2015/9/7.
 */
public class BindClassTracker {
    private static Logger logger = Logger.getLogger(BindCase.class);

    public static void printBindCase(Class<?> bindClass){
        assert bindClass != null;
        for(Method method : bindClass.getDeclaredMethods()){
            Bind bind = method.getAnnotation(Bind.class);
            if(bind == null){
                continue;
            }
            System.out.println(String.format("Found [%s] Bind case : %s-%d", method.getName(), bind.name(), bind.time()));
        }
    }

    public static void main(String args[]) {
        BindClassTracker.printBindCase(BindCase.class);

    }
}
