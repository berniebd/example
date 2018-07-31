package com.bernie.aspectTry;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.EnableAspectJAutoProxy;

@Configuration
//@ComponentScan(basePackages = "com.bernie.aspectTry")
@EnableAspectJAutoProxy
public class ConcertConfig {
    @Bean
    public AudienceAspect audience(){
        return new AudienceAspect();
    }

    @Bean
    public Performance jonePerformance(){
        return new JonePerformance();
    }

    @Bean
    public DecoratorAspect encoreableAspect(){return new DecoratorAspect();}
}
