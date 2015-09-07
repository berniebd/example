package com.bernie.resource;

import javax.servlet.http.HttpServletResponse;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Request;
import javax.ws.rs.core.UriInfo;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * Created by bida on 2015/8/6.
 */
@Path("/todos")
public class TodosResource {
//    Allows to insert contextual objects into the class,
    // e.g. ServletContext, Request, Response, UriInfo
    @Context
    UriInfo uriInfo;
    @Context
    Request request;

    // Return the list of todos to the user in the browser
    @GET
    @Produces("text/xml")
    public List<ToDo> getTodosBrowser() {
        List<ToDo> todos = new ArrayList<ToDo>();
        todos.addAll(TodoDao.instance.getModel().values());
        return todos;
    }

    // Return the list of todos for applications
    @GET
    @Produces({"application/xml","application/json"})
    public List<ToDo> getTodos() {
        List<ToDo> todos = new ArrayList<ToDo>();
        todos.addAll(TodoDao.instance.getModel().values());
        return todos;
    }

    // retuns the number of todos
    // Use http://localhost:8080/com.vogella.jersey.todo/rest/todos/count
    // to get the total number of records
    @GET
    @Path("count")
    @Produces("text/plain")
    public String getCount() {
        int count = TodoDao.instance.getModel().size();
        return String.valueOf(count);
    }

    @POST
    @Produces("text/html")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    public void newTodo(@FormParam("id") String id,
                        @FormParam("summary") String summary,
                        @FormParam("description") String description,
                        @Context HttpServletResponse servletResponse) throws IOException {
        ToDo todo = new ToDo(id, summary);
        if (description != null) {
            todo.setDescription(description);
        }
        TodoDao.instance.getModel().put(id, todo);

        servletResponse.sendRedirect("../create_todo.html");
    }

    // Defines that the next path parameter after todos is
    // treated as a parameter and passed to the TodoResources
    // Allows to type http://localhost:8080/com.vogella.jersey.todo/rest/todos/1
    // 1 will be treaded as parameter todo and passed to TodoResource
    @Path("{todo}")
    public TodoResource getTodo(@PathParam("todo") String id) {
        return new TodoResource(uriInfo, request, id);
    }
}
