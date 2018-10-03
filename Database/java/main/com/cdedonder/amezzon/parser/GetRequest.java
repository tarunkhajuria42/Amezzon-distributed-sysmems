package com.cdedonder.amezzon.parser;

import java.util.List;

public class GetRequest {

    private String resultclass;
    private List<Integer> transaction;
    private List<Integer> transaction_type;
    private List<Integer> person;
    private List<Integer> product;
    private List<Integer> pile;
    private List<Integer> producttype;

    public String getResultclass() {
        return resultclass;
    }

    public void setResultclass(String resultclass) {
        this.resultclass = resultclass;
    }

    public List<Integer> getTransaction() {
        return transaction;
    }

    public void setTransaction(List<Integer> transaction) {
        this.transaction = transaction;
    }

    public List<Integer> getTransaction_type() {
        return transaction_type;
    }

    public void setTransaction_type(List<Integer> transaction_type) {
        this.transaction_type = transaction_type;
    }

    public List<Integer> getPerson() {
        return person;
    }

    public void setPerson(List<Integer> person) {
        this.person = person;
    }

    public List<Integer> getProduct() {
        return product;
    }

    public void setProduct(List<Integer> product) {
        this.product = product;
    }

    public List<Integer> getPile() {
        return pile;
    }

    public void setPile(List<Integer> pile) {
        this.pile = pile;
    }

    public List<Integer> getProducttype() {
        return producttype;
    }

    public void setProducttype(List<Integer> producttype) {
        this.producttype = producttype;
    }
}
