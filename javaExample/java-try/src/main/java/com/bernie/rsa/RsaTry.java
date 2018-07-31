package com.bernie.rsa;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import java.util.Base64;

public class RsaTry {
    private static final int KEYSIZE = 1024;
    public static void main(String[] args) throws IOException, NoSuchAlgorithmException {
        KeyPairGenerator pairgen = KeyPairGenerator.getInstance("RSA");
        SecureRandom random = new SecureRandom();
        pairgen.initialize(KEYSIZE, random);


        KeyPair keyPair = pairgen.generateKeyPair();
        byte[] publicKey = keyPair.getPublic().getEncoded();
        byte[] privateKey = keyPair.getPrivate().getEncoded();


        System.out.println(new String(Base64.getEncoder().encode(publicKey)));
        System.out.println(new String(Base64.getEncoder().encode(privateKey)));
        ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream("public"));
        out.writeObject(keyPair.getPublic());
        out.close();
        out = new ObjectOutputStream(new FileOutputStream("private]"));

        out.writeObject(keyPair.getPrivate());
        out.close();
    }
}
