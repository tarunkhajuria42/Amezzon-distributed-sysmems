package com.cdedonder.amezzon;

import com.cdedonder.amezzon.database.DataAccesContext;
import com.cdedonder.amezzon.database.DataAccesProvider;
import com.cdedonder.amezzon.database.DataAccessException;
import com.cdedonder.amezzon.database.data.PersonDAO;
import com.cdedonder.amezzon.database.mysql.MySQLDAP;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.util.Properties;

public class MySQLDatabaseTest {

    private static Properties properties;

    @Before
    public void initialize() {
        //TODO
    }

    @Test
    public void testConnection() throws DataAccessException {
        DataAccesProvider provider = new MySQLDAP();
        try (DataAccesContext context = provider.getDataAccessContext(properties)) {
            PersonDAO personDAO = context.getPersonDAO();
        }
    }

    @After
    public void cleanUp() {

    }
}
