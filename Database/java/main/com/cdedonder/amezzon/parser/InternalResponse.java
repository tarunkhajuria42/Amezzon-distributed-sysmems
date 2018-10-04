package com.cdedonder.amezzon.parser;

public class InternalResponse {

    private int responseCode;
    private String responseBody;

    public InternalResponse() {
        responseCode = 0;
        responseBody = "";
    }

    public String getResponseBody() {
        return responseBody;
    }

    public void setResponseBody(String responseBody) {
        this.responseBody = responseBody;
    }

    public int getResponseCode() {
        return responseCode;
    }

    public void setResponseCode(int responseCode) {
        this.responseCode = responseCode;
    }
}
