package com.bernie.multyThread;

import com.alibaba.dubbo.common.utils.NamedThreadFactory;
import kafka.javaapi.producer.Producer;
import kafka.producer.KeyedMessage;
import kafka.producer.ProducerConfig;

import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.Properties;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

/**
 * Created by bida on 2016/1/12.
 */
public class ExecutorExample {
    private static String msg = " {" +
            "        \"messageType\": \"ZYYB_ORD\"," +
            "        \"src\": \"\",\"messageId\": \"aa4011c8-1982-41b7-8402-333c6d949f18\",\"messageProcessorName\": null,\"dest\": \"\",\"sendTime\": \"2015-11-02 18:20:18\"," +
            "        \"body\": \"{" +
            "            'deliveryStationId':''," +
            "            'orderType':'1'," +
            "            'sendCity':'1110105'," +
            "            'expectedDeliveryTimePromise':'2015-09-24 10:47:07'," +
            "            'orderId':'${order_id}'," +
            "            'siteName':''," +
            "            'selfServiceId':'1'," +
            "            'packageSpec':'packageSpec'," +
            "            'shipName':'皮特'," +
            "            'expectedDeliveryTimeStart':null," +
            "            'orderItems':[" +
            "                {'lastNum':1,'itemId':13232913383004,'productId':20999128,'salePrice':11.11,'productName':'窗边'}," +
            "                {'lastNum':1,'itemId':13232913383005,'productId':21081984,'salePrice':22.22,'productName':'秘密'}," +
            "                {'lastNum':1,'itemId':13232913383003,'productId':23605048,'salePrice':33.33,'productName':'意林'}," +
            "                {'lastNum':1,'itemId':13232913383001,'productId':23643240,'salePrice':44.44,'productName':'光明'}," +
            "                {'lastNum':1,'itemId':13232913383002,'productId':23696692,'salePrice':55.55,'productName':'城南'}]," +
            "            'packagePos':''," +
            "            'erpSendDate':'2015-09-23 23:59:45'," +
            "            'subOrderId':''," +
            "            'sendFee':5.0," +
            "            'cashs':12.0," +
            "            'coupons':13.0," +
            "            'pointDeductionAmount':14.0," +
            "            'couponsMoney':15.0," +
            "            'money':16.0," +
            "            'giftCoupons':17.0," +
            "            'armoney':47.99," +
            "            'foodsFee':166.65," +
            "            'foodsLastFee':166.65," +
            "            'custId':'174115203'," +
            "            'orgOrderNo':''," +
            "            'packageBarcode':'D1801'," +
            "             'shipRegion':'E001'," +
            "            'shipId':'1'," +
            "            'packageNum':1," +
            "            'shipTel':',17786512829'," +
            "            'custMessage':'custom message'," +
            "            'orderSource':'当当自营订单'," +
            "            'siteCode':'18146'," +
            "            'shipZip':'430000'," +
            "            'rcvStreetId':'111010507'," +
            "            'sendCompany':'99999998'," +
            "            'deliveryNo':'JJD0615092330681'," +
            "            'shipAddress':'参考地址','custRequestSenddate':'自营随意'," +
            "            'ordersErro':''," +
            "            'custEmail':'47901@dd.com'," +
            "            'custType':'0'," +
            "            'mappingTrackingNumber':''," +
            "            'payId':'1'," +
            "            'orderDate':'2015-09-23 10:46:58'}\"" +
            "    }";

    public static void main(String[] args) throws InterruptedException {
        List<String> orderIds = new ArrayList<String>();
        String orderId = new SimpleDateFormat("yyMMddmmssSSS").format(new Date());
        for(int i = 0;i < 50;i++){
            orderIds.add(orderId + i);
        }

        for(String id:orderIds){
            System.out.println(id);
        }
        Properties props = new Properties();

        props.put("metadata.broker.list", "10.3.254.26:9092");
        props.put("serializer.class", "kafka.serializer.StringEncoder");
        props.put("key.serializer.class", "kafka.serializer.StringEncoder");
        props.put("request.required.acks", "-1");

        Producer<String, String> producer = new Producer<String, String>(new ProducerConfig(props));

        ExecutorService es = Executors.newFixedThreadPool(5, new NamedThreadFactory("My Test"));
        List<Callable<String>> tasks = new ArrayList<Callable<String>>();
        for(int i = 0;i < 10;i++){
            tasks.add(() -> {
                for(String orderId1 :orderIds){
                    producer.send(new KeyedMessage<String, String>("IT_ORD_TO_TMS", msg.replace("${order_id}", orderId1)));
                }
                return null;
            });
        }

        es.invokeAll(tasks);

        producer.close();

        es.shutdown();
    }
}
