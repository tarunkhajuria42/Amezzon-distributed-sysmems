package com.cdedonder.amezzon.database;

public class GenericServerError extends Exception {

    public GenericServerError(Exception e) {
        super(e);
    }
}
