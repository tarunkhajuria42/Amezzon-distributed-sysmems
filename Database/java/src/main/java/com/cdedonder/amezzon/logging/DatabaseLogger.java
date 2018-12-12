package com.cdedonder.amezzon.logging;

import java.io.IOException;
import java.util.logging.*;

public class DatabaseLogger {

    private static Logger LOGGER = Logger.getLogger(Logger.GLOBAL_LOGGER_NAME);

    public static void setup() throws IOException {
        setup(Level.SEVERE, false);
    }

    public static void setup(Level level, boolean displayOnTerminal) throws IOException {
        if (!displayOnTerminal) {
            Logger rootLogger = Logger.getLogger("");
            Handler[] handlers = rootLogger.getHandlers();
            if (handlers[0] instanceof ConsoleHandler) {
                rootLogger.removeHandler(handlers[0]);
            }
        }

        LOGGER.setLevel(level);

        FileHandler fileHandler = new FileHandler("dblog.txt");
        SimpleFormatter formatter = new SimpleFormatter();
        fileHandler.setFormatter(formatter);
        LOGGER.addHandler(fileHandler);
    }

    public static Logger getLogger() {
        return LOGGER;
    }
}
