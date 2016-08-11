package com.bernie.ocr;

import com.asprise.ocr.Ocr;

import java.io.File;

/**
 * Created by bida on 2016/6/15.
 */
public class AspriseDemo {
    public static void main(String[] args) {
        Ocr.setUp();
        Ocr ocr = new Ocr();
        ocr.startEngine("eng", Ocr.SPEED_SLOW);
        String s = ocr.recognize(new File[]{new File("c:\\Workspace\\bconvert.jpg")}, Ocr.RECOGNIZE_TYPE_ALL, Ocr.OUTPUT_FORMAT_PLAINTEXT);
        System.out.println(s);
        ocr.stopEngine();
    }
}
