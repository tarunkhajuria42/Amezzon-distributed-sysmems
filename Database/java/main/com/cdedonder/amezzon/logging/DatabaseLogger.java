package com.cdedonder.amezzon.logging;

import java.io.IOException;
import java.util.logging.FileHandler;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.logging.SimpleFormatter;

public class DatabaseLogger {

    private static Logger LOGGER;

    public static void setup() throws IOException {
        LOGGER = Logger.getLogger(Logger.GLOBAL_LOGGER_NAME);

        /*Logger rootLogger = Logger.getLogger("");
        Handler[] handlers = rootLogger.getHandlers();
        if(handlers[0] instanceof ConsoleHandler){
            rootLogger.removeHandler(handlers[0]);
        }*/

        LOGGER.setLevel(Level.INFO);

        FileHandler fileHandler = new FileHandler("dblog.txt");
        SimpleFormatter formatter = new SimpleFormatter();
        fileHandler.setFormatter(formatter);
        LOGGER.addHandler(fileHandler);
    }

    public static Logger getLogger() {
        return LOGGER;
    }
}
