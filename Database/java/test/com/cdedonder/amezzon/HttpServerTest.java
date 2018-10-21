package com.cdedonder.amezzon;

import com.cdedonder.amezzon.server.DatabaseHttpServer;

import java.io.IOException;
import java.util.Properties;

public class HttpServerTest {

    public static void main(String[] args) throws IOException {
        Properties properties = new Properties();
        properties.load(DatabaseHttpServer.class.getResourceAsStream("default.properties"));
        DatabaseHttpServer server = new DatabaseHttpServer(properties);
        server.start();
    }
}
