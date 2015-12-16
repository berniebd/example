package com.bernie;

import java.io.File;

/**
 * Created by bida on 2015/12/1.
 */
public class ParameterDemo {
    public static void main(String[] args) {
        int len = args.length;
        System.out.println(len);

        for(int i=0;i<len;i++){
            System.out.println(args[i]);
        }

        File f = new File(args[0]);
    }
}
