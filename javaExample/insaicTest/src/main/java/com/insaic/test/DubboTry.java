package com.insaic.test;

import com.alibaba.dubbo.common.utils.NamedThreadFactory;
import com.alibaba.dubbo.config.ApplicationConfig;
import com.alibaba.dubbo.config.ReferenceConfig;
import com.insaic.base.context.UserProfile;
import com.insaic.claim.model.AppPushRepairInput;
import com.insaic.claim.service.PushRepairInputService;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.*;

/**
 * Created by bida on 2015/11/27.
 */
public class DubboTry {
    public static void main(String[] args) throws InterruptedException, IOException {
        ApplicationConfig application = new ApplicationConfig();
        application.setName("dubbo-test");

        ReferenceConfig<PushRepairInputService> reference = new ReferenceConfig<PushRepairInputService>();
        reference.setUrl("dubbo://10.118.22.31:20830/com.insaic.claim.service.PushRepairInputService");
        reference.setTimeout(500);
        reference.setConnections(10);
        reference.setApplication(application);
        reference.setInterface(PushRepairInputService.class);
        reference.setVersion("1.0.0");

        final PushRepairInputService pushRepairInputService = reference.get();

        UserProfile userProfile = new UserProfile();

        userProfile.setDealerCode("BK20006");
        userProfile.setBrandCode("VW");
        userProfile.setUserName("分配专员");
        userProfile.setManufactory("SVW");
        userProfile.setUserCode("fenpei");
        userProfile.setUserType("dealerGroup");
        userProfile.setProvince("370000");
        userProfile.setCurrentUser();

        List<AppPushRepairInput> appPushRepairInputs = new ArrayList<AppPushRepairInput>();
        AppPushRepairInput       appPushRepair  = new AppPushRepairInput();
        appPushRepair.setSms("天安财产保险股份有限公司");
//        appPushRepair.setSms("中华联合财产保险股份有限公司");
        appPushRepair.setMessageNo("13141315151");
        appPushRepairInputs.add(appPushRepair);

        pushRepairInputService.savePushRepairInputByApp(appPushRepairInputs);

    }
}
