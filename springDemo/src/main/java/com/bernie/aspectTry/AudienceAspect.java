package com.bernie.aspectTry;


import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.*;

import java.util.HashMap;
import java.util.Map;

@Aspect
public class AudienceAspect {

    @Pointcut("execution(* com.bernie.aspectTry.JonePerformance.perform(..))")
    public void performance(){}

//    @Pointcut("execution(* com.bernie.aspectTry.JonePerformance.perform(String)) && args(music)")

    @Around("performance()")
    public void watchPerformance(ProceedingJoinPoint jp){
        try{
            System.out.println("Siling cell phones");
            System.out.println("Taking seats");
            jp.proceed();
            System.out.println("CLAP CLAP CLAP");
        } catch (Throwable e){
            System.out.println("Demanding a refund");
        }
    }


//    @Before("performance()")
//    public void silenceCellPhones(){
//        System.out.printf("Silencing cell phones!\n");
//    }
//
//    @Before("performance()")
//    public void takeSeats(){
//        System.out.printf("Taking seats!\n");
//    }
//
//    @After("performance()")
//    public void applause(){
//        System.out.println("CLAP CLAP CLAP!\n");
//    }
//
//    @AfterThrowing("performance()")
//    public void demandRefund(){
//        System.out.println("Demanding a refund!\n");
//    }
}
