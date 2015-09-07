package com.bernie.json;

import com.jayway.jsonassert.JsonAssert;
import com.jayway.jsonpath.Criteria;
import com.jayway.jsonpath.Filter;
import com.jayway.jsonpath.JsonPath;
import org.hamcrest.Matchers;
import java.util.List;
import static com.jayway.jsonassert.JsonAssert.collectionWithSize;
import static com.jayway.jsonassert.JsonAssert.emptyCollection;
import static com.jayway.jsonassert.JsonAssert.with;
import static com.jayway.jsonpath.Criteria.where;
import static com.jayway.jsonpath.Filter.filter;
import static org.hamcrest.core.Is.is;
import static org.hamcrest.core.IsCollectionContaining.hasItems;
import static org.hamcrest.core.IsEqual.equalTo;

/**
 * Created by bida on 2015/8/4.
 */
public class JsonPathTry {
    private static String jsonString = "{ \"store\": {\n" +
            "    \"book\": [ \n" +
            "      { \"category\": \"reference\",\n" +
            "        \"author\": \"Nigel Rees\",\n" +
            "        \"title\": \"Sayings of the Century\",\n" +
            "        \"price\": 8.95\n" +
            "      },\n" +
            "      { \"category\": \"fiction\",\n" +
            "        \"author\": \"Evelyn Waugh\",\n" +
            "        \"title\": \"Sword of Honour\",\n" +
            "        \"price\": 12.99\n" +
            "      },\n" +
            "      { \"category\": \"fiction\",\n" +
            "        \"author\": \"Herman Melville\",\n" +
            "        \"title\": \"Moby Dick\",\n" +
            "        \"isbn\": \"0-553-21311-3\",\n" +
            "        \"price\": 8.99\n" +
            "      },\n" +
            "      { \"category\": \"fiction\",\n" +
            "        \"author\": \"J. R. R. Tolkien\",\n" +
            "        \"title\": \"The Lord of the Rings\",\n" +
            "        \"isbn\": \"0-395-19395-8\",\n" +
            "        \"price\": 22.99\n" +
            "      }\n" +
            "    ],\n" +
            "    \"bicycle\": {\n" +
            "      \"color\": \"red\",\n" +
            "      \"price\": 19.95\n" +
            "    }\n" +
            "  }\n" +
            "}";

    public static void main(String[] args){
        String author = JsonPath.read(jsonString, "$.store.book[1].author");
        List<String> authors = JsonPath.read(jsonString, "$.store.book[*].author");

        List<Object> books = JsonPath.read(jsonString, "$.store.book[?(@.category == 'reference')]");
        books = JsonPath.read(jsonString, "$.store.book[?]", filter(where("category").is("reference")));

        books = JsonPath.read(jsonString, "$.store.book[?(@.isbn)]");
        books = JsonPath.read(jsonString, "$.store.book[?]", filter(where("isbn").exists(true)));

        books = JsonPath.read(jsonString, "$.store.book[?(@.price > 10)]");
        books = JsonPath.read(jsonString, "$.store.book[?]", filter(where("price").gt(10)));

        Filter filter = Filter.filter(Criteria.where("isbn").exists(true).and("category").in("fiction", "reference"));
        books = JsonPath.read(jsonString, "$.store.book[?]", filter);

        List<Double> prices = JsonPath.read(jsonString, "$..price");

//        Compiled path
        JsonPath path = JsonPath.compile("$.store.book[*]");
        books = path.read(jsonString);

//        Assert
        JsonAssert.with(jsonString)
                .assertThat("$.store.bicycle.color", Matchers.equalTo("red"))
                .assertThat("$.store.bicycle.price", Matchers.equalTo(19.95D));

        with(jsonString)
                .assertThat("$..author", hasItems("Nigel Rees1", "Evelyn Waugh"))
                .assertThat("$..author", is(collectionWithSize(equalTo(2))));

        with(jsonString).assertThat("$.store.book[?(@.category == 'reference')]", emptyCollection());
    }
}

