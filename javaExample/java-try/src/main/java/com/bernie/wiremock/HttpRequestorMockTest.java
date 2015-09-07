package com.bernie.wiremock;

import com.github.tomakehurst.wiremock.WireMockServer;
import com.github.tomakehurst.wiremock.client.WireMock;
import com.jayway.restassured.response.Response;
import org.testng.Assert;
import org.testng.ITest;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;

import java.util.HashMap;

import static com.github.tomakehurst.wiremock.client.WireMock.*;
import static com.github.tomakehurst.wiremock.core.WireMockConfiguration.wireMockConfig;
import static org.testng.Assert.fail;

/**
 * Created by bida on 2015/8/6.
 */
public class HttpRequestorMockTest implements ITest {
    private WireMockServer wireMockServer;

    public String getTestName() {
        return "Mock Test";
    }

    public HttpRequestorMockTest() {
        wireMockServer = new WireMockServer(wireMockConfig().port(8090));
        WireMock.configureFor("localhost", 8090);
        wireMockServer.start();
    }

    @BeforeTest
    public void stubRequests() {
        stubFor(get(urlEqualTo("/cars/Chevy"))
                        .withHeader("Accept", equalTo("application/json"))
                        .withHeader("User-Agent", equalTo("Jakarta Commons-HttpClient/3.1"))
                        .willReturn(aResponse()
                                        .withHeader("content-type", "application/json")
                                        .withStatus(200)
                                        .withBody("{\"message\":\"Chevy car response body\"}")
                        )
        );

        stubFor(post(urlEqualTo("/cars/Mini"))
                        .withHeader("Authorization", equalTo("Basic d8d74jf82o929d"))
                        .withHeader("Accept", equalTo("application/json"))
                        .withHeader("User-Agent", equalTo("Jakarta Commons-HttpClient/3.1"))
                        .withRequestBody(equalTo("Mini Cooper"))
                        .willReturn(aResponse()
                                        .withHeader("content-type", "application/json")
                                        .withStatus(200)
                                        .withBody("{\"message\":\"Mini Cooper car response body\", \"success\":true}")
                        )
        );
    }

    @Test
    public void testGetMethod() {
        String url = "http://localhost:8090/cars/Chevy";
        String method = "GET";
        String body = "";

        HashMap<String, String> headers = new HashMap<String, String>();
        headers.put("Accept", "application/json");
        headers.put("User-Agent", "Jakarta Commons-HttpClient/3.1");

        HTTPRequestor httpRequestor = new HTTPRequestor();
        Response response = null;

        try {
            response = httpRequestor.performRequest(url, method, headers, body);
        } catch (Exception e) {
            fail("Problem using HTTPRequeswtor to generate response : " + e.getMessage());
        }

        Assert.assertEquals(200, response.getStatusCode());
//        Assert.assertEquals("Chevy car response body", response.jsonPath().getString("message"));
    }

    @Test
    public void testPostMethod() {
        String url = "http://localhost:8090/cars/Mini";
        String method = "POST";
        String body = "Mini Cooper";

        HashMap<String, String> headers = new HashMap<String, String>();
        headers.put("Authorization", "Basic d8d74jf82o929d");
        headers.put("Accept", "application/json");
        headers.put("User-Agent", "Jakarta Commons-HttpClient/3.1");

        HTTPRequestor httpRequestor = new HTTPRequestor();
        Response response = null;

        try {
            response = httpRequestor.performRequest(url, method, headers, body);
        } catch (Exception e) {
            fail("Problem using HttpRequestor to generate response :" + e.getMessage());
        }

        Assert.assertEquals(200, response.getStatusCode());
//        Assert.assertEquals("Mini Cooper car response body", response.jsonPath().get("message"));
    }

    @AfterTest
    public void tearDown() {
        wireMockServer.stop();
        wireMockServer.shutdown();
    }
}
