package com.cdedonder.amezzon.parser;

import com.cdedonder.amezzon.database.TransactionPool;
import com.cdedonder.amezzon.parser.dto.DatabaseStatementRequest;
import com.cdedonder.amezzon.parser.dto.DatabaseStatementResponse;
import com.cdedonder.amezzon.parser.dto.InitializeTransactionResponse;
import com.cdedonder.amezzon.parser.dto.QueryResult;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.IOException;
import java.io.StringReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.function.BiConsumer;
import java.util.function.Consumer;
import java.util.logging.Logger;

public class MessageParser {

    private static final Logger LOGGER = Logger.getLogger(Logger.GLOBAL_LOGGER_NAME);

    private ObjectMapper objectMapper;

    private HashMap<String, BiConsumer<Message, JsonNode>> parserMap;

    private final TransactionPool transactionPool;

    public MessageParser() {
        objectMapper = new ObjectMapper();

        transactionPool = new TransactionPool();

        parserMap = new HashMap<>();
        parserMap.put("initialize transaction", this::initializeTransaction);
        parserMap.put("database statement", this::databaseStatement);
        parserMap.put("debug message", this::debugMessage);
    }

    public Message parse(Message message) {
        try {
            String body = message.getBody();
            JsonNode node = objectMapper.readTree(new StringReader(body));
            String actionString = node.get("action").asText();
            parserMap.get(actionString).accept(message, node.get("data"));
        } catch (IOException e) {
            e.printStackTrace(); //TODO
        }
        return message;
    }

    private void initializeTransaction(Message message, JsonNode data) {
        try {
            String token = transactionPool.newTransactionInstance();
            InitializeTransactionResponse response = new InitializeTransactionResponse();
            response.setToken(token);
            String json = wrapInData(objectMapper.writeValueAsString(response));
            message.setResponseCode(200);
            message.setResponseBody(json);
        } catch (Exception e) {
            e.printStackTrace(); //TODO
        }
    }

    private void databaseStatement(Message message, JsonNode data) {
        //TODO error collecting
        try {
            DatabaseStatementRequest request = objectMapper.treeToValue(data, DatabaseStatementRequest.class);
            List<DatabaseStatementResponse.ResultWrapper> results = new ArrayList<>();
            for (DatabaseStatementRequest.StatementWrapper wrapper : request.getStatement_list()) {
                DatabaseStatementResponse.ResultWrapper resultWrapper = new DatabaseStatementResponse.ResultWrapper();
                resultWrapper.setResult_message(transactionPool.processStatement(request.getTransaction_token(), wrapper.getStatement()));
                resultWrapper.setStatement_id(wrapper.getStatement_id());
                results.add(resultWrapper);
            }
            DatabaseStatementResponse response = new DatabaseStatementResponse();
            response.setResult_list(results);
            message.setResponseCode(200);
            message.setResponseBody(wrapInData(objectMapper.writeValueAsString(response)));
        } catch (Exception e) {
            e.printStackTrace(); //DEBUG
        }
    }

    //DEBUG
    private void debugMessage(Message message, JsonNode data) {
        LOGGER.info("Received debug message");
        String text = data.asText();
        LOGGER.info("Message reads: " + text);
        message.setResponseCode(200);
        message.setResponseBody("Well received: " + text);
    }

    private static String wrapInData(String json) {
        return "{\"data\": " + json + "}";
    }
}
