package com.cdedonder.amezzon.database.data.mysql;

import com.cdedonder.amezzon.database.DataAccessException;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.sql.Statement;

public abstract class MySQLAbstractDAO {

    private final Connection connection;

    public MySQLAbstractDAO(Connection connection) throws DataAccessException {
        this.connection = connection;
        try {
            this.connection.setAutoCommit(false);
        } catch (SQLException e) {
            throw new DataAccessException("Cannot create DAO:\n" + e.getMessage());
        }
    }

    protected Connection getConnection() {
        return connection;
    }

    protected PreparedStatement prepare(String sql) throws SQLException {
        return connection.prepareStatement(sql);
    }

    protected PreparedStatement prepareWithKeys(String sql) throws SQLException {
        return connection.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS);
    }

    protected void commit(boolean atomic) throws SQLException {
        if (atomic) connection.commit();
    }

    protected void rollback() throws SQLException {
        connection.rollback();
    }
}
