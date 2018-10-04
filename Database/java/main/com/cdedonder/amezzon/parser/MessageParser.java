package com.cdedonder.amezzon.parser;

import com.cdedonder.amezzon.database.DataAccesContext;
import com.cdedonder.amezzon.database.DataAccesProvider;
import com.cdedonder.amezzon.database.DataAccessException;
import com.cdedonder.amezzon.database.mysql.MySQLDAP;
import com.cdedonder.amezzon.parser.classhandler.*;
import com.cdedonder.amezzon.parser.request.DeleteRequest;
import com.cdedonder.amezzon.parser.request.GetRequest;
import com.cdedonder.amezzon.parser.request.PutRequest;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.Properties;
import java.util.logging.Logger;

public class MessageParser {

    private static final Logger LOGGER = Logger.getLogger(Logger.GLOBAL_LOGGER_NAME);

    private final Map<String, Procedure> methodMap;
    private final Map<String, ClassHandler> classHandlerMap;

    private final Messsage messsage;

    private ObjectMapper objectMapper;

    public MessageParser(Messsage messsage) {
        this.messsage = messsage;

        methodMap = new HashMap<>();
        methodMap.put("PUT", this::parsePUT);
        methodMap.put("GET", this::parseGET);
        methodMap.put("DELETE", this::parseDELETE);

        DataAccesProvider dap = new MySQLDAP();
        Properties properties = new Properties();
        DataAccesContext dac = null; //TODO CLEANUP
        try {
            properties.load(getClass().getResourceAsStream("database.properties"));
            dac = dap.getDataAccessContext(properties);
        } catch (DataAccessException | IOException ignored) {
        }

        classHandlerMap = new HashMap<>();
        classHandlerMap.put("person", new PersonClassHandler(dac));
        classHandlerMap.put("pile", new PileClassHandler(dac));
        classHandlerMap.put("product", new ProductClassHandler(dac));
        classHandlerMap.put("producttype", new ProductTypeClassHandler(dac));
        classHandlerMap.put("transaction", new TransactionClassHandler(dac));
        classHandlerMap.put("transactiontype", new TransactionTypeClassHandler(dac));

        objectMapper = new ObjectMapper();
    }

    public Messsage parse() throws IOException {
        if (methodMap.containsKey(messsage.getMethod().toUpperCase())) {
            methodMap.get(messsage.getMethod().toUpperCase()).execute();
        } else {
            throw new IOException("Message method unknown: " + messsage.getMethod());
        }
        return messsage;
    }

    private void parsePUT() throws IOException {
        PutRequest putRequest = objectMapper.readValue(messsage.getBody(), PutRequest.class);
        classHandlerMap.get(putRequest.getObjectclass()).put(putRequest);
    }

    private void parseGET() throws IOException {
        GetRequest getRequest = objectMapper.readValue(messsage.getBody(), GetRequest.class);
        classHandlerMap.get(getRequest.getResultclass()).get(getRequest);
    }

    private void parseDELETE() throws IOException {
        DeleteRequest deleteRequest = objectMapper.readValue(messsage.getBody(), DeleteRequest.class);
        classHandlerMap.get(deleteRequest.getObjectclass()).delete(deleteRequest);
    }

    @FunctionalInterface
    private interface Procedure {

        void execute() throws IOException;

        /*default Procedure andThen(final Procedure after) {
            return () -> {
                execute();
                after.execute();
            };
        }

        default Procedure compose(final Procedure before) {
            return () -> {
                before.execute();
                execute();
            };
        }*/
    }
}
