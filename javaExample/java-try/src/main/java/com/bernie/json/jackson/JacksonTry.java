package com.bernie.json.jackson;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JavaType;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.dataformat.xml.XmlMapper;

import java.io.IOException;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.List;

/**
 * Created by bida on 2015/8/20.
 */
public class JacksonTry {
    private User user = new User();
    private User user2 = new User();
    private SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd");
    private List<User> users = new ArrayList<User>();

    public JacksonTry() throws ParseException {
        user.setName("bernie");
        user.setAge(22);
        user.setEmail("test@example.com");
        user.setBirthday(format.parse("2015-08-20"));

        user2.setName("leilei");
        user2.setAge(21);
        user2.setEmail("leilei@example.com");
        user2.setBirthday(format.parse("2012-08-20"));

        users.add(user);
        users.add(user2);
    }

    private void java2xml() throws IOException {
        System.out.println("************************java 2 xml");
        XmlMapper mapper = new XmlMapper();
        System.out.println(user.getEmail());
        System.out.println(mapper.writeValueAsString(user));
    }
    private void java2json() throws ParseException, JsonProcessingException {
        System.out.println("************************java 2 json");
        ObjectMapper mapper = new ObjectMapper();
        System.out.println(mapper.writeValueAsString(user));
        System.out.println(mapper.writeValueAsString(users));
    }

    private void json2Java() throws IOException {
        System.out.println("************************* json 2 java");
        String json = "{\"name\":\"bernie\",\"mail\":\"test@example.com\",\"birthday\":1440000000000}";
        String jsonList = "[{\"name\":\"bernie\",\"mail\":\"test@example.com\",\"birthday\":1440000000000}," +
                "{\"name\":\"leilei\",\"mail\":\"ttt@example.com\",\"birthday\":1440000000000}]";

//        json String 2 Java class
        ObjectMapper mapper = new ObjectMapper();
        User user = mapper.readValue(json, User.class);
        System.out.println(user.getEmail());
        System.out.println(user.getAge());

//        json list String 2 java List
        JavaType javaType = mapper.getTypeFactory().constructCollectionType(List.class, User.class);
        List<User> userList = (List<User>)mapper.readValue(jsonList, javaType);
        for(User usr:userList){
            System.out.println(usr.getName());
        }
    }

    public static void main(String[] args) throws ParseException, IOException {
        JacksonTry jacksonTry = new JacksonTry();
        jacksonTry.java2json();
        jacksonTry.json2Java();
        jacksonTry.java2xml();
    }
}
