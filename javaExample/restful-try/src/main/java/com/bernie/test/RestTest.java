package com.bernie.test;

import org.glassfish.jersey.client.ClientConfig;

import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.client.WebTarget;
import javax.ws.rs.core.Form;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.UriBuilder;
import java.net.URI;

/**
 * Created by bida on 2015/8/6.
 */
public class RestTest {
    public static void main(String[] args){
        ClientConfig config = new ClientConfig();
        Client client = ClientBuilder.newClient(config);
        WebTarget target = client.target(getBaseURI());

        String response = target.path("rest")
                .path("helloworld")
                .request()
                .accept("text/plain")
                .get(Response.class).toString();

        String plainAnswer = target.path("rest").path("helloworld")
                .request()
                .accept("application/xml")
                .get(String.class);

        Form form = new Form();
        form.param("id", "5");
        form.param("summary", "summary 5");
        form.param("description", "description 5");

//        String addTodoAnswe = target.path("rest").path("todos")
//                .request().accept("text.html")
//                .post(Entity.entity(form, MediaType.APPLICATION_FORM_URLENCODED_TYPE), TodosResource.class).getTodos().toString();

        System.out.println(response);
        System.out.println(plainAnswer);
    }

    private static URI getBaseURI(){
        return UriBuilder.fromUri("http://localhost:8080").build();
    }
}
