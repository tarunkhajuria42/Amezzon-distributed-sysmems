package com.cdedonder.amezzon.database.data.mysql;

import com.cdedonder.amezzon.database.DataAccesContext;
import com.cdedonder.amezzon.database.DataAccessException;
import com.cdedonder.amezzon.database.data.ProductType;
import com.cdedonder.amezzon.database.data.ProductTypeDAO;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class MySQLProductTypeDAO extends MySQLAbstractDAO implements ProductTypeDAO {

    private static final String CREATE_PRODUCT_TYPE = "INSERT INTO producttype VALUES (?);";
    private static final String DELETE_PRODUCT_TYPE = "DELETE FROM producttype WHERE producttype=?";
    private static final String PRODUCT_TYPE_EXISTS = "SELECT 1 FROM producttype WHERE producttype=?";

    public MySQLProductTypeDAO(Connection connection, DataAccesContext dac) {
        super(connection, dac);
    }

    @Override
    public boolean exists(ProductType productType) throws DataAccessException {
        try {
            try (PreparedStatement stmt = prepare(PRODUCT_TYPE_EXISTS)) {
                stmt.setString(1, productType.getProductType());
                try (ResultSet set = stmt.executeQuery()) {
                    return set.next();
                }
            }
        } catch (SQLException e) {
            throw new DataAccessException(e);
        }
    }

    @Override
    public void delete(ProductType productType) throws DataAccessException {
        try {
            try (PreparedStatement stmt = prepare(DELETE_PRODUCT_TYPE)) {
                stmt.setString(1, productType.getProductType());
                stmt.executeUpdate();
            }
        } catch (SQLException e) {
            throw new DataAccessException(e);
        }
    }

    @Override
    public ProductType create(ProductType productType) throws DataAccessException {
        try {
            try (PreparedStatement stmt = prepare(CREATE_PRODUCT_TYPE)) {
                stmt.setString(1, productType.getProductType());
                stmt.executeUpdate();
                return productType;
            }
        } catch (SQLException e) {
            throw new DataAccessException(e);
        }
    }

    @Override
    public ProductType read(String productType) throws DataAccessException {
        ProductType type = new ProductType();
        type.setProductType(productType);
        if (exists(type)) return type;
        throw new DataAccessException("Product type '" + productType + "' does not exist.");
    }


}
