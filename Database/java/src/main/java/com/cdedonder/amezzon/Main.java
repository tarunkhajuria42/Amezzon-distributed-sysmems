package com.cdedonder.amezzon;

import com.cdedonder.amezzon.logging.DatabaseLogger;
import com.cdedonder.amezzon.server.DatabaseHttpServer;
import com.cdedonder.amezzon.server.Server;
import org.apache.commons.cli.*;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.Properties;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Main {

    private final static Map<String, ExceptionFunction<Properties, Server>> serverMap;
    private static Options options;
    private static HelpFormatter formatter;

    static {
        serverMap = new HashMap<>();
        serverMap.put("http", DatabaseHttpServer::new);
        serverMap.put("https", DatabaseHttpServer::new);
    }

    public static void main(String[] args) {
        options = new Options();
        Option httpType = new Option("t", "type", true, "use either http or https");
        httpType.setRequired(true);
        options.addOption(httpType);
        Option logType = new Option("l", "logging", false, "set flag to use debug logging");
        logType.setRequired(false);
        options.addOption(logType);
        Option displayType = new Option("d", "display-on-terminal", false, "set flag to direct logging to terminal");
        displayType.setRequired(false);
        options.addOption(displayType);

        CommandLineParser parser = new DefaultParser();
        formatter = new HelpFormatter();

        try {
            CommandLine cmd = parser.parse(options, args);
            try {
                DatabaseLogger.setup(cmd.hasOption("logging") ? Level.INFO : Level.SEVERE, cmd.hasOption("display-on-terminal"));
            } catch (IOException e) {
                System.err.println("Cannot create logger instance:\n" + e.getMessage());
                System.exit(1);
            }
            String type = cmd.getOptionValue("type");
            if (serverMap.containsKey(type.toLowerCase())) {
                Properties properties = Server.defaultProperties();
                try {
                    serverMap.get(type.toLowerCase()).apply(properties).start();
                } catch (Exception e) {
                    Logger LOGGER = Logger.getLogger(Logger.GLOBAL_LOGGER_NAME);
                    LOGGER.severe("Cannot setup server: " + e.getMessage());
                }
            } else {
                helpAndExit();
            }
        } catch (ParseException e) {
            System.out.println(e.getMessage());
            helpAndExit();
        }
    }

    private static void helpAndExit() {
        formatter.printHelp("Database Server", options);
        System.exit(1);
    }

    @FunctionalInterface
    private interface ExceptionFunction<A, B> {
        B apply(A a) throws Exception;
    }
}
