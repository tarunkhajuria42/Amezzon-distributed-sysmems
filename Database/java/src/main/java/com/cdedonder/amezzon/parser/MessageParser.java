package com.cdedonder.amezzon.parser;

import com.cdedonder.amezzon.database.QueryResultErrorMessageWrapper;
import com.cdedonder.amezzon.database.TransactionPool;
import com.cdedonder.amezzon.debugging.SocketProducer;
import com.cdedonder.amezzon.logging.DatabaseLogger;
import com.cdedonder.amezzon.parser.dto.DatabaseStatementRequest;
import com.cdedonder.amezzon.parser.dto.DatabaseStatementResponse;
import com.cdedonder.amezzon.parser.dto.InitializeTransactionResponse;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.IOException;
import java.io.StringReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.function.BiConsumer;
import java.util.logging.Logger;

public class MessageParser {

    private static final Logger LOGGER = DatabaseLogger.getLogger();

    private ObjectMapper objectMapper;

    private HashMap<String, BiConsumer<Message, JsonNode>> parserMap;

    private final TransactionPool transactionPool;

    private final SocketProducer socketProducer;

    public MessageParser() {
        objectMapper = new ObjectMapper();

        transactionPool = new TransactionPool();

        parserMap = new HashMap<>();
        parserMap.put("initialize transaction", this::initializeTransaction);
        parserMap.put("database statement", this::databaseStatement);
        //parserMap.put("debug message", this::debugMessage);

        socketProducer = new SocketProducer();
    }

    public Message parse(Message message) {
        LOGGER.info("Received message");
        //TODO PLUG IN GUI DEBUGGER
        try {
            String body = message.getBody();
            JsonNode node = objectMapper.readTree(new StringReader(body));
            String actionString = node.get("action").asText();
            JsonNode data = node.get("data");
            String dataString = data.asText();
            socketProducer.sendMessage(actionString, dataString);
            parserMap.get(actionString).accept(message, data);
        } catch (IOException e) {
            LOGGER.severe(e.getMessage());
        }
        return message;
    }

    private void initializeTransaction(Message message, JsonNode data) {
        try {
            LOGGER.info("Initialize new Transaction");
            String token = transactionPool.newTransactionInstance();
            InitializeTransactionResponse response = new InitializeTransactionResponse();
            if (token != null) {
                response.setToken(token);
                String json = wrapInData(objectMapper.writeValueAsString(response));
                message.setResponseCode(200);
                message.setResponseBody(json);
                LOGGER.info("Send Transaction token");
            } else {
                response.getErrorMessages().add("No connections available.");
                message.setResponseCode(300);
            }
            message.setResponseBody(wrapInData(objectMapper.writeValueAsString(response)));
        } catch (Exception e) {
            LOGGER.severe(e.getMessage());
        }
    }

    private void databaseStatement(Message message, JsonNode data) {
        LOGGER.info("Received statement");
        DatabaseStatementResponse response = new DatabaseStatementResponse();
        try {
            DatabaseStatementRequest request = objectMapper.treeToValue(data, DatabaseStatementRequest.class);
            List<DatabaseStatementResponse.ResultWrapper> results = new ArrayList<>();
            List<DatabaseStatementResponse.ErrorMessageWrapper> errors = new ArrayList<>();
            if (request.getStatementList() != null) {
                for (DatabaseStatementRequest.StatementWrapper wrapper : request.getStatementList()) {
                    QueryResultErrorMessageWrapper intermediateWrapper = transactionPool.processStatement(request.getTransactionToken(), wrapper.getStatement());

                    DatabaseStatementResponse.ResultWrapper resultWrapper = new DatabaseStatementResponse.ResultWrapper();
                    resultWrapper.setResultMessage(intermediateWrapper.getQueryResult());
                    resultWrapper.setStatementId(wrapper.getStatementId());
                    results.add(resultWrapper);

                    DatabaseStatementResponse.ErrorMessageWrapper errorWrapper = new DatabaseStatementResponse.ErrorMessageWrapper();
                    errorWrapper.setErrorMessage(intermediateWrapper.getError_message());
                    errorWrapper.setStatementId(wrapper.getStatementId());
                    errors.add(errorWrapper);
                }
            }
            response.setResultList(results);
            response.setErrorMessages(errors);

            message.setResponseCode(200);

        } catch (Exception e) {
            LOGGER.severe(e.getMessage());
            response.setStatementErrorMessages(new ArrayList<String>(1) {{
                add(e.getMessage());
            }});
        } finally {
            try {
                message.setResponseBody(wrapInData(objectMapper.writeValueAsString(response)));
            } catch (JsonProcessingException f) {
                LOGGER.severe(f.getMessage());
            }
        }
    }

    /*
    private void debugMessage(Message message, JsonNode data) {
        LOGGER.info("Received message");
        String text = data.asText();
        LOGGER.info("Message reads: " + text);
        message.setResponseCode(200);
        message.setResponseBody("Well received: " + text);
    }*/

    private static String wrapInData(String json) {
        return "{\"data\": " + json + "}";
    }
}
