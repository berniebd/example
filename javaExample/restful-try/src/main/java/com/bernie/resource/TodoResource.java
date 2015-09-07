package com.bernie.resource;

import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.Request;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.UriInfo;
import javax.xml.bind.JAXBElement;

/**
 * Created by bida on 2015/8/6.
 */
public class TodoResource {
    @Context
    UriInfo uriInfo;
    @Context
    Request request;
    String id;

    public TodoResource(UriInfo uriInfo, Request request, String id) {
        this.uriInfo = uriInfo;
        this.request = request;
        this.id = id;
    }

    @GET
    @Produces("application/xml")
    public ToDo getTodoHTML(){
        ToDo todo = TodoDao.instance.getModel().get(id);
        if (todo == null)
            throw new RuntimeException("Get: Todo with " + id + "not found");
        return todo;
    }
    @PUT
    @Consumes("application/xml")
    public Response putTodo(JAXBElement<ToDo> todo) {
        ToDo c = todo.getValue();
        return putAndGetResponse(c);
    }

    @DELETE
    public void deleteTodo() {
        ToDo c = TodoDao.instance.getModel().remove(id);
        if(c==null)
            throw new RuntimeException("Delete: Todo with " + id +  " not found");
    }

    private Response putAndGetResponse(ToDo todo) {
        Response res;
        if(TodoDao.instance.getModel().containsKey(todo.getId())) {
            res = Response.noContent().build();
        } else {
            res = Response.created(uriInfo.getAbsolutePath()).build();
        }
        TodoDao.instance.getModel().put(todo.getId(), todo);
        return res;
    }
}
