package com.cdedonder.amezzon.database.data;

import com.cdedonder.amezzon.database.DataAccessException;

import java.util.Collection;

public interface ProductTypeDAO {

    boolean exists(ProductType productType) throws DataAccessException;

    void delete(ProductType productType) throws DataAccessException;

    ProductType create(ProductType productType) throws DataAccessException;

    ProductType read(String productType) throws DataAccessException;

    void deleteAll() throws DataAccessException;

    Collection<ProductType> readAll() throws DataAccessException;
}
