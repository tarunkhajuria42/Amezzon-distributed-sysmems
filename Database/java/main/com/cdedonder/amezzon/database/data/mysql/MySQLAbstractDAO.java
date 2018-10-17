package com.cdedonder.amezzon.database.data.mysql;

import com.cdedonder.amezzon.database.DataAccesContext;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.sql.Statement;

public abstract class MySQLAbstractDAO {

    private final Connection connection;
    private final DataAccesContext dac;

    public MySQLAbstractDAO(Connection connection, DataAccesContext dac) {
        this.connection = connection;
        this.dac = dac;
    }

    protected final PreparedStatement prepare(String sql) throws SQLException {
        return prepare(sql, false);
    }

    protected final PreparedStatement prepare(String sql, boolean keys) throws SQLException {
        return keys ? connection.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS) : connection.prepareStatement(sql);
    }

    protected final DataAccesContext getDataAccesContext() {
        return dac;
    }
}
