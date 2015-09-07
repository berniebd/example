package com.bernie.wiremock;

import com.jayway.restassured.response.Response;
import com.jayway.restassured.specification.RequestSpecification;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.HashMap;
import java.util.Map;

import static com.jayway.restassured.RestAssured.given;


/**
 * Created by bida on 2015/8/6.
 */
public class HTTPRequestor {
    protected static final Logger logger = LoggerFactory.getLogger(HTTPRequestor.class);
    private RequestSpecification reqSpec;

    public HTTPRequestor() {
        reqSpec = given().relaxedHTTPSValidation();
    }

    public HTTPRequestor(String proxy) {
        reqSpec = given().relaxedHTTPSValidation().proxy(proxy);
    }

    public Response performRequest(String url, String method, HashMap<String, String> headers, String body) {
        Response response = null;

        try {
            for (Map.Entry<String, String> entry : headers.entrySet()) {
                reqSpec.header(entry.getKey(), entry.getValue());
            }

            if (method.equals("GET")) {
                response = reqSpec.get(url);
                return response;
            }
            if (method.equals("POST")) {
                response = reqSpec.body(body).post(url);
                return response;
            }
            if (method.equals("PUT")) {
                response = reqSpec.body(body).put(url);
                return response;
            }
            if (method.equals("DELETE")) {
                response = reqSpec.delete(url);
                return response;
            }

            logger.error("Unknown call type : [" + method + "]");
            return response;
        } catch (Exception e) {
            logger.error("Problem performing request: " + e);
        }
        return response;
    }
}

