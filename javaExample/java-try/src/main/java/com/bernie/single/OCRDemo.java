package com.bernie.single;

import cn.easyproject.easyocr.EasyOCR;
import cn.easyproject.easyocr.ImageType;
import com.meterware.httpunit.GetMethodWebRequest;
import com.meterware.httpunit.WebConversation;
import com.meterware.httpunit.WebRequest;
import com.meterware.httpunit.WebResponse;
import org.apache.http.HttpEntity;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.conn.ssl.*;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.ssl.SSLContextBuilder;
import org.apache.http.util.EntityUtils;
import org.apache.jmeter.config.KeystoreConfig;
import org.xml.sax.SAXException;

import javax.net.ssl.SSLContext;
import java.io.*;
import java.security.KeyManagementException;
import java.security.KeyStore;
import java.security.KeyStoreException;
import java.security.NoSuchAlgorithmException;
import java.security.cert.CertificateException;
import java.security.cert.X509Certificate;
import java.util.Date;

/**
 * Created by bida on 2015/10/13.
 */
public class OCRDemo {
    private EasyOCR e;
    private static final String randCodeUrl = String.format("https://dimtest.insaic.com/captcha?t=%s", new Date().getTime());
    private static final String imagePath = "c:\\Workspace\\tmp.png";

    public OCRDemo() {
        e = new EasyOCR();
//        e.setTesseractPath("C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe");
    }

    public String getRandCodeByHttpComponents() throws IOException, KeyStoreException, NoSuchAlgorithmException, KeyManagementException, CertificateException {
        SSLContext sslContext = new SSLContextBuilder().loadTrustMaterial(null, (x509Certificates, s) -> true).build();
        SSLConnectionSocketFactory sslsf = new SSLConnectionSocketFactory(sslContext);
        CloseableHttpClient client = HttpClients.custom().setSSLSocketFactory(sslsf).build();

        HttpGet httpGet = new HttpGet(randCodeUrl);
        CloseableHttpResponse response = client.execute(httpGet);
        HttpEntity entity = response.getEntity();
        entity.writeTo(new FileOutputStream(new File(imagePath)));
        EntityUtils.consume(entity);

//        String randCode = e.discern(new File(imagePath));
        String randCode = e.discernAndAutoCleanImage(imagePath, ImageType.CAPTCHA_NORMAL);
        System.out.println(randCode);

        return randCode;
    }

    public String getRandCodeByHttpunit() throws IOException, SAXException {
        WebConversation wc = new WebConversation();
        WebRequest request = new GetMethodWebRequest(randCodeUrl);
        WebResponse response = wc.getResponse(request);

        FileOutputStream f = new FileOutputStream(new File(imagePath));
        f.write(response.getBytes());
        f.close();

        String randCode = "";
        randCode = e.discern(new File(imagePath));
        System.out.println(randCode);

        return randCode;
    }

    public static void main(String[] args) throws IOException, SAXException, NoSuchAlgorithmException, KeyStoreException, KeyManagementException, CertificateException {
        OCRDemo demo = new OCRDemo();
        demo.getRandCodeByHttpComponents();
//        demo.getRandCodeByHttpunit();
    }
}
