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

        socketProducer = new SocketProducer();
    }

    public Message parse(Message message) {
        LOGGER.info("Received message");
        try {
            String body = message.getBody();
            JsonNode node = objectMapper.readTree(new StringReader(body));
            String actionString = node.get("action").asText();
            JsonNode data = node.get("data");
            String dataString = data.toString();
            socketProducer.sendMessage(actionString, dataString);
            parserMap.get(actionString).accept(message, data);
        } catch (IOException e) {
            LOGGER.severe(e.getMessage());
        }
        return message;
    }

    @SuppressWarnings("unused")
    private void initializeTransaction(Message message, JsonNode _data) {
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
                    LOGGER.info(wrapper.getStatement());
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

        } catch (JsonProcessingException e) {
            LOGGER.severe(e.getMessage());
            ArrayList<String> errorMessages = new ArrayList<>(1);
            errorMessages.add(e.getMessage());
            response.setStatementErrorMessages(errorMessages);
        } catch (Exception ignored) {
        } finally {
            try {
                message.setResponseBody(wrapInData(objectMapper.writeValueAsString(response)));
            } catch (JsonProcessingException f) {
                response.getStatementErrorMessages().add(f.getMessage());
                LOGGER.severe(f.getMessage());
            }
        }
    }

    private static String wrapInData(String json) {
        return "{\"data\": " + json + "}";
    }
}
