package com.cdedonder.amezzon.database.mysql;

import com.cdedonder.amezzon.database.DataAccesContext;
import com.cdedonder.amezzon.database.DataAccessException;
import com.cdedonder.amezzon.database.data.*;
import com.cdedonder.amezzon.database.data.mysql.*;

import java.sql.Connection;
import java.sql.SQLException;

public class MySQLDAC implements DataAccesContext {

    private final Connection connection;

    public MySQLDAC(Connection connection) {
        this.connection = connection;
    }

    @Override
    public PersonDAO getPersonDAO() {
        return new MySQLPersonDAO(connection, this);
    }

    @Override
    public PileDAO getPileDAO() {
        return new MySQLPileDAO(connection, this);
    }

    @Override
    public ProductDAO getProductDAO() {
        return new MySQLProductDAO(connection, this);
    }

    @Override
    public ProductTypeDAO getProductTypeDAO() {
        return new MySQLProductTypeDAO(connection, this);
    }

    @Override
    public TransactionDAO getTransactionDAO() {
        return new MySQLTransactionDAO(connection, this);
    }

    @Override
    public TransactionTypeDAO getTransactionTypeDAO() {
        return new MySQLTransactionTypeDAO(connection, this);
    }

    @Override
    public void commit() throws DataAccessException {
        try {
            connection.commit();
        } catch (SQLException e) {
            throw new DataAccessException(e);
        }
    }

    @Override
    public void rollback() throws DataAccessException {
        try {
            connection.rollback();
        } catch (SQLException e) {
            throw new DataAccessException(e);
        }
    }

    @Override
    public void close() throws DataAccessException {
        try {
            connection.close();
        } catch (SQLException e) {
            throw new DataAccessException(e);
        }
    }

    @Override
    public void startTransaction() throws DataAccessException {
        try {
            connection.setAutoCommit(false);
        } catch (SQLException e) {
            throw new DataAccessException(e);
        }
    }

    @Override
    public void endTransaction() throws DataAccessException {
        try {
            connection.setAutoCommit(true);
        } catch (SQLException e) {
            throw new DataAccessException(e);
        }
    }
}
