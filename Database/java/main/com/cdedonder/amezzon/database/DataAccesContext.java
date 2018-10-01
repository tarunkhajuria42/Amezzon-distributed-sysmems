package com.cdedonder.amezzon.database;

import com.cdedonder.amezzon.database.data.*;

public interface DataAccesContext extends AutoCloseable {

    PersonDAO getPersonDAO() throws DataAccessException;

    PileDAO getPileDAO() throws DataAccessException;

    ProductDAO getProductDAO() throws DataAccessException;

    ProductTypeDAO getProductTypeDAO() throws DataAccessException;

    TransactionDAO getTransactionDAO() throws DataAccessException;

    TransactionTypeDAO getTransactionTypeDAO() throws DataAccessException;

    @Override
    void close() throws DataAccessException;
}
