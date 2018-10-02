package com.cdedonder.amezzon;

import com.cdedonder.amezzon.database.DataAccesContext;
import com.cdedonder.amezzon.database.DataAccesProvider;
import com.cdedonder.amezzon.database.DataAccessException;
import com.cdedonder.amezzon.database.data.Person;
import com.cdedonder.amezzon.database.data.PersonDAO;
import com.cdedonder.amezzon.database.mysql.MySQLDAP;
import org.junit.After;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;

import java.io.IOException;
import java.util.Properties;

import static org.junit.Assert.assertTrue;

public class PersonDatabaseTest {

    private static Properties properties;
    private Person person;

    @BeforeClass
    public static void classInit() throws IOException {
        properties = new Properties();
        properties.load(PersonDatabaseTest.class.getResourceAsStream("database.properties"));
    }

    @Before
    public void init() {
        person = new Person();
        person.setUsername("testuser");
        person.setPasswordHash("testpassword");
        person.setFirstName("testname");
        person.setLastName("testname");
        person.setMail("testmail");
    }

    @Test
    public void testPersonInsertion() throws DataAccessException {
        DataAccesProvider dap = new MySQLDAP();
        DataAccesContext dac = dap.getDataAccessContext(properties);
        PersonDAO personDAO = dac.getPersonDAO();
        person = personDAO.create(person);
        assertTrue(personDAO.exist(person));
    }

    @After
    public void cleanUp() throws DataAccessException {
        DataAccesProvider dap = new MySQLDAP();
        DataAccesContext dac = dap.getDataAccessContext(properties);
        PersonDAO personDAO = dac.getPersonDAO();
        personDAO.delete(person);
    }


}
