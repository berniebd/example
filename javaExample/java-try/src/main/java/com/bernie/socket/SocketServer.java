package com.bernie.socket;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

/**
 * Created by bida on 2015/10/30.
 */
public class SocketServer {
    public static void main(String[] args) throws IOException {
        ServerSocket server = new ServerSocket(4700);
        Socket socket = server.accept();

        BufferedReader is = new BufferedReader(new InputStreamReader(socket.getInputStream()));

        PrintWriter os = new PrintWriter(socket.getOutputStream());

        BufferedReader sin = new BufferedReader(new InputStreamReader(System.in));

        System.out.println("from client: " + is.readLine());

        String line = sin.readLine();

        while(!"bye".equals(line)){
            os.println(line);
            os.flush();
            System.out.println("Server: " + line);
            System.out.println("client: " + is.readLine());
            line = sin.readLine();
        }

        os.close();
        is.close();
        socket.close();
        server.close();
    }
}
