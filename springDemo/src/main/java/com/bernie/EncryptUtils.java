package com.bernie;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
//import org.apache.commons.collections.map.LinkedMap;
import org.apache.commons.io.IOUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.context.ContextLoader;
import org.springframework.web.context.WebApplicationContext;

import javax.crypto.Cipher;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.security.*;
import java.security.spec.PKCS8EncodedKeySpec;
import java.security.spec.X509EncodedKeySpec;
import java.util.*;

/**
 * 签名工具
 *
 * @author c_yuwei-005
 */
public class EncryptUtils {

    private static final Logger logger = LoggerFactory.getLogger(EncryptUtils.class);

    /**
     * 加密算法RSA
     */
    private static final String KEY_ALGORITHM = "RSA";

    /**
     * 签名算法
     */
    private static final String SIGNATURE_ALGORITHM = "MD5withRSA";

    /**
     * RSA最大加密明文大小
     */
    private static final int MAX_ENCRYPT_BLOCK = 117;

    /**
     * RSA最大解密密文大小
     */
    private static final int MAX_DECRYPT_BLOCK = 128;

    // 保险公司公钥路径
    private static final String INSURER_PUBLIC_KEY_FILE_PATH = "insurer.pk.file.path";

    // 保险公司私钥路径
    private static final String INSURER_PRIVATE_KEY_FILE_PATH = "insurer.sk.file.path";

    // 上汽保险公钥路径
    private static final String INSAIC_PUBLIC_KEY_FILE_PATH = "insaic.pk.file.path";

    // 上汽保险私钥路径
    private static final String INSAIC_PRIVATE_KEY_FILE_PATH = "insaic.sk.file.path";

    /**
     * 太保公钥，上汽私钥
     */
    private static Map<String, String> KEYS = new HashMap<>();

    public enum EncryptKeyType {
        InsurerPublicKey("insurerPublicKey"),
        InsurerPrivateKey("insurerPrivateKey"),
        InsaicPublicKey("insaicPublicKey"),
        InsaicPrivateKey("insaicPrivateKey");

        private String keyType;

        EncryptKeyType(String keyType) {
            this.keyType = keyType;
        }

        public String getKeyType() {
            return keyType;
        }
    }

