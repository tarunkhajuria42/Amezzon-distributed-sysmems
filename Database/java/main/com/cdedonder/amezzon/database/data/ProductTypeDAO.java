package com.cdedonder.amezzon.database.data;

import com.cdedonder.amezzon.database.DataAccessException;

public interface ProductTypeDAO {

    boolean exists(ProductType productType) throws DataAccessException;

    void delete(ProductType productType) throws DataAccessException;

    ProductType create(ProductType productType) throws DataAccessException;
}
