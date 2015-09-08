package com.bernie.annotation.example2;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by bida on 2015/9/7.
 */
public class AnnotationExample {
    @Override
    @MethodInfo(author = "Pankaj", comments = "Main method", date = "Nov 12 2013", revision = 2)
    public String toString(){
        return "Override toString method";
    }

    @Deprecated
    @MethodInfo(comments = "deprecated method", date = "Jan 12 2014")
    public static void oldMethhod(){
        System.out.println("old method,do not use it");
    }

    @SuppressWarnings({"unchecked", "deprecation"})
    public static void genericsTest(){
        List l = new ArrayList();
        l.add("abc");
        oldMethhod();
    }
}
