package com.cdedonder.amezzon.parser;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.IOException;
import java.io.StringReader;
import java.util.HashMap;
import java.util.function.Consumer;
import java.util.logging.Logger;

public class MessageParser {

    private static final Logger LOGGER = Logger.getLogger(Logger.GLOBAL_LOGGER_NAME);

    private ObjectMapper objectMapper;

    private HashMap<String, Consumer<JsonNode>> parserMap;

    public MessageParser() {
        objectMapper = new ObjectMapper();

        parserMap = new HashMap<>();
        parserMap.put("initialize transaction", this::initializeTransaction);
        parserMap.put("database statement", this::databaseStatement);
    }

    public Message parse(Message message) {
        try {
            String body = message.getBody();
            JsonNode node = objectMapper.readTree(new StringReader(body));
            String actionString = node.get("action").asText();
            parserMap.get(actionString).accept(node.get("data"));
        }catch (IOException e){
            e.printStackTrace();
        }
        return null;
    }

    public void initializeTransaction(JsonNode data){

    }

    public void databaseStatement(JsonNode data){

    }
}
