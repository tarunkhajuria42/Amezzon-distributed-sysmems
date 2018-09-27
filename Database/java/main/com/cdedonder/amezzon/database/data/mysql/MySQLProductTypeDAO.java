package com.cdedonder.amezzon.database.data.mysql;

import com.cdedonder.amezzon.database.data.ProductTypeDAO;

import java.sql.Connection;

public class MySQLProductTypeDAO extends MySQLAbstractDAO implements ProductTypeDAO {

    public MySQLProductTypeDAO(Connection connection) {
        super(connection);
    }
}
