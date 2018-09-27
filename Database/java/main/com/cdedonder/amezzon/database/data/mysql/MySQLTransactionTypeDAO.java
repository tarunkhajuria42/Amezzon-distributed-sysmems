package com.cdedonder.amezzon.database.data.mysql;

import com.cdedonder.amezzon.database.data.TransactionTypeDAO;

import java.sql.Connection;

public class MySQLTransactionTypeDAO extends MySQLAbstractDAO implements TransactionTypeDAO {

    public MySQLTransactionTypeDAO(Connection connection) {
        super(connection);
    }
}
