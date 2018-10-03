package com.cdedonder.amezzon.database.data;

import java.io.IOException;

public class Pile extends AbstractDTO {

    private int id;
    private Product product;
    private double sell, buy;

    public Product getProduct() {
        return product;
    }

    public double getSell() {
        return sell;
    }

    public double getBuy() {
        return buy;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public void setProduct(Product product) {
        this.product = product;
    }

    public void setSell(double sell) {
        this.sell = sell;
    }

    public void setBuy(double buy) {
        this.buy = buy;
    }

    @Override
    public String toJSON() throws IOException {
        return objectMapper.writeValueAsString(this);
    }
}
