package com.bernie.aspectTry;

import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.DeclareParents;

@Aspect
public class DecoratorAspect {
    @DeclareParents(value = "com.bernie.aspectTry.Performance+", defaultImpl = DefaultDecorator.class)
    public static Decorator encoreable;

}
