package com.cdedonder.amezzon.database;

import com.cdedonder.amezzon.database.data.*;

public interface DataAccesContext extends AutoCloseable {

    PersonDAO getPersonDAO();

    PileDAO getPileDAO();

    ProductDAO getProductDAO();

    ProductTypeDAO getProductTypeDAO();

    TransactionDAO getTransactionDAO();

    TransactionTypeDAO getTransactionTypeDAO();

    void commit() throws DataAccessException;

    void rollback() throws DataAccessException;

    void startTransaction() throws DataAccessException;

    @Override
    void close() throws DataAccessException;
}
