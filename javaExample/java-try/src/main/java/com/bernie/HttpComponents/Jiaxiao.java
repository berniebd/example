package com.bernie.HttpComponents;

import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;

import java.util.Date;

/**
 * Created by bida on 2016/6/13.
 */
public class Jiaxiao {
    public static void main(String[] args) {
        System.out.println(new Date().getTime());
        String imgUrl = String.format("http://zhjp.sz-its.cn/Pages/GetCheckCode.aspx?timer=%s", new Date().getTime());

        CloseableHttpClient client = HttpClients.createDefault();
        HttpPost capthca = new HttpPost(String.format("http://zhjp.sz-its.cn/Pages/GetCheckCode.aspx?timer={1}", new Date().getTime()));
    }
}
