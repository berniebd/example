package com.bernie.json;

import org.json.JSONArray;
import org.json.JSONObject;
import org.json.JSONStringer;

/**
 * Created by bida on 2015/8/6.
 */
public class JSONTry {
    public void jsonStringerTest(){
        JSONStringer jsonStringer = new JSONStringer();

        JSONObject obj6 = new JSONObject();
        obj6.put("title", "book1").put("price", "$11");
        JSONObject obj3 = new JSONObject();
        obj3.put("book", obj6);
        obj3.put("author", new JSONObject().put("name", "author-1"));

        JSONObject obj5 = new JSONObject();
        obj5.put("title", "book2").put("price", "$22");
        JSONObject obj4 = new JSONObject();
        obj4.put("book", obj5);
        obj4.put("author", new JSONObject().put("name", "author-2"));

        JSONArray obj2 = new JSONArray();
        obj2.put(obj3).put(obj4);

        JSONObject obj1 = new JSONObject();
        obj1.put("title", "BOOK");
        obj1.put("signing", obj2);

        jsonStringer.object().key("session").value(obj1).endObject();
        System.out.println(jsonStringer.toString());
    }
    public static void main(String[] args){
        JSONTry jsonTry = new JSONTry();
        jsonTry.jsonStringerTest();
    }
}
