package com.cdedonder.amezzon.parser.dto;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;

import java.util.List;

@SuppressWarnings("unused")
@JsonPropertyOrder({"transaction_token", "statement_list"})
public class DatabaseStatementRequest {

    @JsonProperty("statement_list")
    private List<StatementWrapper> statementList;
    @JsonProperty("transaction_token")
    private String transactionToken;

    @JsonProperty("statement_list")
    public List<StatementWrapper> getStatementList() {
        return statementList;
    }

    @JsonProperty("statement_list")
    public void setStatementList(List<StatementWrapper> statementList) {
        this.statementList = statementList;
    }

    @JsonProperty("transaction_token")
    public String getTransactionToken() {
        return transactionToken;
    }

    @JsonProperty("transaction_token")
    public void setTransactionToken(String transactionToken) {
        this.transactionToken = transactionToken;
    }

    public static class StatementWrapper {
        @JsonProperty("statement_id")
        private String statementId;
        private String statement;

        @JsonProperty("statement_id")
        public String getStatementId() {
            return statementId;
        }

        @JsonProperty("statement_id")
        public void setStatementId(String statementId) {
            this.statementId = statementId;
        }

        public String getStatement() {
            return statement;
        }

        public void setStatement(String statement) {
            this.statement = statement;
        }
    }
}
