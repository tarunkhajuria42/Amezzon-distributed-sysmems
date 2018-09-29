package com.cdedonder.amezzon.parser;

public class Messsage {

    private final String method, body;
    private String responseBody;
    private int responseCode;

    public Messsage(String method, String body) {
        this.method = method;
        this.body = body;
    }

    String getMethod() {
        return method;
    }

    String getBody() {
        return body;
    }

    public String getResponseBody() {
        return responseBody;
    }

    void setResponseBody(String responseBody) {
        this.responseBody = responseBody;
    }

    public int getResponseCode() {
        return responseCode;
    }
}