    /**
     * 生成密钥关键字
     *
     * @param insurer           保险公司代码
     * @param insurerBranchCode 保险公司分公司代码
     * @param dealerCode        经销商代码
     * @param interfaceName     接口名
     * @param keyType           密钥类型
     * @return 密钥关键字
     */
    public static String generateKeyIdentify(String insurer, String insurerBranchCode, String dealerCode, String interfaceName, EncryptKeyType keyType) {
        if (StringUtil.isBlank(insurer) || keyType == null) {
            return null;
        }

        WebApplicationContext applicationContext = ContextLoader.getCurrentWebApplicationContext();
        CacheManager commonCodeCache;
        if (applicationContext != null) {
            commonCodeCache = applicationContext.getBean("commonCodeCacheImpl", CacheManager.class);
        } else {
            commonCodeCache = SpringBeanLocator.getBean("commonCodeCacheImpl", CacheManager.class);
        }

        Map<String, CommonCodeProperty> result = (Map<String, CommonCodeProperty>) commonCodeCache.getAllCache(Constants.INSURER_INTERFACE_CONFIG);

        if (result != null && !result.isEmpty()) {
            // 获取经销商组别
            String dealerGroup = commonCodeCache.getInsurerGroupConfig(insurer, dealerCode, Constants.INSURER_DEALERGROUP_CONFIG);
            // 获取分公司组别
            String insurerBranchGroup = commonCodeCache.getInsurerGroupConfig(insurer, insurerBranchCode, Constants.INSURER_BRANCHGROUP_CONFIG);

            String key = null;
            if (!StringUtil.isBlank(interfaceName)) {
                if (StringUtil.isNotBlank(dealerGroup)) {
                    key = insurer + Constants.DIVISION + dealerGroup + Constants.DIVISION + interfaceName;
                    if (result.get(key) != null && result.get(key).getMap() != null) {
                        return key;
                    }
                }

                if (StringUtil.isNotBlank(insurerBranchCode)) {
                    key = insurer + Constants.DIVISION + insurerBranchCode + Constants.DIVISION + interfaceName;
                    if (result.get(key) != null && result.get(key).getMap() != null) {
                        return key;
                    }
                }

                if (StringUtil.isNotBlank(insurerBranchGroup)) {
                    key = insurer + Constants.DIVISION + insurerBranchGroup + Constants.DIVISION + interfaceName;
                    if (result.get(key) != null && result.get(key).getMap() != null) {
                        return key;
                    }
                }

                key = insurer + Constants.DIVISION + interfaceName;
                if (result.get(key) != null && result.get(key).getMap() != null) {
                    return key;
                }
            }

            if (StringUtil.isNotBlank(dealerGroup)) {
                key = insurer + Constants.DIVISION + dealerGroup + Constants.DIVISION + Constants.ALL;
                if (result.get(key) != null && result.get(key).getMap() != null) {
                    return key;
                }
            }

            if (StringUtil.isNotBlank(insurerBranchCode)) {
                key = insurer + Constants.DIVISION + insurerBranchCode + Constants.DIVISION + Constants.ALL;
                if (result.get(key) != null && result.get(key).getMap() != null) {
                    return key;
                }
            }

            if (StringUtil.isNotBlank(insurerBranchGroup)) {
                key = insurer + Constants.DIVISION + insurerBranchGroup + Constants.DIVISION + Constants.ALL;
                if (result.get(key) != null && result.get(key).getMap() != null) {
                    return key;
                }
            }

            key = insurer + Constants.DIVISION + Constants.ALL;
            if (result.get(key) != null && result.get(key).getMap() != null) {
                return key;
            }
        }

        return null;
    }

    /**
     * 生成密钥关键字
     *
     * @param insurer     保险公司代码
     * @param serviceName 上汽服务名
     * @param version     上汽服务版本号
     * @param keyType
     * @return
     */
    public static String generateKeyIdentify(String insurer, String serviceName, String version, EncryptKeyType keyType) {
        if (StringUtil.isBlank(insurer) || StringUtil.isBlank(version) || keyType == null) {
            return null;
        }

        WebApplicationContext applicationContext = ContextLoader.getCurrentWebApplicationContext();
        CacheManager commonCodeCache;
        if (applicationContext != null) {
            commonCodeCache = applicationContext.getBean("commonCodeCacheImpl", CacheManager.class);
        } else {
            commonCodeCache = SpringBeanLocator.getBean("commonCodeCacheImpl", CacheManager.class);
        }

        Map<String, CommonCodeProperty> result = (Map<String, CommonCodeProperty>) commonCodeCache.getAllCache(Constants.INSAIC_INSURER_SERIVCE_CONFIG);

        if (result != null && !result.isEmpty()) {
            CommonCodeProperty commonCodeProperty = null;
            if (StringUtil.isNotBlank(serviceName)) {
                commonCodeProperty = result.get(insurer + Constants.DIVISION + version + Constants.DIVISION + serviceName);
                if (commonCodeProperty != null && commonCodeProperty.getMap() != null && !commonCodeProperty.getMap().isEmpty()) {
                    return insurer + Constants.DIVISION + version + Constants.DIVISION + serviceName;
                }
            }

            commonCodeProperty = result.get(insurer + Constants.DIVISION + version + Constants.DIVISION + Constants.ALL);

            if (commonCodeProperty != null && commonCodeProperty.getMap() != null && !commonCodeProperty.getMap().isEmpty()) {
                return insurer + Constants.DIVISION + version + Constants.DIVISION + Constants.ALL;
            }
        }

        return null;
    }

