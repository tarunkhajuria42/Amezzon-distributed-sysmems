package com.cdedonder.amezzon.server;

import com.sun.net.httpserver.HttpServer;

import java.io.IOException;
import java.net.InetSocketAddress;
import java.util.Properties;
import java.util.concurrent.Executors;

public class DatabaseHttpServer implements Server {

    private final HttpServer server;

    public DatabaseHttpServer(Properties properties) throws IOException {
        server = HttpServer.create(new InetSocketAddress(properties.getProperty("host"), Integer.parseInt(properties.getProperty("port"))), 0);
        server.createContext("/", new HttpExchangeHandler());
        server.setExecutor(Executors.newFixedThreadPool(Integer.parseInt(properties.getProperty("threads"))));
    }

    @Override
    public void start() {
        server.start();
    }
}
