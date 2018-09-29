package com.cdedonder.amezzon.server;

import com.sun.net.httpserver.HttpServer;

import java.io.IOException;
import java.net.InetSocketAddress;
import java.util.Properties;
import java.util.concurrent.Executors;
import java.util.logging.Logger;

public class DatabaseHttpServer implements Server {

    private static final Logger LOGGER = Logger.getLogger(Logger.GLOBAL_LOGGER_NAME);

    private final HttpServer server;

    public DatabaseHttpServer(Properties properties) throws IOException {
        String host = properties.getProperty("host");
        int port = Integer.parseInt(properties.getProperty("port"));
        server = HttpServer.create(new InetSocketAddress(host, port), 0);
        LOGGER.info("Created server at" + host + ":" + port);
        server.createContext("/", new HttpExchangeHandler());
        server.setExecutor(Executors.newFixedThreadPool(Integer.parseInt(properties.getProperty("threads"))));
    }

    @Override
    public void start() {
        LOGGER.info("Starting server.");
        server.start();
        LOGGER.info("Server started.");
    }
}
