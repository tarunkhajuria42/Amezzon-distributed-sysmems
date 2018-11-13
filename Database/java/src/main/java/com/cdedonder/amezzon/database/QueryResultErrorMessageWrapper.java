package com.cdedonder.amezzon.database;

import com.cdedonder.amezzon.parser.dto.QueryResult;

public class QueryResultErrorMessageWrapper {
    private QueryResult queryResult;
    private String error_message;

    public QueryResult getQueryResult() {
        return queryResult;
    }

    public void setQueryResult(QueryResult queryResult) {
        this.queryResult = queryResult;
    }

    public String getError_message() {
        return error_message;
    }

    public void setError_message(String error_message) {
        this.error_message = error_message;
    }
}
