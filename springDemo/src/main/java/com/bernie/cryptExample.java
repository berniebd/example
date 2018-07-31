package com.bernie;

import javax.crypto.Cipher;
import javax.crypto.NoSuchPaddingException;
import java.io.ByteArrayOutputStream;
import java.security.InvalidKeyException;
import java.security.Key;
import java.security.KeyFactory;
import java.security.NoSuchAlgorithmException;
import java.security.spec.InvalidKeySpecException;
import java.security.spec.X509EncodedKeySpec;
import java.util.Base64;

public class cryptExample {
    public static void main(String[] args) throws Exception {
        String KEY_ALGORITHM = "RSA";
        int MAX_ENCRYPT_BLOCK = 117;

        byte[] data = "{\"interfaceHead\":{\"requestNo\":\"20171227101817fOVi8CPu\"},\"responseCode\":\"0000\",\"responseMsg\":\"[行业车型查询接口]调用成功!\",\"vehicleHyModelQueryRes\":{\"isTheSame\":\"1\",\"totalCount\":\"1\",\"vehicleModels\":[{\"deductionDueCodeJY\":\"0\",\"emptyWeight\":1662.0,\"engineCapacity\":2.744,\"familyCode\":\"JPA1AK\",\"familyName\":\"切诺基\",\"gearboxtype\":\"手动档\",\"moldCharacterCode\":\"JPAACD0001\",\"moldName\":\"切诺基BJ2021ED轻型越野汽车\",\"producingArea\":\"2\",\"purchasePrice\":136000.0,\"remark\":\"手动档 四驱\",\"seatCount\":5,\"vehicleAlias\":\"切诺基2700\",\"vehicleBrand\":\"北京吉普\",\"vehiclePower\":96.0,\"yearPattern\":\"\"}]}}"
                .getBytes();
        String publicKey = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCs/qLvyhRJxvjo0xo+tCD9L2eQr3FQfa6RFCnyF+HTK3Y6ee1LO/lR20rRTgY6d1ktsegJQ2oxAzEJzDpTpfK3a1DOQICyJ4Ger26LMrX9wFqBb3ElW3wcHGbxBxoBXcFWVsA6etNNZkU/KWhCxo6XBzEJtqeOZGQzQj/nqHNy7QIDAQAB";

        byte[] keyBytes = decode(publicKey);
        X509EncodedKeySpec x509KeySpec = new X509EncodedKeySpec(keyBytes);
        KeyFactory keyFactory = KeyFactory.getInstance(KEY_ALGORITHM);
        Key publicK = keyFactory.generatePublic(x509KeySpec);
        // 对数据加密
        Cipher cipher = Cipher.getInstance(keyFactory.getAlgorithm());
        cipher.init(Cipher.ENCRYPT_MODE, publicK);
        int inputLen = data.length;
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        int offSet = 0;
        byte[] cache;
        int i = 0;
        // 对数据分段加密
        while (inputLen - offSet > 0) {
            if (inputLen - offSet > MAX_ENCRYPT_BLOCK) {
                cache = cipher.doFinal(data, offSet, MAX_ENCRYPT_BLOCK);
            } else {
                cache = cipher.doFinal(data, offSet, inputLen - offSet);
            }
            out.write(cache, 0, cache.length);
            i++;
            offSet = i * MAX_ENCRYPT_BLOCK;
        }
        byte[] encryptedData = out.toByteArray();
        out.close();
        System.out.println(encryptedData);
    }

    private static byte[] decode(String base64) throws Exception {
        return Base64.getDecoder().decode(base64.getBytes());
    }

    /**
     * 二进制数据编码为BASE64字符串
     *
     * @param bytes
     * @return
     * @throws Exception
     */
    private static String encode(byte[] bytes) throws Exception {
        return new String(Base64.getEncoder().encode(bytes));
    }
}
