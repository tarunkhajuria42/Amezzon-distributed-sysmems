package com.cdedonder.amezzon.database.data;

import java.io.IOException;

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

    public void setName(String name) {
        this.name = name;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public void setType(ProductType type) {
        this.type = type;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    @Override
    public String toJSON() throws IOException {
        return objectMapper.writeValueAsString(this);
    }
}
