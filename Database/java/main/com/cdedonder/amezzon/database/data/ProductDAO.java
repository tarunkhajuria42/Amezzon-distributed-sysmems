package com.cdedonder.amezzon.database.data;

import com.cdedonder.amezzon.database.DataAccessException;

import java.util.Collection;

public interface ProductDAO {

    Product create(Product product) throws DataAccessException;

    Product read(int id) throws DataAccessException;

    Product read(String productName) throws DataAccessException;

    void update(Product product) throws DataAccessException;

    void delete(Product product) throws DataAccessException;

    void deleteAll() throws DataAccessException;

    boolean exists(Product product) throws DataAccessException;

    Collection<Product> readByProductType(ProductType productType) throws DataAccessException;

    Collection<Product> readAll() throws DataAccessException;

    default Product read(Product product) throws DataAccessException {
        return read(product.getId());
    }
}
