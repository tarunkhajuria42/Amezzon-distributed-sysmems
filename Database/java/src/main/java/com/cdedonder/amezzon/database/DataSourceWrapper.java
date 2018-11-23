package com.cdedonder.amezzon.database;

import com.cdedonder.amezzon.logging.DatabaseLogger;
import com.cdedonder.amezzon.util.InvalidationQueue;

import javax.sql.DataSource;
import java.io.IOException;
import java.io.InputStream;
import java.sql.Connection;
import java.sql.SQLException;
import java.util.Properties;
import java.util.logging.Logger;

public class DataSourceWrapper {

    private static Logger LOGGER = DatabaseLogger.getLogger();

    private InvalidationQueue<DataSource> dataSources;

    public DataSourceWrapper() {
        dataSources = new InvalidationQueue<>();
        initialize();
    }

    private void initialize() {
        try {
            InputStream is;
            Properties properties;
            for (int i = 1; ; i++) {
                is = getClass().getResourceAsStream("/db" + i + ".properties");
                if (is == null) {
                    break;
                }
                properties = new Properties();
                properties.load(is);
                DataSource ds = DataSourceFactory.getMySQLDataSource(properties);
                if (ds != null) {
                    dataSources.add(ds);
                }
            }
        } catch (IOException e) {
            LOGGER.severe(e.getMessage());
        }
    }

    public Connection getConnection() {
        while (dataSources.hasValid()) {
            try {
                return dataSources.get().getConnection();
            } catch (SQLException e) {
                dataSources.invalidate();
            }
        }
        throw new IllegalStateException("No connections available!"); //DEBUG
    }
}
