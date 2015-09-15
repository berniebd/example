package com.bernie.single;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

/**
 * Created by bida on 2015/9/15.
 */
public class FileDemo {
    public static void main(String[] args) throws IOException {
        File f = new File("e:/pull.txt");
        BufferedReader reader = new BufferedReader(new FileReader(f));
        String tmp = "";
        while ((tmp = reader.readLine()) != null){
            System.out.println(tmp);
        }
    }
}
