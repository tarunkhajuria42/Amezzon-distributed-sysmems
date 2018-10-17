package com.cdedonder.amezzon.database.data;

import com.fasterxml.jackson.databind.DeserializationFeature;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.IOException;

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

    static {
        objectMapper.configure(DeserializationFeature.FAIL_ON_NULL_FOR_PRIMITIVES, false);
    }

    public abstract String toJSON() throws IOException;
}
