package com.bernie.single;

import com.carrotsearch.junitbenchmarks.BenchmarkOptions;
import com.carrotsearch.junitbenchmarks.BenchmarkRule;
import org.junit.Rule;
import org.junit.Test;
import org.junit.rules.TestRule;

/**
 * Created by bida on 2015/9/6.
 */
public class JUnitBenchmarkTry {
    public static final long LOOPS_COUNT = 1000;

    @Rule
    public TestRule benchmarksRun = new BenchmarkRule();

    @Test
    @BenchmarkOptions(benchmarkRounds = 3, warmupRounds = 1)
    public void stringBuilderBenchmarks(){
        StringBuilder builder = new StringBuilder();
        for(long i = 0;i < LOOPS_COUNT; i++){
            builder.append("i").append(i);
        }
        System.out.println("stringbuilder appends");
        System.out.println(builder.toString().length());
    }

    @Test
    @BenchmarkOptions(benchmarkRounds = 3, warmupRounds = 1)
    public void stringBenchmarks(){
        String buffer = "";
        for(long i = 0;i < LOOPS_COUNT; i++){
            buffer +="i";
            buffer += i;
        }
        System.out.println("String +");
        System.out.println(buffer.toString().length());
    }

}
