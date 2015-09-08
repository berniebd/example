package com.bernie.annotation.example2;

import java.lang.annotation.*;

/**
 * Created by bida on 2015/9/7.
 */
@Target(ElementType.METHOD)
@Inherited
@Retention(RetentionPolicy.RUNTIME)
@Documented
public @interface MethodInfo {
    String author() default "Pankaj";
    String date();
    int revision() default 1;
    String comments();
}
