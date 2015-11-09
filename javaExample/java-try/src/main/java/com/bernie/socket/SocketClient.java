package com.bernie.socket;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

/**
 * Created by bida on 2015/10/29.
 */
public class SocketClient {
    public static void main(String[] args) throws IOException {
        Socket socket = new Socket("192.168.98.45", 4700);

        BufferedReader sin = new BufferedReader(new InputStreamReader(System.in));

        PrintWriter os = new PrintWriter(socket.getOutputStream());

        BufferedReader is = new BufferedReader(new InputStreamReader(socket.getInputStream()));

        String readline;

        readline = sin.readLine();
        while(!"bye".equals(readline)){
            os.println(readline);
            os.flush();
            System.out.println("client : " + readline);

            System.out.println("Server : " + is.readLine());

            readline = sin.readLine();
        }
        os.close();
        is.close();
        socket.close();
    }
}
