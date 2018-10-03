package com.cdedonder.amezzon.database.data.mysql;

import com.cdedonder.amezzon.database.DataAccesContext;
import com.cdedonder.amezzon.database.DataAccessException;
import com.cdedonder.amezzon.database.data.Pile;
import com.cdedonder.amezzon.database.data.PileDAO;
import com.cdedonder.amezzon.database.data.Product;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Collection;

@SuppressWarnings("Duplicates")
public class MySQLPileDAO extends MySQLAbstractDAO implements PileDAO {

    private static final String CREATE_PILE = "INSERT INTO pile (pile_product, pile_sell, pile_buy) VALUES (?,?,?)";
    private static final String READ_PILE_BY_ID = "SELECT pile_id, pile_product, pile_sell, pile_buy FROM pile WHERE pile_id=?";
    private static final String READ_ALL = "SELEXT pile_id, pile_product, pile_sell, pile_buy FROM pile";
    private static final String READ_PILE_BY_PRODUCT = "SELECT pile_id, pile_product, pile_sell, pile_buy FROM pile WHERE pile_product=?";
    private static final String UPDATE_PILE = "UPDATE pile SET pile_product, pile_sell, pile_buy WHERE pile_id=?";
    private static final String DELETE_PILE = "DELETE FROM pile WHERE pile_id=?";
    private static final String DELETE_ALL = "DELETE FROM pile";
    private static final String PILE_EXITS = "SELECT 1 FROM pile WHERE pile_id=?";

    public MySQLPileDAO(Connection connection, DataAccesContext dac) {
        super(connection, dac);
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
        pile.setProduct(getDataAccesContext().getProductDAO().read(set.getInt("pile_product")));

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
    public Collection<Pile> readAll() {
        return null;
    }

    @Override
    public Pile readByProduct(Product product) {
        return null;
    }

    @Override
    public void update(Pile pile) {

    }

    @Override
    public void delete(Pile pile) {

    }

    @Override
    public void deleteAll() {

    }

    @Override
    public boolean exists(Pile pile) {
        return false;
    }
}
