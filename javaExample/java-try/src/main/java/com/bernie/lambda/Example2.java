package com.bernie.lambda;


import com.google.common.collect.Lists;

import java.util.Arrays;
import java.util.List;
import java.util.function.Predicate;

/**
 * Created by bida on 2015/12/3.
 */
public class Example2 {
//    public static void filter(List names, Predicate condition){
//        names.stream().filter((name) -> (condition.test(name))).forEach((name) -> {
//            System.out.println(name + " ");}
//        );
//    }

    public static void main(String[] args) {
        List<String> languages = Arrays.asList("Java", "Scala", "C++", "Hashkell", "Lisp", "Jaaa");
        Predicate<String> startWithJ = (n) -> n.startsWith("J");
        Predicate<String> fourLetterLong = (n) -> n.length() == 4;

        languages.stream().filter(startWithJ.and(fourLetterLong)).forEach(System.out::println);
    }
}
