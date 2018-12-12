package com.cdedonder.amezzon.parser.dto;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;

import java.util.ArrayList;
import java.util.List;

@SuppressWarnings("unused")
@JsonPropertyOrder({"result_list", "statement_error_messages", "error_messages"})
public class DatabaseStatementResponse {

    @JsonProperty("error_messages")
    private List<ErrorMessageWrapper> errorMessages;
    @JsonProperty("result_list")
    private List<ResultWrapper> resultList;
    @JsonProperty("statement_error_messages")
    private List<String> statementErrorMessages;

    public DatabaseStatementResponse() {
        errorMessages = new ArrayList<>();
        resultList = new ArrayList<>();
        statementErrorMessages = new ArrayList<>();
    }

    @JsonProperty("error_messages")
    public List<ErrorMessageWrapper> getErrorMessages() {
        return errorMessages;
    }

    @JsonProperty("error_messages")
    public void setErrorMessages(List<ErrorMessageWrapper> errorMessages) {
        this.errorMessages = errorMessages;
    }

    @JsonProperty("result_list")
    public List<ResultWrapper> getResultList() {
        return resultList;
    }

    @JsonProperty("result_list")
    public void setResultList(List<ResultWrapper> resultList) {
        this.resultList = resultList;
    }

    @JsonProperty("statement_error_messages")
    public List<String> getStatementErrorMessages() {
        return statementErrorMessages;
    }

    @JsonProperty("statement_error_messages")
    public void setStatementErrorMessages(List<String> statementErrorMessages) {
        this.statementErrorMessages = statementErrorMessages;
    }

    @JsonPropertyOrder({"statement_id", "error_message"})
    public static class ErrorMessageWrapper {

        @JsonProperty("error_message")
        private String errorMessage;
        @JsonProperty("statement_id")
        private String statementId;

        @JsonProperty("error_message")
        public String getErrorMessage() {
            return errorMessage;
        }

        @JsonProperty("error_message")
        public void setErrorMessage(String errorMessage) {
            this.errorMessage = errorMessage;
        }

        @JsonProperty("statement_id")
        public String getStatementId() {
            return statementId;
        }

        @JsonProperty("statement_id")
        public void setStatementId(String statementId) {
            this.statementId = statementId;
        }
    }

    @JsonPropertyOrder({"statement_id", "result_message"})
    public static class ResultWrapper {

        @JsonProperty("statement_id")
        private String statementId;
        @JsonProperty("result_message")
        private QueryResult resultMessage;

        @JsonProperty("statement_id")
        public String getStatementId() {
            return statementId;
        }

        @JsonProperty("statement_id")
        public void setStatementId(String statementId) {
            this.statementId = statementId;
        }

        @JsonProperty("result_message")
        public QueryResult getResultMessage() {
            return resultMessage;
        }

        @JsonProperty("result_message")
        public void setResultMessage(QueryResult resultMessage) {
            this.resultMessage = resultMessage;
        }
    }
}
