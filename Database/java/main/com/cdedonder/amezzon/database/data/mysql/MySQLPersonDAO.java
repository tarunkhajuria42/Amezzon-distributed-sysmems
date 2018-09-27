package com.cdedonder.amezzon.database.data.mysql;

import com.cdedonder.amezzon.database.data.PersonDAO;

import java.sql.Connection;

public class MySQLPersonDAO extends MySQLAbstractDAO implements PersonDAO {

    public MySQLPersonDAO(Connection connection) {
        super(connection);
    }
}
