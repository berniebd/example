package com.dangdang.operation.debug;

import com.alibaba.dubbo.config.ApplicationConfig;
import com.alibaba.dubbo.config.ReferenceConfig;
import com.dangdang.express.service.refund.*;

import java.math.BigDecimal;
import java.text.SimpleDateFormat;
import java.util.Date;

/**
 * Created by bida on 2016/1/5.
 */
public class RefundOutServiceDebug {
    private RefundOrder generateRefundOrder(String operation, String orderNo){
        RefundOrder refundOrder = new RefundOrder();
        RefundItem array[] = new RefundItem[2];

        Integer exchangeNo=null;
        Integer returnNo=null;
        Integer lastNo=null;

        if(operation.equals("return")){
            exchangeNo = new Integer("0");
            returnNo = new Integer("1");
            lastNo = new Integer("0");
        }
        if(operation.equals("exchange")){
            exchangeNo = new Integer("1");
            returnNo = new Integer("0");
            lastNo = new Integer("1");
        }
        if(operation.equals("exchangeToReturn")){
            exchangeNo = new Integer("5");
            returnNo = new Integer("0");
            lastNo = new Integer("3");
        }

        RefundItem item1 = new RefundItem();
        item1.setItemId(12767178206001L);
        item1.setExchangeNum(exchangeNo);
        item1.setReturnNum(returnNo);
        item1.setLastNum(lastNo);
        item1.setProductId(20999128L);
        item1.setProductName("窗边");
        item1.setSalePrice(new BigDecimal("11.11"));
        item1.setReplacedProductId(20999128L);
        item1.setReplacedProductName("窗边");
        item1.setReplacedProductType(new Integer(0));

        RefundItem item2 = new RefundItem();
        item2.setItemId(12767178206002L);
        item2.setExchangeNum(exchangeNo);
        item2.setReturnNum(returnNo);
        item2.setLastNum(lastNo);
        item2.setProductId(21081984L);
        item2.setProductName("窗边");
        item2.setSalePrice(new BigDecimal("22.22"));
        item2.setReplacedProductId(21081984L);
        item2.setReplacedProductName("秘密");
        item2.setReplacedProductType(new Integer(0));

        array[0] = item1;
        array[1] = item2;

        refundOrder.setRefundItems(array);

        refundOrder.setOrderType("1");
        refundOrder.setSendCity("1110105");
        refundOrder.setExpectedDeliveryTimePromise(new Date());
        refundOrder.setOrderId(orderNo);
        refundOrder.setSelfServiceId("1");
        refundOrder.setShipName("皮特");
        refundOrder.setOrderItems(array);
        refundOrder.setErpSendDate(new Date());

        refundOrder.setPointDeductionAmount(new BigDecimal(0.0));
        refundOrder.setCustId("174115203");

        refundOrder.setShipRegion("2");
        refundOrder.setShipId("101");
        refundOrder.setPackageNum(new Integer(1));
        refundOrder.setShipTel("17786512829");
        refundOrder.setCustMessage("self operated order by MiddleLayer");
        refundOrder.setOrderSource("当当自营订单");
        refundOrder.setSiteCode("T0003");
        refundOrder.setShipZip("430000");
        refundOrder.setRcvStreetId("111010507");
        refundOrder.setSendCompany("18146");
        refundOrder.setDeliveryNo("JJD0615092330681");

        refundOrder.setShipAddress("参考地址");
        refundOrder.setCustRequestSenddate("自营随意");
        refundOrder.setMoney(new BigDecimal(0.0));
        refundOrder.setCustEmail("47901@dd.com");
        refundOrder.setCustType("0");
        refundOrder.setPayId("1");
        refundOrder.setGiftCoupons(new BigDecimal("16.0"));
        refundOrder.setOrderDate(new Date());
        refundOrder.setSendFee(new BigDecimal(5.0));
        refundOrder.setFoodsFee(new BigDecimal(156.65));
        refundOrder.setCoupons(new BigDecimal(13.00));
        refundOrder.setCashs(new BigDecimal(12.00));
        refundOrder.setGiftCoupons(new BigDecimal(17.00));
        refundOrder.setFoodsLastFee(new BigDecimal(166.65));
        refundOrder.setCouponsMoney(new BigDecimal(15.00));
        refundOrder.setArmoney(new BigDecimal("47.99"));
        refundOrder.setPointDeductionAmount(new BigDecimal(14.0));
        return refundOrder;
    }
    public static void main(String[] args) {
        ApplicationConfig application = new ApplicationConfig();
        application.setName("ErpRefundService");

        ReferenceConfig<RefundOutService> reference = new ReferenceConfig<RefundOutService>();
        reference.setUrl("dubbo://10.255.209.85:20881/com.dangdang.express.service.refund.RefundOutService");

        reference.setTimeout(3500);
        reference.setConnections(10);
        reference.setApplication(application);
        reference.setInterface(RefundOutService.class);
        reference.setVersion("3.1.0.0");
        final RefundOutService refundOutService = reference.get();


        String orderId = new SimpleDateFormat("yyyyMMddhhmmss").format(new Date());
        System.out.println(orderId);
        RefundOutServiceDebug refundOutServiceDebug = new RefundOutServiceDebug();
        String option = "return";
        RefundOrder refundOrder = refundOutServiceDebug.generateRefundOrder(option, orderId);
        refundOutService.acceptWmsRefundOrder(refundOrder, 2015122109);
    }
}
