package com.cdedonder.amezzon.database.data.mysql;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.sql.Statement;

public abstract class MySQLAbstractDAO {

    private final Connection connection;

    public MySQLAbstractDAO(Connection connection) {
        this.connection = connection;
    }

    protected PreparedStatement prepare(String sql) throws SQLException {
        return prepare(sql, false);
    }

    protected PreparedStatement prepare(String sql, boolean keys) throws SQLException {
        return keys ? connection.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS) : connection.prepareStatement(sql);
    }
}
