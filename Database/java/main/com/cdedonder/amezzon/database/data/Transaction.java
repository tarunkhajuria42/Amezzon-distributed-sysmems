package com.cdedonder.amezzon.database.data;

import com.cdedonder.amezzon.database.data.util.LocalDateTimeDeserializer;
import com.cdedonder.amezzon.database.data.util.LocalDateTimeSerializer;
import com.fasterxml.jackson.databind.annotation.JsonDeserialize;
import com.fasterxml.jackson.databind.annotation.JsonSerialize;

import java.io.IOException;
import java.time.LocalDateTime;

public class Transaction extends AbstractDTO {

    private int id;
    private TransactionType type;
    private Person client;
    private Product product;
    private double price;
    private int quantity;

    @JsonSerialize(using = LocalDateTimeSerializer.class)
    @JsonDeserialize(using = LocalDateTimeDeserializer.class)
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

    public static Transaction fromJSON(String json) throws IOException {
        return objectMapper.readValue(json, Transaction.class);
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public void setType(TransactionType type) {
        this.type = type;
    }

    public void setClient(Person client) {
        this.client = client;
    }

    public void setProduct(Product product) {
        this.product = product;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    public void setDateTime(LocalDateTime dateTime) {
        this.dateTime = dateTime;
    }

    @Override
    public String toJSON() throws IOException {
        return objectMapper.writeValueAsString(this);
    }
}
