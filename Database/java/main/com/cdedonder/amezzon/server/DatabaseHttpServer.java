package com.cdedonder.amezzon.server;

import com.sun.net.httpserver.HttpServer;

import java.io.IOException;
import java.net.InetSocketAddress;
import java.util.Properties;
import java.util.concurrent.Executors;
import java.util.logging.Logger;

public class DatabaseHttpServer {

    private static final Logger LOGGER = Logger.getLogger(Logger.GLOBAL_LOGGER_NAME);

    private final HttpServer server;

    public DatabaseHttpServer(Properties properties) throws IOException {
        server = HttpServer.create(new InetSocketAddress(properties.getProperty("host"), Integer.parseInt(properties.getProperty("port"))), 0);
        server.createContext("/", new HttpExchangeHandler());
        server.setExecutor(Executors.newFixedThreadPool(Integer.parseInt(properties.getProperty("threads"))));
    }

    public static Properties defaultProperties() {
        Properties properties = new Properties();
        try {
            properties.load(DatabaseHttpServer.class.getResourceAsStream("default.properties"));
        } catch (IOException e) {
            LOGGER.severe("Cannot read default properties:\n" + e.getMessage());
        }
        return properties;
    }

    public void start() {
        server.start();
    }
}
