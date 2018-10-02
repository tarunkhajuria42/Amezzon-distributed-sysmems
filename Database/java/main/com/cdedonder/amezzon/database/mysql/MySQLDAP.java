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
        String base = properties.getProperty("urlbase");
        String host = properties.getProperty("host");
        String database = properties.getProperty("database");
        String user = properties.getProperty("user");

        String url = base + host + database + "?serverTimezone=UTC&useSSL=false&autoReconnect=true&user=" + user; //TODO add password
        return DriverManager.getConnection(url);
    }
}
