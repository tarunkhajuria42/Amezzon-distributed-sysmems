package com.cdedonder.amezzon.database.data.mysql;

import com.cdedonder.amezzon.database.DataAccesContext;
import com.cdedonder.amezzon.database.DataAccessException;
import com.cdedonder.amezzon.database.data.Product;
import com.cdedonder.amezzon.database.data.ProductDAO;
import com.cdedonder.amezzon.database.data.ProductType;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

public class MySQLProductDAO extends MySQLAbstractDAO implements ProductDAO {

    private static final String CREATE_PRODUCT = "INSERT INTO product (product_type, product_name, product_description) VALUES (?,?,?)";
    private static final String READ_PRODUCT_BY_ID = "SELECT product_id, product_type, product_name, product_description FROM product WHERE product_id=?";
    private static final String READ_PRODUCT_BY_NAME = "SELECT product_id, product_type, product_name, product_description FROM product WHERE product_name=?";
    private static final String UPDATE_PRODUCT = "UPDATE product SET product_type=?,product_name=?, product_description=? WHERE product_id=?";
    private static final String DELETE_PRODUCT = "DELETE FROM product WHERE product_id=?";
    private static final String DELETE_ALL = "DELETE FROM product";
    private static final String PRODUCT_EXISTS = "SELECT 1 FROM product WHERE product_id=?";
    private static final String READ_PRODUCTS_BY_PRODUCT_TYPE = "SELECT product_id, product_type, product_name, product_description FROM product WHERE product_type=?";
    private static final String READ_ALL = "SELECT product_id, product_type, product_name, product_description FROM product";

    public MySQLProductDAO(Connection connection, DataAccesContext dac) {
        super(connection, dac);
    }

    private static void fillProduct(ResultSet set, Product product) throws SQLException {
        ProductType type = new ProductType();
        type.setProductType(set.getString("product_type"));

        product.setType(type);
        product.setName(set.getString("product_name"));
        product.setDescription(set.getString("product_description"));
        product.setId(set.getInt("product_id"));
    }

    private static void fillStatement(PreparedStatement stmt, Product product) throws SQLException {
        stmt.setString(1, product.getType().getProductType());
        stmt.setString(2, product.getName());
        stmt.setString(3, product.getDescription());
        stmt.setInt(4, product.getId());
    }

    @Override
    public Product create(Product product) throws DataAccessException {
        try {
            try (PreparedStatement stmt = prepare(CREATE_PRODUCT, true)) {
                fillStatement(stmt, product);
                stmt.executeUpdate();
                try (ResultSet set = stmt.getGeneratedKeys()) {
                    if (set.next()) {
                        product.setId(set.getInt(1));
                        return product;
                    }
                    throw new DataAccessException("Keys were not generated.");
                }
            }
        } catch (SQLException e) {
            throw new DataAccessException(e);
        }
    }

    @Override
    public Product read(int id) throws DataAccessException {
        try {
            try (PreparedStatement stmt = prepare(READ_PRODUCT_BY_ID)) {
                stmt.setInt(1, id);
                try (ResultSet set = stmt.executeQuery()) {
                    if (set.next()) {
                        Product product = new Product();
                        fillProduct(set, product);
                        return product;
                    }
                    throw new DataAccessException("Product with id " + id + " does not exist.");
                }
            }
        } catch (SQLException e) {
            throw new DataAccessException(e);
        }
    }

    @Override
    public Product read(String productName) throws DataAccessException {
        try {
            try (PreparedStatement stmt = prepare(READ_PRODUCT_BY_NAME)) {
                stmt.setString(1, productName);
                try (ResultSet set = stmt.executeQuery()) {
                    if (set.next()) {
                        Product product = new Product();
                        fillProduct(set, product);
                        return product;
                    }
                    throw new DataAccessException("Product " + productName + " does not exist.");
                }
            }
        } catch (SQLException e) {
            throw new DataAccessException(e);
        }
    }

    @Override
    public void update(Product product) throws DataAccessException {
        try {
            try (PreparedStatement stmt = prepare(UPDATE_PRODUCT)) {
                fillStatement(stmt, product);
                stmt.executeUpdate();
            }
        } catch (SQLException e) {
            throw new DataAccessException(e);
        }
    }

    @Override
    public void delete(Product product) throws DataAccessException {
        try {
            try (PreparedStatement stmt = prepare(DELETE_PRODUCT)) {
                stmt.setInt(0, product.getId());
                stmt.executeUpdate();
            }
        } catch (SQLException e) {
            throw new DataAccessException(e);
        }
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
    public boolean exists(Product product) throws DataAccessException {
        try {
            try (PreparedStatement stmt = prepare(PRODUCT_EXISTS)) {
                stmt.setInt(0, product.getId());
                try (ResultSet set = stmt.executeQuery()) {
                    return set.next();
                }
            }
        } catch (SQLException e) {
            throw new DataAccessException(e);
        }
    }

    @Override
    public Collection<Product> readByProductType(ProductType productType) throws DataAccessException {
        try {
            try (PreparedStatement stmt = prepare(READ_PRODUCTS_BY_PRODUCT_TYPE)) {
                stmt.setString(1, productType.getProductType());
                try (ResultSet set = stmt.executeQuery()) {
                    List<Product> list = new ArrayList<>();
                    while (set.next()) {
                        Product product = new Product();
                        fillProduct(set, product);
                        list.add(product);
                    }
                    return list;
                }
            }
        } catch (SQLException e) {
            throw new DataAccessException(e);
        }
    }

    @Override
    public Collection<Product> readAll() throws DataAccessException {
        try {
            try (PreparedStatement stmt = prepare(READ_ALL);
                 ResultSet set = stmt.executeQuery()) {
                List<Product> list = new ArrayList<>();
                while (set.next()) {
                    Product product = new Product();
                    fillProduct(set, product);
                }
                return list;
            }
        } catch (SQLException e) {
            throw new DataAccessException(e);
        }
    }
}
