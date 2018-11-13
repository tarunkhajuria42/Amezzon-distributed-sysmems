package com.cdedonder.amezzon;

import com.cdedonder.amezzon.database.DataSourceFactory;

import javax.sql.DataSource;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

public class ConnectionTest {

    public static void main(String[] args) throws Exception {
        DataSource ds = DataSourceFactory.getMySQLDataSource();
        try (Connection conn = ds.getConnection()) {
            try (PreparedStatement ps = conn.prepareStatement("SELECT * FROM product")) {
                try (ResultSet set = ps.executeQuery()) {
                    while (set.next()) {
                        System.out.println(set.getInt(1));
                    }
                }
            }
        }
    }
}
