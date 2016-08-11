package com.bernie.ocr;

import cn.easyproject.easyocr.EasyOCR;
import cn.easyproject.easyocr.ImageType;

import java.io.File;

/**
 * Created by bida on 2016/6/17.
 */
public class EasyOCRDemo {
    public static void main(String[] args) {
        EasyOCR e = new EasyOCR();
        e.setTesseractPath("C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe");
        String randCode = e.discernAndAutoCleanImage("c:\\workspace\\bconvert.jpg", ImageType.PLAYER);
        System.out.println(randCode);
    }
}
