package com.cdedonder.amezzon.parser;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class MessageParser {

    private final Map<String, Procedure> methodMap;
    private final Messsage messsage;

    public MessageParser(Messsage messsage) {
        this.messsage = messsage;
        methodMap = new HashMap<>();
        methodMap.put("PUT", this::parsePUT);
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

    private void parsePUT() {

    }

    private void parseGET() {

    }

    private void parseDELETE() {

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
