package com.cdedonder.amezzon.parser.dto;

import java.util.List;

@SuppressWarnings("unused")
public class InitializeTransactionResponse {

    private List<String> error_messages;
    private String token;

    public String getToken() {
        return token;
    }

    public void setToken(String token) {
        this.token = token;
    }

    public List<String> getError_messages() {
        return error_messages;
    }

    public void setError_messages(List<String> error_messages) {
        this.error_messages = error_messages;
    }
}
