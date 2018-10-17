package com.cdedonder.amezzon;

import com.cdedonder.amezzon.database.data.Person;
import com.cdedonder.amezzon.database.data.Product;
import com.cdedonder.amezzon.database.data.Transaction;
import com.cdedonder.amezzon.database.data.TransactionType;
import org.junit.Assert;
import org.junit.BeforeClass;
import org.junit.Test;

import java.io.IOException;
import java.time.LocalDateTime;

public class JSONConversionTest {

    private static Transaction transaction;

    @BeforeClass
    public static void initClass() {
        transaction = new Transaction();
        transaction.setDateTime(LocalDateTime.now());
        Person person = new Person();
        person.setUsername("testUser");
        transaction.setClient(person);
        transaction.setId(10);
        transaction.setPrice(200.0);
        transaction.setQuantity(10);
        Product product = new Product();
        product.setName("Product1");
        transaction.setProduct(product);
        TransactionType type = new TransactionType();
        type.setTransactionType("BUYING");
        transaction.setType(type);
    }

    @Test
    public void testToJson() throws IOException {
        System.out.println(transaction.toJSON());
    }

    @Test
    public void testFromJSON() throws IOException {
        Assert.assertEquals(transaction.toString(), Transaction.fromJSON(transaction.toJSON()).toString());
    }
}