    /**
     * 验签
     *
     * @param keyType     密钥类型
     * @param keyIdentify 密钥识别码
     * @param json        json字符串
     * @param sign        数字签名
     * @return
     */
    public static boolean verify(EncryptKeyType keyType, String keyIdentify, String json, String sign) {
        try {
            String publicKey = getKey(keyType, keyIdentify);
            return verify(json.getBytes(), publicKey, sign);
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    /**
     * <p>
     * 校验数字签名
     * </p>
     *
     * @param data      已加密数据
     * @param publicKey 公钥(BASE64编码)
     * @param sign      数字签名
     * @return boolean
     * @throws Exception
     */
    private static boolean verify(byte[] data, String publicKey, String sign) throws Exception {
        byte[] keyBytes = decode(publicKey);
        X509EncodedKeySpec keySpec = new X509EncodedKeySpec(keyBytes);
        KeyFactory keyFactory = KeyFactory.getInstance(KEY_ALGORITHM);
        PublicKey publicK = keyFactory.generatePublic(keySpec);
        Signature signature = Signature.getInstance(SIGNATURE_ALGORITHM);
        signature.initVerify(publicK);
        signature.update(data);
        return signature.verify(decode(sign));
    }

    /**
     * 解密并设值
     *
     * @param keyType     密钥类型
     * @param keyIdentify 密钥识别码
     * @param bizContent  加密后的文本
     * @param root        Map<String,Object>
     * @return Map<String,Object>
     */
//    public static Map<String, Object> decrypt(EncryptKeyType keyType, InterfaceLogEo interfaceLogEo, String keyIdentify, String bizContent, String decryptKeyword, String messageType, boolean isSyncLog, Map<String, Object> root) {
//        String decrypted = decrypt(keyType, interfaceLogEo, keyIdentify, bizContent, messageType, isSyncLog);
//        Map<String, Object> map = new Gson().fromJson(decrypted, Map.class);
//        root.put(decryptKeyword, map);
//        return map;
//    }

    /**
     * 私钥对数据进行解密
     *
     * @param keyType     密钥类型
     * @param keyIdentify 密钥识别码
     * @param bizContent  加密后的文本
     * @return 解密后的文本
     */
    public static String decrypt(EncryptKeyType keyType, InterfaceLogEo interfaceLogEo, String keyIdentify, String bizContent, String messageType, boolean isSyncLog) {
        try {
            String privateKey = getKey(keyType, keyIdentify);
            String decryptStr = new String(decrypt(decode(bizContent), privateKey));
            if (isSyncLog && StringUtil.isNotBlank(messageType) && interfaceLogEo != null) {
                InterfaceLogUtil.setInterfaceLogMessage(interfaceLogEo, decryptStr, messageType);
            }
            return decryptStr;
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    /**
     * 私钥解密
     *
     * @param encryptedData 已加密数据
     * @param privateKey    私钥(BASE64编码)
     * @return byte[]
     * @throws Exception
     */
    private static byte[] decrypt(byte[] encryptedData, String privateKey) throws Exception {
        byte[] keyBytes = decode(privateKey);
        PKCS8EncodedKeySpec pkcs8KeySpec = new PKCS8EncodedKeySpec(keyBytes);
        KeyFactory keyFactory = KeyFactory.getInstance(KEY_ALGORITHM);
        Key privateK = keyFactory.generatePrivate(pkcs8KeySpec);
        Cipher cipher = Cipher.getInstance(keyFactory.getAlgorithm());
        cipher.init(Cipher.DECRYPT_MODE, privateK);
        int inputLen = encryptedData.length;
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        int offSet = 0;
        byte[] cache = null;
        int i = 0;
        // 对数据分段解密
        while (inputLen - offSet > 0) {
            if (inputLen - offSet > MAX_DECRYPT_BLOCK) {
                cache = cipher.doFinal(encryptedData, offSet, MAX_DECRYPT_BLOCK);
            } else {
                cache = cipher.doFinal(encryptedData, offSet, inputLen - offSet);
            }
            out.write(cache, 0, cache.length);
            i++;
            offSet = i * MAX_DECRYPT_BLOCK;
        }
        byte[] decryptedData = out.toByteArray();
        out.close();
        return decryptedData;
    }

    /**
     * 公钥加密
     *
     * @param keyType     密钥类型
     * @param keyIdentify 密钥识别码
     * @param request     待加密文本
     * @return 加密后文本
     */
    public static String encrypt(EncryptKeyType keyType, String keyIdentify, String request) {
        try {
            String publicKey = getKey(keyType, keyIdentify);
            String encrypted = encode(encrypt(request.getBytes(), publicKey));
            return encrypted.replace("\n", "");
        } catch (Exception e) {
            logger.error("加密失败",e);
            return "加密失败！";
        }
    }

    /**
     * 公钥加密
     *
     * @param data      源数据
     * @param publicKey 公钥(BASE64编码)
     * @return byte[]
     * @throws Exception
     */
    private static byte[] encrypt(byte[] data, String publicKey) throws Exception {
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
        return encryptedData;
    }

    /**
     * 加签
     *
     * @param keyType     密钥类型
     * @param keyIdentify 密钥识别码
     * @param request     待加签文本
     * @return
     */
    public static String sign(EncryptKeyType keyType, String keyIdentify, String request, String signKeyword) {
        Map<String, String> signContentMap = null;
        Gson gson = new GsonBuilder().setPrettyPrinting().disableHtmlEscaping().create();
        try {
//            signContentMap = gson.fromJson(request, Map.class);
//            String privateKey = getKey(keyType, keyIdentify);
//            String signed = sign(getSignContent(signContentMap).getBytes(), privateKey);
            String signed = "";
            signContentMap.put(signKeyword, signed.replace("\n", ""));
            return gson.toJson(signContentMap);
        } catch (Exception e) {
            logger.error("加签失败",e);
            if (signContentMap == null) {
                signContentMap = new HashMap<>();
            }

            signContentMap.put(signKeyword, "加签失败");

            return gson.toJson(signContentMap);
        }
    }

    /**
     * 用私钥对信息生成数字签名
     *
     * @param data       已加密数据
     * @param privateKey 私钥(BASE64编码)
     * @return
     * @throws Exception
     */
    private static String sign(byte[] data, String privateKey) throws Exception {
        byte[] keyBytes = decode(privateKey);
        PKCS8EncodedKeySpec pkcs8KeySpec = new PKCS8EncodedKeySpec(keyBytes);
        KeyFactory keyFactory = KeyFactory.getInstance(KEY_ALGORITHM);
        PrivateKey privateK = keyFactory.generatePrivate(pkcs8KeySpec);
        Signature signature = Signature.getInstance(SIGNATURE_ALGORITHM);
        signature.initSign(privateK);
        signature.update(data);
        return encode(signature.sign());
    }

    /**
     * 封装待验签的内容
     *
     * @param json json字符串
     * @return 封装后文本
     */
//    public static String getSignContent(String json) {
//        return getSignContent(new Gson().fromJson(json, Map.class));
//    }

    /**
     * 封装待验签的内容
     *
     * @param notSorted
     * @return
     */
//    private static String getSignContent(Map<String, String> notSorted) {
//        LinkedMap sorted = new LinkedMap();
//        List<String> keys = new ArrayList<>(notSorted.keySet());
//        Collections.sort(keys);
//        for (int i = 0; i < keys.size(); i++) {
//            String key = keys.get(i);
//            String value = notSorted.get(key).toString();
//            sorted.put(key, value);
//        }
//        return sorted.toString();
//    }

    /**
     * BASE64字符串解码为二进制数据
     *
     * @param base64
     * @return
     * @throws Exception
     */
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

    /**
     * 获取公钥私钥
     *
     * @param keyType     密钥类型
     * @param keyIdentify 密钥识别码
     * @return 密钥
     */
    public static String getKey(EncryptKeyType keyType, String keyIdentify) {
        //删除因为模板产生的/r/n
        if(StringUtil.isNotBlank(keyIdentify)){
            keyIdentify = keyIdentify.trim();
        }
        if (StringUtil.isBlank(keyIdentify) || keyType == null) {
            throw new BusinessException("密钥配置出错，请检查密钥相关配置");
        }

        if (StringUtil.isNotBlank(KEYS.get(keyIdentify + Constants.DIVISION + keyType.getKeyType()))) {
            return KEYS.get(keyIdentify + Constants.DIVISION + keyType.getKeyType());
        }

        return generateKeys(keyType, keyIdentify);
    }

    /**
     * 准备公钥私钥
     *
     * @param keyType     密钥类型
     * @param keyIdentify 密钥识别码
     * @return
     */
//    public static synchronized String generateKeys(EncryptKeyType keyType, String keyIdentify) {
//        String insurerPkFilePath = null;
//        String insurerSkFilePath = null;
//        String insaicPkFilePath = null;
//        String insaicSkFilePath = null;
//
//        if (StringUtil.isNotBlank(System.getProperty(INSURER_PUBLIC_KEY_FILE_PATH))) {
//            insurerPkFilePath = System.getProperty(INSURER_PUBLIC_KEY_FILE_PATH);
//        }
//
//        if (StringUtil.isNotBlank(System.getProperty(INSURER_PRIVATE_KEY_FILE_PATH))) {
//            insurerSkFilePath = System.getProperty(INSURER_PRIVATE_KEY_FILE_PATH);
//        }
//
//        if (StringUtil.isNotBlank(System.getProperty(INSAIC_PUBLIC_KEY_FILE_PATH))) {
//            insaicPkFilePath = System.getProperty(INSAIC_PUBLIC_KEY_FILE_PATH);
//        }
//
//        if (StringUtil.isNotBlank(System.getProperty(INSAIC_PRIVATE_KEY_FILE_PATH))) {
//            insaicSkFilePath = System.getProperty(INSAIC_PRIVATE_KEY_FILE_PATH);
//        }
//
//        if (StringUtil.isBlank(insurerPkFilePath) || StringUtil.isBlank(insurerSkFilePath) || StringUtil.isBlank(insaicPkFilePath) || StringUtil.isBlank(insaicSkFilePath)) {
//            WebApplicationContext applicationContext = ContextLoader.getCurrentWebApplicationContext();
//            CacheManager commonCodeCache;
//            if (applicationContext != null) {
//                commonCodeCache = applicationContext.getBean("commonCodeCacheImpl", CacheManager.class);
//            } else {
//                commonCodeCache = SpringBeanLocator.getBean("commonCodeCacheImpl", CacheManager.class);
//            }
//
//            Map<String, CommonCodeProperty> result = (Map<String, CommonCodeProperty>) commonCodeCache.getAllCache(Constants.INSURER_INTERFACE_CONFIG);
//            if (result != null && !result.isEmpty() && result.get(keyIdentify) != null && result.get(keyIdentify).getMap() != null) {
//                Map<String, String> insuerConfig = result.get(keyIdentify).getMap();
//
//                if (StringUtil.isBlank(insurerPkFilePath) && StringUtil.isNotBlank(insuerConfig.get(INSURER_PUBLIC_KEY_FILE_PATH))) {
//                    insurerPkFilePath = insuerConfig.get(INSURER_PUBLIC_KEY_FILE_PATH);
//                }
//
//                if (StringUtil.isBlank(insurerSkFilePath) && StringUtil.isNotBlank(insuerConfig.get(INSURER_PRIVATE_KEY_FILE_PATH))) {
//                    insurerSkFilePath = insuerConfig.get(INSURER_PRIVATE_KEY_FILE_PATH);
//                }
//
//                if (StringUtil.isBlank(insaicPkFilePath) && StringUtil.isNotBlank(insuerConfig.get(INSAIC_PUBLIC_KEY_FILE_PATH))) {
//                    insaicPkFilePath = insuerConfig.get(INSAIC_PUBLIC_KEY_FILE_PATH);
//                }
//
//                if (StringUtil.isBlank(insaicSkFilePath) && StringUtil.isNotBlank(insuerConfig.get(INSAIC_PRIVATE_KEY_FILE_PATH))) {
//                    insaicSkFilePath = insuerConfig.get(INSAIC_PRIVATE_KEY_FILE_PATH);
//                }
//            }
//
//            if (StringUtil.isBlank(insurerPkFilePath) && StringUtil.isBlank(insurerSkFilePath) && StringUtil.isBlank(insaicPkFilePath) && StringUtil.isBlank(insaicSkFilePath)) {
//                result = (Map<String, CommonCodeProperty>) commonCodeCache.getAllCache(Constants.INSAIC_INSURER_SERIVCE_CONFIG);
//
//                if (result != null && !result.isEmpty() && result.get(keyIdentify) != null && result.get(keyIdentify).getMap() != null && !result.get(keyIdentify).getMap().isEmpty()) {
//                    Map<String, String> insaicServiceConfig = result.get(keyIdentify).getMap();
//
//                    if (StringUtil.isNotBlank(insaicServiceConfig.get(INSURER_PUBLIC_KEY_FILE_PATH))) {
//                        insurerPkFilePath = insaicServiceConfig.get(INSURER_PUBLIC_KEY_FILE_PATH);
//                    }
//
//                    if (StringUtil.isNotBlank(insaicServiceConfig.get(INSURER_PRIVATE_KEY_FILE_PATH))) {
//                        insurerSkFilePath = insaicServiceConfig.get(INSURER_PRIVATE_KEY_FILE_PATH);
//                    }
//
//                    if (StringUtil.isNotBlank(insaicServiceConfig.get(INSAIC_PUBLIC_KEY_FILE_PATH))) {
//                        insaicPkFilePath = insaicServiceConfig.get(INSAIC_PUBLIC_KEY_FILE_PATH);
//                    }
//
//                    if (StringUtil.isNotBlank(insaicServiceConfig.get(INSAIC_PRIVATE_KEY_FILE_PATH))) {
//                        insaicSkFilePath = insaicServiceConfig.get(INSAIC_PRIVATE_KEY_FILE_PATH);
//                    }
//                }
//            }
//        }
//
//        setKey(EncryptKeyType.InsurerPublicKey, keyIdentify, insurerPkFilePath);
//        setKey(EncryptKeyType.InsurerPrivateKey, keyIdentify, insurerSkFilePath);
//        setKey(EncryptKeyType.InsaicPublicKey, keyIdentify, insaicPkFilePath);
//        setKey(EncryptKeyType.InsaicPrivateKey, keyIdentify, insaicSkFilePath);
//
//        if (StringUtil.isNotBlank(KEYS.get(keyIdentify + Constants.DIVISION + keyType.getKeyType()))) {
//            return KEYS.get(keyIdentify + Constants.DIVISION + keyType.getKeyType());
//        } else {
//            throw new BusinessException("获取密钥失败，请检查密钥相关配置！");
//        }
//    }

    /**
     * 设置密钥缓存
     *
     * @param keyType     密钥类型
     * @param keyIdentify 密钥识别码
     * @param keyFilePath 密钥文件位置
     */
    private static void setKey(EncryptKeyType keyType, String keyIdentify, String keyFilePath) {
        if (StringUtil.isNotBlank(keyIdentify) && StringUtil.isNotBlank(keyFilePath) && StringUtil.isBlank(KEYS.get(keyIdentify + Constants.DIVISION + keyType))) {
            try {
                FileInputStream keyFile = new FileInputStream(new File(keyFilePath));
                String keyStr = IOUtils.toString(keyFile, "utf-8");
                keyFile.close();
                KEYS.put(keyIdentify + Constants.DIVISION + keyType.getKeyType(), keyStr);
            } catch (Exception e) {
                logger.error("准备公钥私钥失败！", e);
            }
        }
    }
}