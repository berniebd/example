package com.bernie.single;

import cn.easyproject.easyocr.EasyOCR;

import java.io.File;

/**
 * Created by bida on 2015/10/13.
 */
public class OCRDemo {
    public static void main(String[] args) {
        EasyOCR e = new EasyOCR();
        e.setTesseractPath("D:\\tools\\Tesseract-OCR\\tesseract.exe");
        System.out.println(e.discern(new File("d:\\randCodeImage.jpg")));
    }
}
