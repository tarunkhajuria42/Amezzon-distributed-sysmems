package com.cdedonder.amezzon.parser.dto;

import java.util.List;

@SuppressWarnings("unused")
public class DatabaseStatementResponse {

    private List<ErrorMessageWrapper> error_messages;
    private List<ResultWrapper> result_list;

    public List<ErrorMessageWrapper> getError_messages() {
        return error_messages;
    }

    public void setError_messages(List<ErrorMessageWrapper> error_messages) {
        this.error_messages = error_messages;
    }

    public List<ResultWrapper> getResult_list() {
        return result_list;
    }

    public void setResult_list(List<ResultWrapper> result_list) {
        this.result_list = result_list;
    }

    public static class ErrorMessageWrapper {

        private String error_message;
        private int statement_id;

        public String getError_message() {
            return error_message;
        }

        public void setError_message(String error_message) {
            this.error_message = error_message;
        }

        public int getStatement_id() {
            return statement_id;
        }

        public void setStatement_id(int statement_id) {
            this.statement_id = statement_id;
        }
    }

    public static class ResultWrapper {

        private int statement_id;
        private QueryResult result_message;

        public int getStatement_id() {
            return statement_id;
        }

        public void setStatement_id(int statement_id) {
            this.statement_id = statement_id;
        }

        public QueryResult getResult_message() {
            return result_message;
        }

        public void setResult_message(QueryResult result_message) {
            this.result_message = result_message;
        }
    }
}
