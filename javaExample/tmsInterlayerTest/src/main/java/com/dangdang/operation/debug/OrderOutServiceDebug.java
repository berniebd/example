package com.dangdang.operation.debug;

import com.alibaba.dubbo.config.ApplicationConfig;
import com.alibaba.dubbo.config.ReferenceConfig;
import com.alibaba.dubbo.config.RegistryConfig;
import com.dangdang.express.service.order.OrderInfo;
import com.dangdang.express.service.order.OrderItem;
import com.dangdang.express.service.order.OrderOutService;

import java.math.BigDecimal;
import java.text.SimpleDateFormat;
import java.util.Date;

/**
 * Created by bida on 2015/12/18.
 * 一般运单下传
 *
 */
public class OrderOutServiceDebug {
    private OrderInfo generateOrderInfo(String orderNo){
        OrderItem array[] = new OrderItem[2];

        OrderItem item1 = new OrderItem();
        item1.setItemId(13232913383004L);
        item1.setProductId(20999128L);
        item1.setProductName("窗边");
        item1.setSalePrice(new BigDecimal("11.11"));
        item1.setLastNum(new Integer(1));

        OrderItem item2 = new OrderItem();
        item2.setItemId(13232913383005L);
        item2.setProductId(21081984L);
        item2.setProductName("秘密");
        item2.setSalePrice(new BigDecimal("22.22"));
        item2.setLastNum(new Integer(1));

        array[0] = item1;
        array[1] = item2;

        OrderInfo orderInfo = new OrderInfo();

        orderInfo.setOrderType("1");
        orderInfo.setSendCity("1420103");
        orderInfo.setExpectedDeliveryTimePromise(new Date());
        orderInfo.setOrderId(orderNo);
        orderInfo.setSelfServiceId("1");
        orderInfo.setShipName("皮特");
        orderInfo.setOrderItems(array);
        orderInfo.setErpSendDate(new Date());

        orderInfo.setPointDeductionAmount(new BigDecimal(0.0));
        orderInfo.setCustId("174115203");

        orderInfo.setShipRegion("2");
        orderInfo.setShipId("101");
        orderInfo.setPackageNum(new Integer(1));
        orderInfo.setShipTel("17786512829");
        orderInfo.setCustMessage("self operated order by MiddleLayer");
        orderInfo.setOrderSource("当当自营订单");
        orderInfo.setSiteCode("");
        orderInfo.setShipZip("430000");
        orderInfo.setRcvStreetId("111010501");
        orderInfo.setSendCompany("2");
        orderInfo.setDeliveryNo("JJD0615092330681");

        orderInfo.setShipAddress("参考地址");
        orderInfo.setCustRequestSenddate("自营随意");
        orderInfo.setMoney(new BigDecimal(0.0));
        orderInfo.setCustEmail("47901@dd.com");
        orderInfo.setCustType("0");
        orderInfo.setPayId("1");
        orderInfo.setGiftCoupons(new BigDecimal("16.0"));
        orderInfo.setOrderDate(new Date());
        orderInfo.setSendFee(new BigDecimal(5.0));
        orderInfo.setFoodsFee(new BigDecimal(156.65));
        orderInfo.setCoupons(new BigDecimal(13.00));
        orderInfo.setCashs(new BigDecimal(12.00));
        orderInfo.setGiftCoupons(new BigDecimal(17.00));
        orderInfo.setFoodsLastFee(new BigDecimal(166.65));
        orderInfo.setCouponsMoney(new BigDecimal(15.00));
        orderInfo.setArmoney(new BigDecimal("47.99"));
        orderInfo.setPointDeductionAmount(new BigDecimal(14.0));

        return orderInfo;
    }
    public static void main(String[] args) throws InterruptedException {
        ApplicationConfig application = new ApplicationConfig();
        application.setName("orderOutService");

//        RegistryConfig registryConfig = new RegistryConfig();
//        registryConfig.setAddress("10.255.209.85:2181");

        ReferenceConfig<OrderOutService> reference = new ReferenceConfig<OrderOutService>();
        reference.setUrl("dubbo://10.255.209.85:20880/com.dangdang.express.service.order.OrderOutService");
//        reference.setRegistry(registryConfig);
        reference.setTimeout(3500);
        reference.setConnections(10);
        reference.setApplication(application);
        reference.setInterface(OrderOutService.class);
        reference.setVersion("3.1.0.0");
        reference.setOwner("bernie");

        final OrderOutService orderOutService = reference.get();

        OrderOutServiceDebug orderOutServiceDebug = new OrderOutServiceDebug();

        String orderId = new SimpleDateFormat("yyyyMMddhhmmss").format(new Date());
        OrderInfo orderInfo = orderOutServiceDebug.generateOrderInfo(orderId);
        orderOutService.acceptWmsOutOrders(orderInfo, 2015122109);
        System.out.println(orderId);
    }
}
