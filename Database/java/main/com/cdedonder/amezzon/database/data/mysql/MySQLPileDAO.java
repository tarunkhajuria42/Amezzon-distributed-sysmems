package com.cdedonder.amezzon.database.data.mysql;

import com.cdedonder.amezzon.database.DataAccesContext;
import com.cdedonder.amezzon.database.data.PileDAO;

import java.sql.Connection;

public class MySQLPileDAO extends MySQLAbstractDAO implements PileDAO {

    public MySQLPileDAO(Connection connection, DataAccesContext dac) {
        super(connection, dac);
    }
}
