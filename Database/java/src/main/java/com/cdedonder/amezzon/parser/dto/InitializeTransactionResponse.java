package com.cdedonder.amezzon.parser.dto;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;

import java.util.ArrayList;
import java.util.List;

@SuppressWarnings("unused")
@JsonPropertyOrder({"token", "error_messages"})
public class InitializeTransactionResponse {

    @JsonProperty("error_messages")
    private List<String> errorMessages;
    private String token;

    public InitializeTransactionResponse() {
        errorMessages = new ArrayList<>();
    }

    public String getToken() {
        return token;
    }

    public void setToken(String token) {
        this.token = token;
    }

    @JsonProperty("error_messages")
    public List<String> getErrorMessages() {
        return errorMessages;
    }

    @JsonProperty("error_messages")
    public void setErrorMessages(List<String> errorMessages) {
        this.errorMessages = errorMessages;
    }
}
