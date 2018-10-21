package com.cdedonder.amezzon;

import com.cdedonder.amezzon.server.DatabaseHttpServer;
import com.cdedonder.amezzon.server.DatabaseHttpsServer;

import java.io.IOException;
import java.util.Properties;

public class HttpsServerTest {

    public static void main(String[] args) throws IOException {
        Properties properties = new Properties();
        properties.load(DatabaseHttpServer.class.getResourceAsStream("default.properties"));
        DatabaseHttpsServer server = new DatabaseHttpsServer(properties);
        server.start();
    }
}
