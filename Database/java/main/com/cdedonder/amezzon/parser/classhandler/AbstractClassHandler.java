package com.cdedonder.amezzon.parser.classhandler;

import com.cdedonder.amezzon.database.DataAccesContext;
import com.fasterxml.jackson.databind.ObjectMapper;

public abstract class AbstractClassHandler implements ClassHandler {

    private final DataAccesContext dataAccesContext;
    protected final ObjectMapper objectMapper;

    public AbstractClassHandler(DataAccesContext dac) {
        this.dataAccesContext = dac;
        objectMapper = new ObjectMapper();
    }

    protected DataAccesContext getDataAccessContext() {
        return dataAccesContext;
    }
}
