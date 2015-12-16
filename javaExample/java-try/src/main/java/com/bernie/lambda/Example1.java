package com.bernie.lambda;

import com.google.common.collect.Lists;
import org.springframework.util.SocketUtils;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

/**
 * Created by bida on 2015/12/1.
 */
public class Example1 {
    public static void main(String[] args) {
        String[] atp = {"Rafael Nadal", "Novak Djokovic",
                "Stanislas Wawrinka",
                "David Ferrer","Roger Federer",
                "Andy Murray","Tomas Berdych",
                "Juan Martin Del Potro"};

        List<String> players = Arrays.asList(atp);
        players.stream().filter(a -> a.contains("a"))
                .sorted(Comparator.comparing(a -> a.toString()))
                .collect(Collectors.groupingBy(b -> b.codePointAt(1)));
//        players.forEach(System.out::println);


//        List<Integer> nums = Lists.newArrayList(1, null, 3, 4, null, 6, 8, 9, null);
//        List<Integer> numWithNull = nums.stream().filter(num -> num != null)
//                .collect(() -> new ArrayList<Integer>(),
//                        (list, item) -> list.add(item),
//                        (list1, list2) ->list1.addAll(list2));
//        List<Integer> numWithoutNull = nums.stream().filter(num -> num != null).collect(Collectors.toList());
//        numWithoutNull.stream().forEach(System.out::println);
//        System.out.println(nums.stream().filter(num -> num != null).count());
//        Stream<String> stringStream = Stream.of("hello world");

//        Stream.iterate(1, item -> item + 1).limit(10).forEach(System.out::println);

//        List<Integer> ints = Lists.newArrayList(1,2,3,4,5,6,7,8,9,10);
//        System.out.println(ints.stream().reduce(10, (sum, item) -> sum + item).hashCode());
//        new Thread( ()-> System.out.println("hello world!")).start();
    }
}
