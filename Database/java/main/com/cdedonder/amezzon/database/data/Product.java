package com.cdedonder.amezzon.database.data;

public class Product extends AbstractDTO {

    private int id;
    private String name, description;
    private ProductType type;

    public String getName() {
        return name;
    }

    public String getDescription() {
        return description;
    }

    public ProductType getType() {
        return type;
    }
}
