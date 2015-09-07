package com.bernie.single;

import java.io.FileOutputStream;
import java.io.IOException;
import java.util.UUID;

/**
 * Created by bida on 2015/8/28.
 */
public class UUIDTry {
    public static void main(String[] args) throws IOException {
        String uuid;

        FileOutputStream fos = new FileOutputStream("C:\\uuid.txt");
//        BufferedWriter writer = new BufferedWriter();
        for(int i = 0;i < 10;i++){
            uuid = UUID.randomUUID().toString();
            fos.write(new StringBuilder(uuid.substring(0, 7)).append(uuid.substring(9, 12)).append(uuid.substring(14,17)).append(uuid.substring(19, 22)).
                    append(uuid.substring(24, 31)).append("\r\n").toString().getBytes());

        }

        fos.close();
    }
}
