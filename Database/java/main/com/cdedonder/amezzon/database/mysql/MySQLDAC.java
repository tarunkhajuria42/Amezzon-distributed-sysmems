package com.cdedonder.amezzon.database.mysql;

import com.cdedonder.amezzon.database.DataAccesContext;
import com.cdedonder.amezzon.database.DataAccessException;
import com.cdedonder.amezzon.database.data.*;

import java.sql.Connection;
import java.sql.SQLException;

public class MySQLDAC implements DataAccesContext {

    private final Connection connection;

    public MySQLDAC(Connection connection) {
        this.connection = connection;
    }

    @Override
    public PersonDAO getPersonDAO() {
        return null;
    }

    @Override
    public PileDAO getPileDAO() {
        return null;
    }

    @Override
    public ProductDAO getProductDAO() {
        return null;
    }

    @Override
    public ProductTypeDAO getProductTypeDAO() {
        return null;
    }

    @Override
    public TransactionDAO getTransactionDAO() {
        return null;
    }

    @Override
    public TransactionTypeDAO getTransactionTypeDAO() {
        return null;
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
