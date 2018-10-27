package com.cdedonder.amezzon.parser.dto;

import java.util.List;

@SuppressWarnings("unused")
public class QueryResult {

    private List<String> column_names;
    private List<String> column_types;
    private List<List<String>> rows;

    public List<String> getColumn_names() {
        return column_names;
    }

    public void setColumn_names(List<String> column_names) {
        this.column_names = column_names;
    }

    public List<String> getColumn_types() {
        return column_types;
    }

    public void setColumn_types(List<String> column_types) {
        this.column_types = column_types;
    }

    public List<List<String>> getRows() {
        return rows;
    }

    public void setRows(List<List<String>> rows) {
        this.rows = rows;
    }
}
