package com.cdedonder.amezzon.parser;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.logging.Logger;

public class MessageParser {

    private static final Logger LOGGER = Logger.getLogger(Logger.GLOBAL_LOGGER_NAME);

    private final Map<String, Procedure> methodMap;
    private final Messsage messsage;

    public MessageParser(Messsage messsage) {
        this.messsage = messsage;
        methodMap = new HashMap<>();
        methodMap.put("POST", this::parsePOST);
        methodMap.put("GET", this::parseGET);
        methodMap.put("DELETE", this::parseDELETE);
    }

    public Messsage parse() throws IOException {
        if (methodMap.containsKey(messsage.getMethod().toUpperCase())) {
            methodMap.get(messsage.getMethod().toUpperCase()).execute();
        } else {
            throw new IOException("Message method unknown: " + messsage.getMethod());
        }
        return messsage;
    }

    private void parsePOST() {
        //DEBUG
        LOGGER.info("Message received:\n" + messsage.getBody());
        messsage.setResponseCode(200);
        messsage.setResponseBody("Hello Client!");
        //DEBUG ENDS
        //TODO
    }

    private void parseGET() {
        //TODO
    }

    private void parseDELETE() {
        //TODO
    }

    @FunctionalInterface
    private interface Procedure {

        void execute();

        default Procedure andThen(final Procedure after) {
            return () -> {
                execute();
                after.execute();
            };
        }

        default Procedure compose(final Procedure before) {
            return () -> {
                before.execute();
                execute();
            };
        }
    }
}
