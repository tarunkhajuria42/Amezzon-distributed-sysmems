package com.cdedonder.amezzon.database.data;

import java.time.LocalDateTime;

public class Transaction extends AbstractDTO {

    private int id;
    private TransactionType type;
    private Person client;
    private Product product;
    private double price;
    private int quantity;
    private LocalDateTime dateTime;

    public TransactionType getType() {
        return type;
    }

    public Person getClient() {
        return client;
    }

    public Product getProduct() {
        return product;
    }

    public double getPrice() {
        return price;
    }

    public int getQuantity() {
        return quantity;
    }

    public LocalDateTime getDateTime() {
        return dateTime;
    }
}
