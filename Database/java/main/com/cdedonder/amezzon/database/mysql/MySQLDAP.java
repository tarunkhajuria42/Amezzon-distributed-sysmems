package com.cdedonder.amezzon.database.mysql;

import com.cdedonder.amezzon.database.DataAccesContext;
import com.cdedonder.amezzon.database.DataAccesProvider;
import com.cdedonder.amezzon.database.DataAccessException;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.Properties;

public class MySQLDAP implements DataAccesProvider {

    @Override
    public DataAccesContext getDataAccessContext(Properties properties) throws DataAccessException {
        try {
            return new MySQLDAC(getConnection(properties));
        } catch (SQLException e) {
            throw new DataAccessException(e);
        }
    }

    private Connection getConnection(Properties properties) throws SQLException {
        String url = null; //TODO
        return DriverManager.getConnection(url);
    }
}
