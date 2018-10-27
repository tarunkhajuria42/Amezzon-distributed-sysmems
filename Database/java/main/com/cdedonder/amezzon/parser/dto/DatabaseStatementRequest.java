package com.cdedonder.amezzon.parser.dto;

import java.util.List;

@SuppressWarnings("unused")
public class DatabaseStatementRequest {

    private List<StatementWrapper> statement_list;
    private String transaction_token;

    public List<StatementWrapper> getStatement_list() {
        return statement_list;
    }

    public void setStatement_list(List<StatementWrapper> statement_list) {
        this.statement_list = statement_list;
    }

    public String getTransaction_token() {
        return transaction_token;
    }

    public void setTransaction_token(String transaction_token) {
        this.transaction_token = transaction_token;
    }

    public static class StatementWrapper {
        private int statement_id;
        private String statement;

        public int getStatement_id() {
            return statement_id;
        }

        public void setStatement_id(int statement_id) {
            this.statement_id = statement_id;
        }

        public String getStatement() {
            return statement;
        }

        public void setStatement(String statement) {
            this.statement = statement;
        }
    }
}
