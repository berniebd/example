package com.bernie.aspectTry;

import org.springframework.stereotype.Component;

@Component
public class JonePerformance implements Performance {
    public void perform() throws Exception {
        System.out.println("Jone's performance");
        throw new Exception("refund");
    }
}
