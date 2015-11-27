package com.bernie.dubbo;

import com.alibaba.dubbo.common.utils.NamedThreadFactory;
import com.alibaba.dubbo.config.ApplicationConfig;
import com.alibaba.dubbo.config.ReferenceConfig;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.*;

/**
 * Created by bida on 2015/11/27.
 */
public class DubboClientTester {
    public static void main(String[] args) throws InterruptedException, IOException {
        ApplicationConfig application = new ApplicationConfig();
        application.setName("dubbo-test");

        ReferenceConfig<DemoService> reference = new ReferenceConfig<DemoService>();
        reference.setUrl("dubbo://127.0.0.1:8989/com.bernie.dubbo.DemoService");
        reference.setTimeout(500);
        reference.setConnections(10);
        reference.setApplication(application);
        reference.setInterface(DemoService.class);
        reference.setVersion("1.0.0");

        final DemoService demoService = reference.get();

        long begin = System.currentTimeMillis();
        System.out.println(demoService.sayHello("bernie"));
        long end = System.currentTimeMillis();
        System.out.println("cost: " + (end - begin));

        ExecutorService es = Executors.newFixedThreadPool(50, new NamedThreadFactory("My Test"));
        List<Callable<String>> tasks = new ArrayList<Callable<String>>();
        for (int i = 0; i < 100000;++i) {
           tasks.add(new Callable<String>() {
               @Override
               public String call() throws Exception {
                   System.out.println("run");
                   System.out.println(demoService.sayHello("bernie"));
                   System.out.println("run success");
                   return null;
               }
           });
        }

        List<Future<String>> futureList = es.invokeAll(tasks);
        for (Future<String> future : futureList) {
            try {
                String result = future.get();
            } catch (ExecutionException e){
                e.printStackTrace();
            }
        }

        es.shutdown();
        System.out.println("end");
        System.in.read();
    }
}
