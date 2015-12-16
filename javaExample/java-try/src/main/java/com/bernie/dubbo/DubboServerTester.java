package com.bernie.dubbo;

import com.alibaba.dubbo.config.ApplicationConfig;
import com.alibaba.dubbo.config.ProtocolConfig;
import com.alibaba.dubbo.config.RegistryConfig;
import com.alibaba.dubbo.config.ServiceConfig;

import java.io.IOException;

/**
 * Created by bida on 2015/11/27.
 */
public class DubboServerTester {
    public static void main(String[] args) throws IOException {
        DemoService demoService = new DemoServiceImpl();
        ApplicationConfig application = new ApplicationConfig();
        application.setName("dubbo-test");

        ProtocolConfig protocol = new ProtocolConfig();
        protocol.setName("dubbo");
        protocol.setPort(8989);
        protocol.setThreads(200);

//        RegistryConfig registry = new RegistryConfig();
//        registry.setAddress("192.168.122.114:9090");
//        registry.setUsername("aaa");
//        registry.setPassword("bbb");

        ServiceConfig<DemoService> service = new ServiceConfig<DemoService>();
        service.setApplication(application);

        service.setRegister(false);
        service.setProtocol(protocol);
        service.setInterface(DemoService.class);
        service.setRef(demoService);
        service.setVersion("1.0.0");

        service.export();
        service.getExportedUrls().stream().forEach(System.out::println);
        System.out.println("press any key to exit.");
        System.in.read();
    }
}
