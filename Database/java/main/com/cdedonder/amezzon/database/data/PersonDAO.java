package com.cdedonder.amezzon.database.data;

import com.cdedonder.amezzon.database.DataAccessException;

public interface PersonDAO {

    Person create(Person person) throws DataAccessException;

    void update(Person person) throws DataAccessException;

    void delete(Person person) throws DataAccessException;

    Person read(int id) throws DataAccessException;

    Person read(String username) throws DataAccessException;

    boolean exist(Person person) throws DataAccessException;

    boolean exist(int id) throws DataAccessException;

}
