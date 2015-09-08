package com.bernie.annotation.example2;

import java.lang.annotation.Annotation;
import java.lang.reflect.Method;

/**
 * Created by bida on 2015/9/7.
 */
public class AnnotationParsing {
    public static void main(String args[]) throws ClassNotFoundException {
        for(Method method: AnnotationParsing.class.getClassLoader()
                .loadClass("com.bernie.annotation.example2.AnnotationExample")
                .getMethods()){
            if(method.isAnnotationPresent(MethodInfo.class)){
                for(Annotation anno : method.getDeclaredAnnotations()){
                    System.out.println("Annotation in method " + method + " : " + anno);
                }
                MethodInfo methodAnno = method.getAnnotation(MethodInfo.class);
                if(methodAnno.revision() == 1){
                    System.out.println("Method with revision no 1 = " + method);
                }
            }
        }
    }
}
