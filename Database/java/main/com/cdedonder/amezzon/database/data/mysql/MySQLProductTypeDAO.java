package com.cdedonder.amezzon.database.data.mysql;

import com.cdedonder.amezzon.database.DataAccesContext;
import com.cdedonder.amezzon.database.DataAccessException;
import com.cdedonder.amezzon.database.data.ProductType;
import com.cdedonder.amezzon.database.data.ProductTypeDAO;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

public class MySQLProductTypeDAO extends MySQLAbstractDAO implements ProductTypeDAO {

    private static final String CREATE_PRODUCT_TYPE = "INSERT INTO product_type VALUES (?);";
    private static final String DELETE_PRODUCT_TYPE = "DELETE FROM product_type WHERE product_type=?";
    private static final String PRODUCT_TYPE_EXISTS = "SELECT 1 FROM product_type WHERE product_type=?";
    private static final String READ_ALL = "SELECT product_type FROM product_type";
    private static final String DELETE_ALL = "DELETE FROM product_type";

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

    @Override
    public void deleteAll() throws DataAccessException {
        try {
            try (PreparedStatement stmt = prepare(DELETE_ALL)) {
                stmt.executeUpdate();
            }
        } catch (SQLException e) {
            throw new DataAccessException(e);
        }
    }

    @Override
    public Collection<ProductType> readAll() throws DataAccessException {
        try {
            try (PreparedStatement stmt = prepare(READ_ALL);
                 ResultSet set = stmt.executeQuery()) {
                List<ProductType> list = new ArrayList<>();
                while (set.next()) {
                    ProductType type = new ProductType();
                    type.setProductType(set.getString("product_type"));
                    list.add(type);
                }
                return list;
            }
        } catch (SQLException e) {
            throw new DataAccessException(e);
        }
    }
}
