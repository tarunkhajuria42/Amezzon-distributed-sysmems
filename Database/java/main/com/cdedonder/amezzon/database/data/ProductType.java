package com.cdedonder.amezzon.database.data;

import java.io.IOException;

public class ProductType extends AbstractDTO {

    private String productType;

    public String getProductType() {
        return productType;
    }

    public void setProductType(String productType) {
        this.productType = productType;
    }

    @Override
    public String toJSON() throws IOException {
        return objectMapper.writeValueAsString(this);
    }
}
