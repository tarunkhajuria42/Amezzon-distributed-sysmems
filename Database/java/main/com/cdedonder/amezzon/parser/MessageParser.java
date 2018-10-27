package com.cdedonder.amezzon.parser;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.IOException;
import java.io.StringReader;
import java.util.HashMap;
import java.util.function.BiConsumer;
import java.util.function.Consumer;
import java.util.logging.Logger;

public class MessageParser {

    private static final Logger LOGGER = Logger.getLogger(Logger.GLOBAL_LOGGER_NAME);

    private ObjectMapper objectMapper;

    private HashMap<String, BiConsumer<Message, JsonNode>> parserMap;

    public MessageParser() {
        objectMapper = new ObjectMapper();

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
        }catch (IOException e){
            e.printStackTrace();
        }
        return message;
    }

    private void initializeTransaction(Message message, JsonNode data){

    }

    private void databaseStatement(Message message, JsonNode data){

    }

    //DEBUG
    private void debugMessage(Message message, JsonNode data){
        LOGGER.info("Received debug message");
        String text = data.asText();
        LOGGER.info("Message reads: " + text);
        message.setResponseCode(200);
        message.setResponseBody("Well received: " + text);
    }
}
