package testsuite;

import com.cdedonder.amezzon.database.DataSourceWrapper;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class ConnectionTest {

    public static void main(String[] args) {
        DataSourceWrapper ds = new DataSourceWrapper();
        try (Connection conn = ds.getConnection();
             PreparedStatement ps = conn.prepareStatement("SHOW TABLES");
             ResultSet set = ps.executeQuery()) {
            while (set.next()) {
                System.out.println(set.getString(1));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }


}
