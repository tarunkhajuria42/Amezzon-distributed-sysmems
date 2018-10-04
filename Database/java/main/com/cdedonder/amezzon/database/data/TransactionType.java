package com.cdedonder.amezzon.database.data;

import java.io.IOException;

public class TransactionType extends AbstractDTO {

    private String transactionType;

    public String getTransactionType() {
        return transactionType;
    }

    public void setTransactionType(String transactionType) {
        this.transactionType = transactionType;
    }

    @Override
    public String toJSON() throws IOException {
        return objectMapper.writeValueAsString(this);
    }
}
