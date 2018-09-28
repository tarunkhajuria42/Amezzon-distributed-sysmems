package com.cdedonder.amezzon;

import com.cdedonder.amezzon.logging.DatabaseLogger;

import java.io.IOException;

public class Main {

    public static void main(String[] args) {
        try {
            DatabaseLogger.setup();
        } catch (IOException e) {
            throw new RuntimeException("Cannot create logger instance:\n" + e.getMessage());
        }
    }
}
