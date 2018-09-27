package com.cdedonder.amezzon.database.data.mysql;

import com.cdedonder.amezzon.database.data.TransactionDAO;

import java.sql.Connection;

public class MySQLTransactionDAO extends MySQLAbstractDAO implements TransactionDAO {

    public MySQLTransactionDAO(Connection connection) {
        super(connection);
    }
}
