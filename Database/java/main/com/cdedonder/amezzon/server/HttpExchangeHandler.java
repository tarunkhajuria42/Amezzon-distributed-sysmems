package com.cdedonder.amezzon.server;

import com.cdedonder.amezzon.parser.MessageParser;
import com.cdedonder.amezzon.parser.Messsage;
import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;

public class HttpExchangeHandler implements HttpHandler {

    @Override
    public void handle(HttpExchange exchange) throws IOException {
        String method = exchange.getRequestMethod();
        StringBuilder sb = new StringBuilder();
        BufferedReader reader = new BufferedReader(new InputStreamReader(exchange.getRequestBody()));
        String line;
        while ((line = reader.readLine()) != null) {
            sb.append(line);
        }
        String body = sb.toString();
        Messsage messsage = new MessageParser(new Messsage(method, body)).parse();
        exchange.sendResponseHeaders(messsage.getResponseCode(), 0);
        try (PrintWriter writer = new PrintWriter(exchange.getResponseBody(), true)) {
            writer.println(messsage.getResponseBody());
        }
    }
}
