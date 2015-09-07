package com.bernie.resource;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;

/**
 * Created by bida on 2015/8/6.
 */
@Path("/helloworld")
public class HelloResource {
//    ����Ϊ�����restʵ���࣬����ֻ����һ������Ϊ���һ��������Ч
    @GET
    @Produces("text/plain")
    public String sayPlainHello(){ return "Hello Jersey plain"; }

    @GET
    @Produces("application/xml")
    public String sayXMLHello(){
        return "<?xml version=\"1.0\"?>" + "<hello> Hello Jersey xml" + "</hello>";
    }

//    @GET
//    @Produces("text/html")
//    public String sayHtmlHello() {
//        return "<html> " + "<title>" + "Hello Jersey html" + "</title>"
//                + "<body><h1>" + "Hello html Jersey" + "</body></h1>" + "</html> ";
//    }
}
