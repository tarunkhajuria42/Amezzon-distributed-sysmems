package com.cdedonder.amezzon.database.data;

abstract class AbstractDTO {

    @Override
    public boolean equals(Object obj) {
        return ReflectEquals.equals(this, obj);
    }

    @Override
    public String toString() {
        return ReflectToString.toString(this);
    }
}
