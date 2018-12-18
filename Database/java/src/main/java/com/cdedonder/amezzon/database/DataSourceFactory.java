package com.cdedonder.amezzon.database;

import com.mysql.cj.jdbc.MysqlDataSource;

import javax.sql.DataSource;
import java.io.IOException;
import java.io.InputStream;
import java.sql.SQLException;
import java.util.Properties;

public class DataSourceFactory {

    public static DataSource getMySQLDataSource(Properties props) {
        MysqlDataSource mysqlDS = null;
        try{
            //props.load(DataSourceFactory.class.getResourceAsStream("/db1.properties"));
            mysqlDS = new MysqlDataSource();
            mysqlDS.setURL(props.getProperty("MYSQL_DB_URL") + "?max-connections=200");
            mysqlDS.setUser(props.getProperty("MYSQL_DB_USERNAME"));
            mysqlDS.setPassword(props.getProperty("MYSQL_DB_PASSWORD"));
            mysqlDS.setUseSSL(Boolean.parseBoolean(props.getProperty("MYSQL_DB_USESSL")));
            mysqlDS.setAutoReconnect(Boolean.parseBoolean(props.getProperty("MYSQL_DB_AUTORECONNECT")));
            mysqlDS.setAllowPublicKeyRetrieval(Boolean.parseBoolean(props.getProperty("MYSQL_DB_ALLOWPUBLICKEYRETRIEVAL")));
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return mysqlDS;
    }

    public static DataSource getMySQLDataSource() {
        DataSource ds = null;
        try {
            Properties properties = new Properties();
            try (InputStream is = DataSourceFactory.class.getResourceAsStream("/db1.properties")) {
                properties.load(is);
            }
            ds = getMySQLDataSource(properties);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return ds;
    }
}
