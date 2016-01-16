package com.dangdang.operation.debug;

import com.alibaba.dubbo.config.ApplicationConfig;
import com.alibaba.dubbo.config.ReferenceConfig;
import com.alibaba.dubbo.config.RegistryConfig;
import com.dangdang.express.service.refund.*;

import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

/**
 * Created by bida on 2016/1/5.
 * 仓库退货签收
 */
public class ErpRefundServiceDebug {
    private RefundQueueInfo generateRefundOrder(String orderId, String operation){
        List<RefundItem> items = new ArrayList<RefundItem>();
        RefundItem item1 = new RefundItem();
        item1.setItemId(12767178206001L);

        item1.setProductId(20999128L);
        item1.setReplacedProductId(20999128L);
        item1.setProductName("窗边");
        item1.setReplacedProductName("窗边");
        item1.setReplacedProductType(new Integer(1));
        item1.setSalePrice(new BigDecimal(11.11));

        RefundItem item2 = new RefundItem();
        item2.setItemId(12767178206002L);

        item2.setProductId(21081984L);
        item2.setReplacedProductId(21081984L);
        item2.setProductName("秘密");
        item2.setReplacedProductName("秘密");
        item2.setReplacedProductType(new Integer(1));
        item2.setSalePrice(new BigDecimal(22.22));

        if (operation.equals("exchange")){
            item1.setExchangeNum(new Integer(1));
            item1.setReturnNum(new Integer(0));
            item1.setLastNum(new Integer(1));
            item2.setExchangeNum(new Integer(1));
            item2.setReturnNum(new Integer(0));
            item2.setLastNum(new Integer(1));
        }
        if (operation.equals("return")){
            item1.setExchangeNum(new Integer(0));
            item1.setReturnNum(new Integer(1));
            item1.setLastNum(new Integer(0));
            item2.setExchangeNum(new Integer(0));
            item2.setReturnNum(new Integer(1));
            item2.setLastNum(new Integer(0));
        }
        if (operation.equals("exchangeToReturn")){
            item1.setExchangeNum(new Integer(5));
            item1.setReturnNum(new Integer(0));
            item1.setLastNum(new Integer(3));
            item2.setExchangeNum(new Integer(5));
            item2.setReturnNum(new Integer(0));
            item2.setLastNum(new Integer(3));
        }
        items.add(item1);
        items.add(item2);


        RefundQueueInfo refundQueueInfo = new RefundQueueInfo();
        refundQueueInfo.setOrderId(orderId);
        refundQueueInfo.setCreationDate(new Date());
        refundQueueInfo.setRefundItems(items);
        return refundQueueInfo;
    }
    public static void main(String[] args) throws InterruptedException {
        ApplicationConfig application = new ApplicationConfig();
        application.setName("ErpRefundService");

//        RegistryConfig registryConfig = new RegistryConfig();
//        registryConfig.setAddress("10.255.209.85:2181");
//        registryConfig.setAddress("10.3.255.137:2181");


        ReferenceConfig<ErpRefundService> reference = new ReferenceConfig<ErpRefundService>();
//        reference.setRegistry(registryConfig);
        reference.setUrl("dubbo://10.255.209.85:20881/com.dangdang.express.service.refund.ErpRefundService");
        reference.setTimeout(3500);
        reference.setConnections(10);
        reference.setApplication(application);
        reference.setInterface(ErpRefundService.class);
        reference.setVersion("3.0.0.0");
        final ErpRefundService erpRefundService = reference.get();

        String orderId = "20160107091336";
        ErpRefundServiceDebug erpRefundServiceDebug = new ErpRefundServiceDebug();
        RefundQueueInfo refundQueueInfo = erpRefundServiceDebug.generateRefundOrder(orderId, "exchangeToReturn");
        erpRefundService.erpRefundNotice(refundQueueInfo, 2015122109);
    }
}
