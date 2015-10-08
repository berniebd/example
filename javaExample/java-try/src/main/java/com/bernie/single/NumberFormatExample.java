package com.bernie.single;

import java.text.NumberFormat;
import java.util.Locale;

/**
 * Created by bida on 2015/10/8.
 */
public class NumberFormatExample {
    public static void main(String[] args) {
        double percent = 50.5D / 150D;
        double currency = 123456789.123D;
        System.out.println(percent);

        NumberFormat format = NumberFormat.getPercentInstance();
//        小数部分位数
        format.setMinimumFractionDigits(3);
        System.out.println(format.format(percent));
//        整数部分位数
        format.setMinimumIntegerDigits(3);
        System.out.println(format.format(percent));

//        默认地区
        NumberFormat format1 = NumberFormat.getCurrencyInstance();
//        指定地区
        NumberFormat format2 = NumberFormat.getCurrencyInstance(Locale.US);
        format1.setMinimumFractionDigits(3);
        System.out.println(format1.format(currency));
        System.out.println(format2.format(currency));
    }
}
