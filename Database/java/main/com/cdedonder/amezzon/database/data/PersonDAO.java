package com.cdedonder.amezzon.database.data;

import com.cdedonder.amezzon.database.DataAccessException;

import java.util.Collection;

public interface PersonDAO {

    Person create(Person person) throws DataAccessException;

    void update(Person person) throws DataAccessException;

    void delete(Person person) throws DataAccessException;

    Person read(int id) throws DataAccessException;

    Person read(String username) throws DataAccessException;

    Collection<Person> readAll() throws DataAccessException;

    void deleteAll() throws DataAccessException;

    default boolean exist(Person person) throws DataAccessException {
        return exist(person.getId());
    }

    boolean exist(int id) throws DataAccessException;

}
