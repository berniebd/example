package com.bernie.annotation.example1;

import java.lang.annotation.*;

/**
 * Created by bida on 2015/9/7.
 */
@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
@Documented
@Inherited
public @interface Bind {
    public String name();
    public int time() default 0;
}
