package com.cdedonder.amezzon.server;

import java.io.IOException;
import java.util.Properties;
import java.util.logging.Logger;

public interface Server {

    static Properties defaultProperties() {
        Logger LOGGER = Logger.getLogger(Logger.GLOBAL_LOGGER_NAME);
        Properties properties = new Properties();
        try {
            properties.load(DatabaseHttpServer.class.getResourceAsStream("/default.properties"));
        } catch (IOException e) {
            LOGGER.severe("Cannot read default properties:\n" + e.getMessage());
        }
        return properties;
    }

    void start();
}
