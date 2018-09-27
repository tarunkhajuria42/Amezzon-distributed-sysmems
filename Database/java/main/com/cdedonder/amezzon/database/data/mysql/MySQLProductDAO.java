package com.cdedonder.amezzon.database.data.mysql;

import com.cdedonder.amezzon.database.data.ProductDAO;

import java.sql.Connection;

public class MySQLProductDAO extends MySQLAbstractDAO implements ProductDAO {

    public MySQLProductDAO(Connection connection) {
        super(connection);
    }
}
