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
import java.util.function.Supplier;
import java.util.logging.Logger;

public class MessageParser {

    private static final Logger LOGGER = Logger.getLogger(Logger.GLOBAL_LOGGER_NAME);

    private final Map<String, Supplier<InternalResponse>> methodMap;
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
            //TODO LOG
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

    public Messsage parse() {
        if (methodMap.containsKey(messsage.getMethod().toUpperCase())) {
            InternalResponse response = methodMap.get(messsage.getMethod().toUpperCase()).get();
            messsage.setResponseCode(response.getResponseCode());
            messsage.setResponseBody(response.getResponseBody());
        } else {
            messsage.setResponseCode(300);
        }
        return messsage;
    }

    private InternalResponse parsePUT() {
        try {
            PutRequest putRequest = objectMapper.readValue(messsage.getBody(), PutRequest.class);
            return classHandlerMap.get(putRequest.getObjectclass()).put(putRequest);
        } catch (IOException e) {
            InternalResponse response = new InternalResponse();
            response.setResponseCode(310);
            return response;
        }
    }

    private InternalResponse parseGET() {
        try {
            GetRequest getRequest = objectMapper.readValue(messsage.getBody(), GetRequest.class);
            return classHandlerMap.get(getRequest.getResultclass()).get(getRequest);
        } catch (IOException e) {
            InternalResponse response = new InternalResponse();
            response.setResponseCode(310);
            return response;
        }
    }

    private InternalResponse parseDELETE() {
        try {
            DeleteRequest deleteRequest = objectMapper.readValue(messsage.getBody(), DeleteRequest.class);
            return classHandlerMap.get(deleteRequest.getObjectclass()).delete(deleteRequest);
        } catch (IOException e) {
            InternalResponse response = new InternalResponse();
            response.setResponseCode(310);
            return response;
        }
    }
}
