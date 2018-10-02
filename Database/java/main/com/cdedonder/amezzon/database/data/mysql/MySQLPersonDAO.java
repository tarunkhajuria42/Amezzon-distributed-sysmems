package com.cdedonder.amezzon.database.data.mysql;

import com.cdedonder.amezzon.database.DataAccessException;
import com.cdedonder.amezzon.database.data.Person;
import com.cdedonder.amezzon.database.data.PersonDAO;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class MySQLPersonDAO extends MySQLAbstractDAO implements PersonDAO {

    public MySQLPersonDAO(Connection connection) throws DataAccessException {
        super(connection);
    }

    @Override
    public Person create(Person person, boolean atomic) throws DataAccessException {
        try {
            try (PreparedStatement checkExistence = prepare("SELECT count(*) FROM person WHERE username=?")) {
                checkExistence.setString(1, person.getUsername());
                try (ResultSet resultSet = checkExistence.executeQuery()) {
                    if (resultSet.next()) {
                        rollback();
                        throw new DataAccessException("User already exists.");
                    }
                }
            }
            try (PreparedStatement insert = prepareWithKeys("INSERT INTO person (person_username, " +
                    "person_passwordhash, person_firstname, person_lastname, person_mail VALUES (?,?,?,?,?")) {
                insert.setString(1, person.getUsername());
                insert.setString(2, person.getPasswordHash());
                insert.setString(3, person.getFirstName());
                insert.setString(4, person.getLastName());
                insert.setString(5, person.getMail());
                insert.executeUpdate();
                try (ResultSet keys = insert.getGeneratedKeys()) {
                    if (keys.next()) {
                        int key = keys.getInt(1);
                        person.setId(key);
                        commit(atomic);
                        return person;
                    }
                    rollback();
                    throw new DataAccessException("Could not create user!");
                }
            }
        } catch (SQLException e) {
            try {
                rollback();
            } catch (SQLException f) {
                throw new DataAccessException("Exceptions " + e.getMessage() + ", " + f.getMessage()); //DEBUG
            }
            throw new DataAccessException(e);
        }
    }

    @Override
    public void update(Person person, boolean atomic) throws DataAccessException {
        try {
            try (PreparedStatement update = prepare("UPDATE person SET person_username=?, person_passwordHash=?, " +
                    "person_firstname=?, person_lastname=?, person_mail=? WHERE person_id=?")) {
                update.setString(1, person.getUsername());
                update.setString(2, person.getPasswordHash());
                update.setString(3, person.getFirstName());
                update.setString(4, person.getLastName());
                update.setString(5, person.getMail());
                update.setInt(6, person.getId());
                update.executeUpdate();
                commit(atomic);
            }
        } catch (SQLException e) {
            try {
                rollback();
            } catch (SQLException f) {
                throw new DataAccessException("Exceptions " + e.getMessage() + ", " + f.getMessage()); //DEBUG
            }
            throw new DataAccessException(e);
        }
    }

    @Override
    public boolean delete(Person person, boolean atomic) throws DataAccessException {
        try {

        } catch (SQLException e) {
            try {
                rollback();
            } catch (SQLException f) {
                throw new DataAccessException("Exceptions " + e.getMessage() + ", " + f.getMessage()); //DEBUG
            }
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
    public Person read(String username, String passwordHash) throws DataAccessException {
        return null;
    }

    @Override
    public Person read(Person person) throws DataAccessException {
        return null;
    }
}
