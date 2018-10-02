package com.cdedonder.amezzon.database.data.mysql;

import com.cdedonder.amezzon.database.DataAccessException;
import com.cdedonder.amezzon.database.data.Person;
import com.cdedonder.amezzon.database.data.PersonDAO;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

@SuppressWarnings("SpellCheckingInspection")
public class MySQLPersonDAO extends MySQLAbstractDAO implements PersonDAO {

    private final static String CREATE_PERSON = "INSERT INTO person " +
            "(person_username, person_passwordhash, person_firstname, person_lastname, person_mail)" +
            "VALUES (?,?,?,?,?)";
    private final static String UPDATE_PERSON = "UPDATE person " +
            "SET person_username=?, person_passwordhash=?, person_firstname=?, person_lastname=?, person_mail" +
            "WHERE person_id=?";
    private final static String DELETE_PERSON = "DELETE FROM person WHERE person_id=?";
    private final static String READ_PERSON_BY_ID = "SELECT person_id, person_username, person_passwordhash, person_firstname, " +
            "person_lastname, person_mail FROM person WHERE person_id=?";
    private final static String READ_PERSON_BY_USERNAME = "SELECT person_id, person_username, person_passwordhash, person_firstname, " +
            "person_lastname, person_mail FROM person WHERE person_username=?";
    private final static String PERSON_EXISTS = "SELECT 1 FROM person WHERE person_id=?";

    public MySQLPersonDAO(Connection connection) {
        super(connection);
    }

    private static void fillStatement(PreparedStatement stmt, Person person) throws SQLException {
        stmt.setString(1, person.getUsername());
        stmt.setString(2, person.getPasswordHash());
        stmt.setString(3, person.getFirstName());
        stmt.setString(4, person.getLastName());
        stmt.setString(5, person.getMail());
    }

    private static void fillPerson(ResultSet set, Person person) throws SQLException {
        person.setId(set.getInt("person_id"));
        person.setUsername(set.getString("person_username"));
        person.setPasswordHash(set.getString("person_passwordhash"));
        person.setFirstName(set.getString("person_firstname"));
        person.setLastName(set.getString("person_lastname"));
        person.setMail(set.getString("person_mail"));
    }

    @Override
    public Person create(Person person) throws DataAccessException {
        try {
            try (PreparedStatement stmt = prepare(CREATE_PERSON, true)) {
                fillStatement(stmt, person);
                stmt.executeUpdate();
                try (ResultSet set = stmt.getGeneratedKeys()) {
                    if (set.next()) {
                        person.setId(set.getInt(1));
                        return person;
                    }
                    throw new DataAccessException("Generated keys not delivered.");
                }
            }
        } catch (SQLException e) {
            throw new DataAccessException(e);
        }
    }

    @Override
    public void update(Person person) throws DataAccessException {
        try {
            try (PreparedStatement stmt = prepare(UPDATE_PERSON)) {
                fillStatement(stmt, person);
                stmt.setInt(6, person.getId());
                stmt.executeUpdate();
            }
        } catch (SQLException e) {
            throw new DataAccessException(e);
        }
    }

    @Override
    public void delete(Person person) throws DataAccessException {
        try {
            try (PreparedStatement stmt = prepare(DELETE_PERSON)) {
                stmt.setInt(1, person.getId());
                stmt.executeUpdate();
            }
        } catch (SQLException e) {
            throw new DataAccessException(e);
        }
    }

    @Override
    public Person read(int id) throws DataAccessException {
        try {
            try (PreparedStatement stmt = prepare(READ_PERSON_BY_ID)) {
                stmt.setInt(1, id);
                try (ResultSet set = stmt.executeQuery()) {
                    if (set.next()) {
                        Person person = new Person();
                        fillPerson(set, person);
                        return person;
                    }
                    throw new DataAccessException("User with ID " + id + " not found.");
                }
            }
        } catch (SQLException e) {
            throw new DataAccessException(e);
        }
    }

    @Override
    public Person read(String username) throws DataAccessException {
        try {
            try (PreparedStatement stmt = prepare(READ_PERSON_BY_USERNAME)) {
                stmt.setString(1, username);
                try (ResultSet set = stmt.executeQuery()) {
                    if (set.next()) {
                        Person person = new Person();
                        fillPerson(set, person);
                        return person;
                    }
                    throw new DataAccessException("User " + username + " not found.");
                }
            }
        } catch (SQLException e) {
            throw new DataAccessException(e);
        }
    }

    @Override
    public boolean exist(int id) throws DataAccessException {
        try {
            try (PreparedStatement stmt = prepare(PERSON_EXISTS)) {
                stmt.setInt(1, id);
                try (ResultSet set = stmt.executeQuery()) {
                    return set.next();
                }
            }
        } catch (SQLException e) {
            throw new DataAccessException(e);
        }
    }
}
