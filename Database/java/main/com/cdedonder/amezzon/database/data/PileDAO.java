package com.cdedonder.amezzon.database.data;

import com.cdedonder.amezzon.database.DataAccessException;

import java.util.Collection;

public interface PileDAO {

    Pile create(Pile pile) throws DataAccessException;

    Pile read(int id) throws DataAccessException;

    Collection<Pile> readAll() throws DataAccessException;

    Pile readByProduct(Product product) throws DataAccessException;

    void update(Pile pile) throws DataAccessException;

    void delete(Pile pile) throws DataAccessException;

    void deleteAll() throws DataAccessException;

    boolean exists(Pile pile) throws DataAccessException;

    default Pile read(Pile pile) throws DataAccessException {
        return read(pile.getId());
    }
}
