package com.cdedonder.amezzon.parser.classhandler;

import com.cdedonder.amezzon.database.DataAccesContext;

public abstract class AbstractClassHandler implements ClassHandler {

    private final DataAccesContext dataAccesContext;

    protected AbstractClassHandler(DataAccesContext dac) {
        this.dataAccesContext = dac;
    }

    protected DataAccesContext getDataAccessContext() {
        return dataAccesContext;
    }
}
