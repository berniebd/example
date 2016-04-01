package com.bernie.HttpComponents;


import org.apache.http.client.fluent.Executor;
import org.apache.http.client.fluent.Request;
import org.apache.http.entity.ContentType;
import java.io.IOException;

/**
 * Created by saic on 2016/3/24.
 */
public class FluentAPIDemo {
    public static void main(String[] args) throws IOException {
        String content = Request.Get("http://www.baidu.com").connectTimeout(1000).socketTimeout(1000).execute().returnContent().toString();

        Executor executor = Executor.newInstance();
        content = executor.execute(Request.Get("http://www.baidu.com")).returnContent().toString();
        System.out.println(content);

        String data1 = "{\"requestBodyJson\":{\"userCode\":\"dfrrdi\",\"password\":\"Pass1234\",\"redirect\":\"\"},\"transCode\":\"TY1015\"}";
        content = Request.Post("http://10.118.22.41:8010/controller/access").bodyString(data1, ContentType.APPLICATION_JSON)
                .execute().returnContent().toString();
        System.out.println(content);

//        Document result = Request.Get("http://www.baidu.com")
//                .execute().handleResponse(new ResponseHandler<Document>() {
//            public Document handleResponse(final HttpResponse response) throws IOException {
//                StatusLine statusLine = response.getStatusLine();
//                HttpEntity entity = response.getEntity();
//                if(statusLine.getStatusCode() >= 300){
//                    throw new HttpResponseException(
//                            statusLine.getStatusCode(),
//                            statusLine.getReasonPhrase()
//                    );
//                }
//                if(entity == null){
//                    throw new ClientProtocolException("Response contains no content");
//                }
//                DocumentBuilderFactory dbfac = DocumentBuilderFactory.newInstance();
//                DocumentBuilder docBuilder = null;
//                String charset = null;
//                try {
//                    docBuilder = dbfac.newDocumentBuilder();
//                    ContentType contentType = ContentType.getOrDefault(entity);
////                    if(!contentType.equals(ContentType.parse("baiduApp/json; v6.27.2.14; charset=UTF-8"))){
////                        throw new ClientProtocolException("Unexpected content type:" + contentType);
////                    }
//                    charset = contentType.getCharset().toString();
//                    System.out.println(charset);
//                    if(charset == null){
//                        charset = HTTP.DEFAULT_CONTENT_CHARSET;
//                    }
//                    return docBuilder.parse(entity.getContent(), charset);
//
//                } catch (ParserConfigurationException ex) {
//                    throw new IllegalStateException(ex);
//                } catch (SAXException ex) {
//                    throw new ClientProtocolException("Malformed Text document", ex);
//                }
//            }
//        });
    }
}
