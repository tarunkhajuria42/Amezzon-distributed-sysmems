package com.cdedonder.amezzon.database.data;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.ObjectReader;

abstract class AbstractDTO {

    @Override
    public boolean equals(Object obj) {
        return ReflectEquals.equals(this, obj);
    }

    @Override
    public String toString() {
        return ReflectToString.toString(this);
    }

    protected static final ObjectMapper objectMapper = new ObjectMapper();
    protected static final ObjectReader objectReader = objectMapper.reader();

    public abstract String toJSON();
}
