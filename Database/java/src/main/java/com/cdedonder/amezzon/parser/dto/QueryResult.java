package com.cdedonder.amezzon.parser.dto;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;

import java.util.List;

@SuppressWarnings("unused")
@JsonPropertyOrder({"column_names", "column_types", "rows"})
public class QueryResult {

    @JsonProperty("column_names")
    private List<String> columnNames;
    @JsonProperty("column_types")
    private List<String> columnTypes;
    private List<List<String>> rows;

    @JsonProperty("column_names")
    public List<String> getColumnNames() {
        return columnNames;
    }

    @JsonProperty("column_names")
    public void setColumnNames(List<String> columnNames) {
        this.columnNames = columnNames;
    }

    @JsonProperty("column_types")
    public List<String> getColumnTypes() {
        return columnTypes;
    }

    @JsonProperty("column_types")
    public void setColumnTypes(List<String> columnTypes) {
        this.columnTypes = columnTypes;
    }

    public List<List<String>> getRows() {
        return rows;
    }

    public void setRows(List<List<String>> rows) {
        this.rows = rows;
    }
}
