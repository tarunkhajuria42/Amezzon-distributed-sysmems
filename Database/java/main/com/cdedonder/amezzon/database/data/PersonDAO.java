package com.cdedonder.amezzon.database.data;

import com.cdedonder.amezzon.database.DataAccessException;

public interface PersonDAO {

    Person create(Person person, boolean atomic) throws DataAccessException;

    default Person create(Person person) throws DataAccessException {
        return create(person, true);
    }

    void update(Person person, boolean atomic) throws DataAccessException;

    default void update(Person person) throws DataAccessException {
        update(person, true);
    }

    boolean delete(Person person, boolean atomic) throws DataAccessException;

    default boolean delete(Person person) throws DataAccessException {
        return delete(person, true);
    }

    Person read(int id) throws DataAccessException;

    Person read(String username) throws DataAccessException;

    Person read(String username, String passwordHash) throws DataAccessException;

    Person read(Person person) throws DataAccessException;

}
