package com.cdedonder.amezzon.database.data.mysql;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public abstract class MySQLAbstractDAO {

    private final Connection connection;

    public MySQLAbstractDAO(Connection connection) {
        this.connection = connection;
    }

    protected Connection getConnection() {
        return connection;
    }

    protected PreparedStatement prepare(String sql) throws SQLException {
        return connection.prepareStatement(sql);
    }
}
