package com.cdedonder.amezzon.database;

import java.util.Properties;

public interface DataAccesProvider {
    DataAccesContext getDataAccessContext(Properties properties) throws DataAccessException;
}
