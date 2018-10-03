package com.cdedonder.amezzon.database.data.mysql;

import com.cdedonder.amezzon.database.DataAccesContext;
import com.cdedonder.amezzon.database.DataAccessException;
import com.cdedonder.amezzon.database.data.Pile;
import com.cdedonder.amezzon.database.data.PileDAO;
import com.cdedonder.amezzon.database.data.Product;
import com.cdedonder.amezzon.database.data.ProductDAO;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

@SuppressWarnings("Duplicates")
public class MySQLPileDAO extends MySQLAbstractDAO implements PileDAO {

    private static final String CREATE_PILE = "INSERT INTO pile (pile_product, pile_sell, pile_buy) VALUES (?,?,?)";
    private static final String READ_PILE_BY_ID = "SELECT pile_id, pile_product, pile_sell, pile_buy FROM pile WHERE pile_id=?";
    private static final String READ_ALL = "SELECT pile_id, pile_product, pile_sell, pile_buy FROM pile";
    private static final String READ_PILE_BY_PRODUCT = "SELECT pile_id, pile_product, pile_sell, pile_buy FROM pile WHERE pile_product=?";
    private static final String UPDATE_PILE = "UPDATE pile SET pile_product=?, pile_sell=?, pile_buy=? WHERE pile_id=?";
    private static final String DELETE_PILE = "DELETE FROM pile WHERE pile_id=?";
    private static final String DELETE_ALL = "DELETE FROM pile";
    private static final String PILE_EXISTS = "SELECT 1 FROM pile WHERE pile_id=?";

    private final ProductDAO productDAO;

    public MySQLPileDAO(Connection connection, DataAccesContext dac) {
        super(connection, dac);
        this.productDAO = getDataAccesContext().getProductDAO();
    }

    private static void fillStatement(PreparedStatement stmt, Pile pile) throws SQLException {
        stmt.setInt(1, pile.getProduct().getId());
        stmt.setDouble(2, pile.getSell());
        stmt.setDouble(3, pile.getBuy());
    }

    private void fillPile(ResultSet set, Pile pile) throws SQLException, DataAccessException {
        pile.setId(set.getInt("pile_id"));
        pile.setSell(set.getDouble("pile_sell"));
        pile.setBuy(set.getDouble("pile_buy"));
        pile.setProduct(productDAO.read(set.getInt("pile_product")));

    }

    @Override
    public Pile create(Pile pile) throws DataAccessException {
        try {
            try (PreparedStatement stmt = prepare(CREATE_PILE, true)) {
                fillStatement(stmt, pile);
                stmt.executeUpdate();
                try (ResultSet set = stmt.getGeneratedKeys()) {
                    if (set.next()) {
                        pile.setId(set.getInt(1));
                        return pile;
                    }
                    throw new DataAccessException("Keys were not generated.");
                }
            }
        } catch (SQLException e) {
            throw new DataAccessException(e);
        }
    }

    @Override
    public Pile read(int id) throws DataAccessException {
        try {
            try (PreparedStatement stmt = prepare(READ_PILE_BY_ID)) {
                stmt.setInt(1, id);
                try (ResultSet set = stmt.executeQuery()) {
                    if (set.next()) {
                        Pile pile = new Pile();
                        fillPile(set, pile);
                    }
                    throw new DataAccessException("Pile with id " + id + " does not exist.");
                }
            }
        } catch (SQLException e) {
            throw new DataAccessException(e);
        }
    }

    @Override
    public Collection<Pile> readAll() throws DataAccessException {
        try {
            try (PreparedStatement stmt = prepare(READ_ALL);
                 ResultSet set = stmt.executeQuery()) {
                List<Pile> pileList = new ArrayList<>();
                while (set.next()) {
                    Pile pile = new Pile();
                    fillPile(set, pile);
                    pileList.add(pile);
                }
                return pileList;
            }
        } catch (SQLException e) {
            throw new DataAccessException(e);
        }
    }

    @Override
    public Pile readByProduct(Product product) throws DataAccessException {
        try {
            try (PreparedStatement stmt = prepare(READ_PILE_BY_PRODUCT)) {
                stmt.setInt(1, product.getId());
                try (ResultSet set = stmt.executeQuery()) {
                    if (set.next()) {
                        Pile pile = new Pile();
                        fillPile(set, pile);
                        return pile;
                    }
                    throw new DataAccessException("A pile with product " + product.getName() + " does not exist.");
                }
            }
        } catch (SQLException e) {
            throw new DataAccessException(e);
        }
    }

    @Override
    public void update(Pile pile) throws DataAccessException {
        try {
            try (PreparedStatement stmt = prepare(UPDATE_PILE)) {
                fillStatement(stmt, pile);
                stmt.setInt(4, pile.getId());
                stmt.executeUpdate();
            }
        } catch (SQLException e) {
            throw new DataAccessException(e);
        }
    }

    @Override
    public void delete(Pile pile) throws DataAccessException {
        try {
            try (PreparedStatement stmt = prepare(DELETE_PILE)) {
                stmt.setInt(1, pile.getId());
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
    public boolean exists(Pile pile) throws DataAccessException {
        try {
            try (PreparedStatement stmt = prepare(PILE_EXISTS)) {
                stmt.setInt(1, pile.getId());
                try (ResultSet set = stmt.executeQuery()) {
                    return set.next();
                }
            }
        } catch (SQLException e) {
            throw new DataAccessException(e);
        }
    }
}
