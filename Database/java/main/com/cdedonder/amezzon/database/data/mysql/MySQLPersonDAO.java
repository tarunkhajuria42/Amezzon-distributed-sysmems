package com.cdedonder.amezzon.database.data.mysql;

import com.cdedonder.amezzon.database.DataAccessException;
import com.cdedonder.amezzon.database.data.Person;
import com.cdedonder.amezzon.database.data.PersonDAO;

import java.sql.Connection;

public class MySQLPersonDAO extends MySQLAbstractDAO implements PersonDAO {

    public MySQLPersonDAO(Connection connection) {
        super(connection);
    }

    @Override
    public Person create(Person person) throws DataAccessException {
        return null;
    }

    @Override
    public void update(Person person) throws DataAccessException {

    }

    @Override
    public void delete(Person person) throws DataAccessException {

    }

    @Override
    public Person read(int id) throws DataAccessException {
        return null;
    }

    @Override
    public Person read(String username) throws DataAccessException {
        return null;
    }

    @Override
    public boolean exist(Person person) throws DataAccessException {
        return false;
    }

    @Override
    public boolean exist(int id) throws DataAccessException {
        return false;
    }
}
