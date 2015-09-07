package com.bernie.application;


import com.bernie.resource.HelloResource;
import org.codehaus.jackson.jaxrs.JacksonJsonProvider;
import org.glassfish.jersey.filter.LoggingFilter;
import org.glassfish.jersey.server.ResourceConfig;

/**
 * Created by bida on 2015/8/6.
 */
public class APIApplication extends ResourceConfig {
    public APIApplication(){
        register(HelloResource.class);

        register(JacksonJsonProvider.class);

        register(LoggingFilter.class);
    }
}
