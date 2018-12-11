package com.cdedonder.amezzon.server;

import com.cdedonder.amezzon.parser.Message;
import com.cdedonder.amezzon.parser.MessageParser;
import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.logging.Logger;

public class HttpExchangeHandler implements HttpHandler {

    private static final Logger LOGGER = Logger.getLogger(Logger.GLOBAL_LOGGER_NAME);

    private MessageParser messageParser;

    public HttpExchangeHandler(){
        messageParser = new MessageParser();
    }

    @Override
    public void handle(HttpExchange exchange) throws IOException {
        LOGGER.info("Exchange received.");
        String method = exchange.getRequestMethod();
        StringBuilder sb = new StringBuilder();
        BufferedReader reader = new BufferedReader(new InputStreamReader(exchange.getRequestBody()));
        String line;
        while ((line = reader.readLine()) != null) {
            sb.append(line);
        }
        String body = sb.toString();
        System.out.println(body);
        try {
            Message message = messageParser.parse(new Message(method, body));
            exchange.sendResponseHeaders(message.getResponseCode(), 0);
            try (PrintWriter writer = new PrintWriter(exchange.getResponseBody(), true)) {
                writer.println(message.getResponseBody());
            }
        }catch (Exception e){
            LOGGER.severe(e.toString());
        }
        LOGGER.info("Exchange answered.");
    }
}
