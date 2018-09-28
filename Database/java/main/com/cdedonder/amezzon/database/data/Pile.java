package com.cdedonder.amezzon.database.data;

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
}
