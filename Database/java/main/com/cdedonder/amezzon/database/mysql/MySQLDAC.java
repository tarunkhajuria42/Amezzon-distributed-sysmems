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
    public PersonDAO getPersonDAO() throws DataAccessException {
        return new MySQLPersonDAO(connection);
    }

    @Override
    public PileDAO getPileDAO() throws DataAccessException {
        return new MySQLPileDAO(connection);
    }

    @Override
    public ProductDAO getProductDAO() throws DataAccessException {
        return new MySQLProductDAO(connection);
    }

    @Override
    public ProductTypeDAO getProductTypeDAO() {
        return new MySQLProductTypeDAO(connection);
    }

    @Override
    public TransactionDAO getTransactionDAO() {
        return new MySQLTransactionDAO(connection);
    }

    @Override
    public TransactionTypeDAO getTransactionTypeDAO() {
        return new MySQLTransactionTypeDAO(connection);
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


}
